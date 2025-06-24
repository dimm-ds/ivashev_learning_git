import telebot
import os
#from telebot import types
from datetime import datetime
import json

bot = telebot.TeleBot(os.getenv('TG_Bot'))


def read_date() -> list:
    try:
        with open('tg_bot_database.json') as file:
            return json.load(file)
    except FileNotFoundError:
        return [{}, {}]


user_sleep_status, users_sleep_data = read_date()


def write_date() -> None:
    with open('tg_bot_database.json', 'w') as file:
        json.dump([user_sleep_status, users_sleep_data], file)


def get_date() -> str:
    td = datetime.now()
    return f'{td.day}-{td.month}-{td.year}'


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f'Привет, я буду помогать тебе отслеживать параметры сна.\n'
                                      f'Используй команды /sleep, /wake, /quality, /notes и /info.')


@bot.message_handler(commands=["sleep"])
def sleep(message):
    sleep_now = user_sleep_status.get(f'{message.chat.id}', [False])  # хранит данные в словаре
    if not sleep_now[0]:
        user_sleep_status[f'{message.chat.id}'] = [True, datetime.now()]
        bot.send_message(message.chat.id, f'Привет, данные сохранены, приятных снов.')
        return
    bot.send_message(message.chat.id, f'Команда "/wake" не была введена и счетчик сна все еще работает.')


@bot.message_handler(commands=["wake"])
def wake(message):
    sleep_now = user_sleep_status.get(f'{message.chat.id}', [False])
    if not sleep_now[0]:
        bot.send_message(message.chat.id, f'Данные об отходе ко сну отсутствуют, введите команду "/sleep".')
        return
    today = get_date()
    yesterday = user_sleep_status[f'{message.chat.id}'][1]
    sleep_delta = (datetime.now() - yesterday).seconds
    new_note = {'start_sleep': f'{yesterday}',
                'duration': f'{sleep_delta // 3600} часов {sleep_delta % 3600 // 60} минут',
                'quality': 0,
                'notes': ''}
    if not users_sleep_data.get(f'{message.chat.id}', None):
        users_sleep_data[f'{message.chat.id}'] = {today: [new_note]}
    else:
        users_sleep_data[f'{message.chat.id}'].get(today, []).append(new_note)
    user_sleep_status[f'{message.chat.id}'] = [False, today]
    bot.send_message(message.chat.id, f'Вы проспали {users_sleep_data[f"{message.chat.id}"][today][-1]["duration"]}\n'
                                      f'Используйте команды "/quality" и "/notes" для оценки качества сна и заметок')
    write_date()


@bot.message_handler(commands=["quality"])
def quality(message):
    try:
        users_sleep_data[f'{message.chat.id}'][get_date()][-1]["quality"] = message.text.split()[1]
        bot.send_message(message.chat.id, f'Оценка сохранена')
        write_date()
    except IndexError:
        bot.send_message(message.chat.id, f'Некорректный ввод данных.')
    except KeyError:
        bot.send_message(message.chat.id, f'Сессия не найдена.')


@bot.message_handler(commands=["notes"])
def notes(message):
    try:
        users_sleep_data[f'{message.chat.id}'][get_date()][-1]["notes"] = f'{" ".join(message.text.split()[1:])}'
        bot.send_message(message.chat.id, f'Заметка сохранена')
        write_date()
    except KeyError:
        bot.send_message(message.chat.id, f'Сессия не найдена.')


@bot.message_handler(commands=["info"])
def info(message):
    try:
        for day in users_sleep_data[f'{message.chat.id}']:
            bot.send_message(message.chat.id, f'Данные за {day}')
            for i, date in enumerate(users_sleep_data[f'{message.chat.id}'][day]):
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
        bot.send_message(message.chat.id, f'{user_sleep_status}')
    if user_choice == 'Запись':
        write_date()
        bot.send_message(message.chat.id, f'Данные записаны')'''

bot.polling(none_stop=True, interval=0)
