import telebot
import os
# from telebot import types
from datetime import datetime as dt
import json

bot = telebot.TeleBot(os.getenv('TG_Bot'))


def read_data() -> dict:
    try:
        with open('tg_bot_database.json') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


users_sleep_data = read_data()


def write_data() -> None:
    with open('tg_bot_database.json', 'w') as file:
        json.dump(users_sleep_data, file)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f'Привет, я буду помогать тебе отслеживать параметры сна.\n'
                                      f'Используй команды /sleep, /wake, /quality, /notes и /info.')


@bot.message_handler(commands=["sleep"])
def sleep(message):
    if not users_sleep_data.get(f'{message.from_user.id}'):
        users_sleep_data[f'{message.from_user.id}'] = {'sleep_status': dt.now().strftime('%Y-%m-%d %H:%M:%S'),
                                                       'user_data': {}}
        bot.send_message(message.chat.id, f'Привет, данные сохранены, приятных снов.')
        write_data()
        return
    if not users_sleep_data[f'{message.from_user.id}'].get('sleep_status'):
        users_sleep_data[f'{message.from_user.id}']['sleep_status'] = dt.now().strftime('%Y-%m-%d %H:%M:%S')
        bot.send_message(message.chat.id, f'Привет, данные сохранены, приятных снов.')
        write_data()
        return
    bot.send_message(message.chat.id, f'Команда "/wake" не была введена и счетчик сна все еще работает.')


@bot.message_handler(commands=["wake"])
def wake(message):
    if not users_sleep_data.get(f'{message.from_user.id}'):
        bot.send_message(message.chat.id, f'Данные об отходе ко сну отсутствуют, введите команду "/sleep".')
        return
    if not users_sleep_data[f'{message.from_user.id}']['sleep_status'][0]:
        bot.send_message(message.chat.id, f'Данные об отходе ко сну отсутствуют, введите команду "/sleep".')
        return
    today = dt.now()
    today_str = today.strftime('%Y-%m-%d')
    yesterday_str = users_sleep_data[f'{message.from_user.id}']['sleep_status']
    yesterday = dt.strptime(yesterday_str, '%Y-%m-%d %H:%M:%S')
    duration = (today - yesterday).seconds
    new_note = {'start_sleep': yesterday_str,
                'duration': duration,
                'quality': None,
                'notes': ''}
    if not users_sleep_data[f'{message.from_user.id}']['user_data'].get(today_str):
        users_sleep_data[f'{message.from_user.id}']['user_data'][today_str] = [new_note]
    else:
        users_sleep_data[f'{message.from_user.id}']['user_data'][today_str].append(new_note)
    del users_sleep_data[f'{message.from_user.id}']['sleep_status']
    bot.send_message(message.chat.id, f'Вы проспали {users_sleep_data[f"{message.from_user.id}"]["user_data"][today_str][-1]["duration"]}\n'
                                      f'Используйте команды "/quality" и "/notes" для оценки качества сна и заметок')
    write_data()


@bot.message_handler(commands=["quality"])
def quality(message):
    try:
        users_sleep_data[f'{message.from_user.id}']['user_data'][f'{dt.now().strftime("%Y-%m-%d")}'][-1]["quality"] = message.text.split()[1]
        bot.send_message(message.chat.id, f'Оценка сохранена')
        write_data()
    except IndexError:
        bot.send_message(message.chat.id, f'Некорректный ввод данных.')
    except KeyError:
        bot.send_message(message.chat.id, f'Сессия не найдена.')


@bot.message_handler(commands=["notes"])
def notes(message):
    try:
        users_sleep_data[f'{message.from_user.id}']['user_data'][f'{dt.now().strftime("%Y-%m-%d")}'][-1]["notes"] = f'{" ".join(message.text.split()[1:])}'
        bot.send_message(message.chat.id, f'Заметка сохранена')
        write_data()
    except KeyError:
        bot.send_message(message.chat.id, f'Сессия не найдена.')


@bot.message_handler(commands=["info"])
def info(message):
    try:
        for day in users_sleep_data[f'{message.from_user.id}']['user_data'].items():
            bot.send_message(message.chat.id, f'Данные за {day[0]}')
            for i, date in enumerate(day[1]):
                bot.send_message(message.chat.id, f'Запись №{i + 1}:'
                                                  f' продолжительность сна - {date["duration"]},'
                                                  f' оценка - {date["quality"]},'
                                                  f' заметка - {date["notes"]}')
    except KeyError:
        bot.send_message(message.chat.id, f'Пока нет данных о Вашем сне.')


'''@bot.message_handler(content_types=["text"])
def handle_text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('юзердата')
    button2 = types.KeyboardButton('юзерстатус')
    button3 = types.KeyboardButton('Запись')
    markup.add(button1, button2, button3)
    user_choice = message.text
    if user_choice == 'юзердата':
        bot.send_message(message.chat.id, f'{users_sleep_data}', reply_markup=markup)
    if user_choice == 'юзерстатус':
        bot.send_message(message.chat.id, f'{users_sleep_data[f"{message.from_user.id}"]["sleep_status"]}')
    if user_choice == 'Запись':
        write_data()
        bot.send_message(message.chat.id, f'Данные записаны')'''


bot.polling(none_stop=True, interval=0)
