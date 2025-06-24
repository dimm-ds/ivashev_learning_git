#Задание 1:
#Работа с JSON файлом
#Задача:
#Прочитать данные из файла students.json.
#Определить общее количество студентов в файле.
#Найти студента с самым высоким возрастом и вывести его данные (имя, возраст, город).
#Определить количество студентов, изучающих определенный предмет (например, Python)
import csv
import json
import statistics

with open('students.json', encoding='utf-8') as f:
    data = json.load(f)

print(f'Общее количество студентов - {len(data)}')
print()
print('Самый старший студент:')
sorted_data = sorted(data, key=lambda item: item['возраст'], reverse=True)
print(f'Имя -{sorted_data[0]["имя"]}, возраст - {sorted_data[0]["возраст"]}, город - {sorted_data[0]["город"]}.')
print()
sum_student = 0
discipline = input('Введите название предмета("Python", "JavaScript", "Java", "SQL")')
for e in data:
    if discipline in e["предметы"]:
        sum_student += 1
if sum_student > 0:
    print(f'Предмет {discipline} изуча{["е", "ю"][sum_student!=1]}т {sum_student} студент{["", "а", "ов"][(sum_student > 1) + (sum_student > 4)]}.')
else:
    print(f'Студентов изучающих {discipline} не найдено.')
print('_________________________________________________________')


#Задание 2:
#Работа с CSV файлом
#Задача:
#Считать данные из файла sales.csv.
#Подсчитать общую сумму продаж за весь период.
#Определить продукт с самым высоким объемом продаж и вывести его на экран.
#Разделить данные на категории по месяцам и вывести общую сумму продаж для каждого месяца.

with open('sales.csv', encoding='utf-8') as f1:
    reader = csv.DictReader(f1, skipinitialspace=True)
    data = list(reader)
sum_sales = 0
for e in data:
    sum_sales += int(e['Сумма'])
print(f'Общая сумма продаж - {sum_sales}.')

new_dict = {}
for e in data:
    new_dict[e['Продукт']] = new_dict.get(e['Продукт'], 0) + int(e['Сумма'])
new_dict = dict(sorted(new_dict.items(), key=lambda item: item[1], reverse=True))
print(f'Продукт с самыми высокими продажами за весь период - {list(new_dict.keys())[0]}')
print()

print('Реализация товаров по месяцам:')
new_dict = {}
for e in data:
    new_dict[e['Дата'][:7]] = new_dict.get(e['Дата'][:7], 0) + int(e['Сумма'])
new_dict = dict(sorted(new_dict.items(), key=lambda item: item[1], reverse=True))
for e in new_dict.items():
    print(f'Продано {e[0]} на общую сумму {e[1]}.')
print('_________________________________________________________')



#Задание 3:
#Комбинированная работа с JSON и CSV
#Задача:
#Считать данные из файлов employees.json и performance.csv.
#Сопоставить данные о производительности каждого сотрудника с их соответствующей информацией из JSON файла.
#Определить среднюю производительность среди всех сотрудников и вывести ее.
#Найти сотрудника с наивысшей производительностью и вывести его имя и показатель производительности.

with open('employees.json', encoding='utf-8') as f2:
    js_data = sorted(json.load(f2), key=lambda x: x['id'])

with open('performance.csv', encoding='utf-8') as f3:
    reader = csv.DictReader(f3, skipinitialspace=True)
    cv_data = sorted(list(reader), key=lambda x: x['employee_id'])

new_data = []
for i in range(len(js_data)):
    cv_data[i].pop('employee_id')
    js_data[i].update(cv_data[i])
    new_data.append(js_data[i])


print(f'Средняя производительность всех сотрудников - {statistics.mean([int(i["performance"]) for i in new_data])}')
new_data = sorted(new_data, key=lambda x: x['performance'], reverse=True)
print(f'{new_data[0]["имя"]} является самым высокопроизводительным сотрудником с рейтингом {new_data[0]["performance"]}.')

