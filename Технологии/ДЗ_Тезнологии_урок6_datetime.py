import datetime


now = datetime.datetime.now()
print(now)
print(now.strftime("%A"))
year = now.year
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('Этот год является високосным.')
else:
    print('Год не високосный.')


try:
    y, m, d = map(int, input('Введите дату в формате Г М Д через пробел').split())
    try:
        date = datetime.date(y, m, d)
        date = datetime.datetime.combine(date, datetime.time())
        time_delta = date - now
        days = time_delta.days
        hours = time_delta.seconds // 3600
        minutes = time_delta.seconds % 3600 // 60
        if time_delta.days < 0:
            message = 'С указанной даты прошло:'
        else:
            message = 'До указанной даты осталось:'

        print(f'{message} {days} дней, {hours} часов, {minutes} минут.')
    except ValueError:
        print('Неверный формат даты.')
except ValueError:
    print('Неверные данные, рассчет невозможен.')

