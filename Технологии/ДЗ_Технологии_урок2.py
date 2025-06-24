import csv
import random


with open('AppleStore.csv', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in list(reader)[:10]:
        print(row)


with open('AppleStore.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    print(list(reader)[:10])

# Запись данных в файл
data = [
    ['Имя', 'Возраст', 'Город'],
    ['Анна', '25', 'Москва'],
    ['Петр', '30', 'Санкт-Петербург'],
    ['Мария', '28', 'Киев']
]

# Открываем файл для записи
with open('новые_данные.csv', 'w', encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)  # Записываем данные в файл


with open('новые_данные.csv', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)




# Запись данных через словари
data = [
    {'Имя': 'Анна', 'Возраст': '25', 'Город': 'Москва'},
    {'Имя': 'Петр', 'Возраст': '30', 'Город': 'Санкт-Петербург'},
    {'Имя': 'Мария', 'Возраст': '28', 'Город': 'Киев'}
]

# Записываем данные в CSV файл с использованием словаря
with open('данные_с_заголовками.csv', 'w', encoding="utf-8") as csvfile:
    fieldnames = ['Имя', 'Возраст', 'Город']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()  # Записываем заголовки
    writer.writerows(data)  # Записываем данные

# Чтение данных из CSV файла с использованием словаря
with open('данные_с_заголовками.csv', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Имя'], row['Возраст'], row['Город'])

'''with open('file.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        print(row)'''


#Задание №1

# создание текстового файла с товарами
with open('prices.txt', 'w', encoding="utf-8") as t_file:
    for i in range(20):
        # Случайное количество товара (от 1 до 10)
        quantity = random.randint(1, 10)
        # Случайная цена за единицу товара (от 10 до 100)
        price = random.randint(10, 100)
        # Запись в файл
        t_file.write(f"Продукт_{i+1}\t{quantity}\t{price}\n")

#Считывание содержимого в переменную t_price
with open('prices.txt', encoding='utf-8') as tf:
    reader = tf.readlines()
    t_price_list = [[i.replace('\n', '')] for i in reader]



with open('prices.csv', 'w', encoding="utf-8", newline='') as c_file:
    writer = csv.writer(c_file)
    writer.writerows(t_price_list)



#Задание №2

with open('prices.csv', encoding="utf-8") as cf:
    reader = csv.reader(cf, delimiter='\t')
    cf_list = list(reader)
print(f'Сумма всех покупок = {sum(int(e[2]) for e in cf_list)}')

