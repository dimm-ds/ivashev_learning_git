import telebot
import os
from sqlite3 import connect
from datetime import datetime as dt


bot = telebot.TeleBot(os.getenv('TG_Bot'))


def get_attribute_query(date):
    if isinstance(date, tuple):
        columns = ', '.join(str(e) for e in date)
        return columns
    if isinstance(date, dict):
        columns = ', '.join(str(e) for e in date.keys())
        substitution = ', '.join('?' for i in range(len(date)))
        values = tuple(date.values())
        return columns, substitution, values


def connector(func):
    def wrapper(*args, **kwargs):
        conn = connect("sleep_bot.db")
        cursor = conn.cursor()
        result = func(cursor, *args, **kwargs)

        conn.commit()
        cursor.close()
        conn.close()
        return result
    return wrapper


@connector
def great_query(cursor, query):
    if 'VIEW' not in query:
        return cursor.execute(query).fetchall()
    cursor.execute(query)
    return


users = '''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT
        );
        '''
sleep_records = '''
        CREATE TABLE IF NOT EXISTS sleep_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            sleep_time DATETIME,
            wake_time DATETIME DEFAULT NULL,
            sleep_quality INTEGER DEFAULT NULL
        );
        '''
notes = '''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            sleep_records_id INTEGER
        );
        '''
joined_view = '''
        CREATE VIEW IF NOT EXISTS joined_view AS
        SELECT sr.user_id, sr.sleep_time, sr.wake_time, sr.sleep_quality, n.text
        FROM sleep_records sr
        LEFT JOIN notes n ON sr.id = n.sleep_records_id;
        '''

great_query(users)
great_query(sleep_records)
great_query(notes)
great_query(joined_view)


@connector
def get_info(cursor, table, **kwargs):
    columns, substitution, values = get_attribute_query(kwargs)
    answer = cursor.execute(
        f"""SELECT * FROM {table}
        WHERE {columns}=?;""",
        values
    ).fetchall()
    return answer


@connector
def add_info(cursor, table, **kwargs):
    columns, substitution, values = get_attribute_query(kwargs)
    cursor.execute(
        f"""
        INSERT INTO {table} ({columns}) 
        VALUES ({substitution});
        """,
        values
    )


@connector
def change_info(cursor, table, **kwargs):
    columns = list(e for e in kwargs.keys())
    values = tuple(kwargs.values())
    if len(columns) == 3:
        cursor.execute(
            f'''
            UPDATE {table}
            SET {columns[0]}=?
            WHERE {columns[1]}=? AND {columns[2]}=?
            ''',
            values
        )
    if len(columns) == 2:
        cursor.execute(
            f'''
            UPDATE {table}
            SET {columns[0]}=?
            WHERE {columns[1]}=?
            ''',
            values
        )



@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f'Привет, я буду помогать тебе отслеживать параметры сна.\n'
                                      f'Используй команды /sleep, /wake, /quality, /notes и /info.')


@bot.message_handler(commands=["sleep"])
def sleep(message):
    if not get_info('users', user_id=message.from_user.id):
        add_info('users', user_id=message.from_user.id, name=message.from_user.username)
    last_note = get_info('sleep_records', user_id=message.from_user.id)
    if len(last_note) == 0 or last_note[-1][3] is not None:
        add_info('sleep_records', user_id=message.from_user.id, sleep_time=dt.now())
        bot.send_message(message.chat.id, f'Привет, данные сохранены, приятных снов.')
        return
    bot.send_message(message.chat.id, f'Команда "/wake" не была введена и счетчик сна все еще работает.')


@bot.message_handler(commands=["wake"])
def wake(message):
    last_note = get_info('sleep_records', user_id=message.from_user.id)
    if not get_info('users', user_id=message.from_user.id) or\
            last_note[-1][2] is None or\
            last_note[-1][3] is not None:
        bot.send_message(message.chat.id, f'Данные об отходе ко сну отсутствуют, введите команду "/sleep".')
        return
    now = dt.now()
    change_info('sleep_records', wake_time=now, user_id=message.from_user.id, sleep_time=last_note[-1][2])
    bot.send_message(message.chat.id,
                     f'Вы проспали {(now - dt.strptime(last_note[-1][2], "%Y-%m-%d %H:%M:%S.%f")).seconds} секунд\n'
                     f'Используйте команды "/quality" и "/notes" для оценки качества сна и заметок')


@bot.message_handler(commands=["quality"])
def quality(message):
    last_note = get_info('sleep_records', user_id=message.from_user.id)
    if not get_info('users', user_id=message.from_user.id) or not last_note:
        bot.send_message(message.chat.id, f'Сессия не найдена.')
        return
    try:
        user_quality = int(message.text.split()[1])
        if user_quality not in range(0, 6):
            bot.send_message(message.chat.id, f'Некорректный ввод данных. Введите значение от 0 до 5.')
            return
        change_info('sleep_records', sleep_quality=user_quality, id=last_note[-1][0])
        bot.send_message(message.chat.id, f'Оценка сохранена.')
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, f'Некорректный ввод данных.')


@bot.message_handler(commands=["notes"])
def notes(message):
    last_note = get_info('sleep_records', user_id=message.from_user.id)
    if not get_info('users', user_id=message.from_user.id) or not last_note:
        bot.send_message(message.chat.id, f'Сессия не найдена.')
        return
    if not message.text.split()[1:]:
        bot.send_message(message.chat.id, f'Невозможно сохранить пустую заметку, введите данные.')
        return
    add_info('notes', text=" ".join(message.text.split()[1:]), sleep_records_id =last_note[-1][0])
    bot.send_message(message.chat.id, f'Заметка сохранена')



@bot.message_handler(commands=["info"])
def info(message):
    answer = get_info('joined_view', user_id=message.from_user.id)
    print(answer)
    if not answer:
        bot.send_message(message.chat.id, 'Данных не найдено, начните пользоваться ботом.')
    for i in answer:
        if not i[2]:
            bot.send_message(message.chat.id, 'Завершенных сессий не найдено, нажмите /wake.')
            break
        bot.send_message(message.chat.id, f'Вы заснули {i[1].split(".")[0]}, '
                                          f'проспав в общей сложности {dt.strptime(i[2].split(".")[0], "%Y-%m-%d %H:%M:%S")  - dt.strptime(i[1].split(".")[0], "%Y-%m-%d %H:%M:%S")}'
                                          f' и оценив свой сон на {i[3]} из 5ти.\n'
                                          f'Так же был добавлен комментарий: "{i[4]}"')


bot.polling(none_stop=True, interval=0)



