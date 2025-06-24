import json
import csv

with open('student_list.json', encoding='utf-8') as file:
    students = json.load(file)


def get_sorted_dict(dct: dict, reverse: bool = False) -> dict:
    return dict(sorted(dct.items(), key=lambda x: x[1], reverse=reverse))


def get_average_score(dct: dict) -> dict:
    average_score_dict = {}
    for i in dct:
        scores = list(dct[i]['grades'].items())
        average_score_dict[i] = sum([x[1] for x in scores]) / len(scores)
    return average_score_dict


def get_best_student(dct: dict) -> str:
    best_student = max(get_average_score(dct).items(), key=lambda x: x[1])
    return f'Наилучший студент: {best_student[0]} (Средний балл: {best_student[1]})'


def get_worst_student(dct: dict) -> str:
    worst_student = min(get_average_score(dct).items(), key=lambda x: x[1])
    return f'Худший студент: {worst_student[0]} (Средний балл: {worst_student[1]})'


def find_student(name: str) -> str:
    if not students.get(name):
        return f'Студент с таким именем не найден'
    return f'Имя: {name}\n' \
           f'Возраст: {students[name]["age"]}\n' \
           f'Предметы: {students[name]["subjects"]}\n' \
           f'Оценки: {students[name]["grades"]}'


for item in get_average_score(students).items():
    print(f'Средний балл студента {item[0]}: {item[1]}')

print(get_best_student(students))
print(get_worst_student(students))
print(find_student('William'))

for item in get_sorted_dict(get_average_score(students), True).items():
    print(f'{item[0]}: {item[1]}')

students_list = [{'name': item[0],
                  'age': item[1]['age'],
                  'subjects': item[1]['subjects'],
                  'grades': item[1]['grades']} for item in students.items()]

students_list_1 = [{'name': item[0],
                    'age': item[1]['age'],
                    'grade': sum(map(lambda x: x[1], item[1]['grades'].items())) / len(item[1]['grades'])} for item in
                   students.items()]

print(students_list_1)
with open('student_list.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age', 'grade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(students_list_1)
