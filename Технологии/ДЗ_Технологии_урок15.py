students_dict = {
 'Саша': 27,
 'Кирилл': 52,
 'Маша': 14,
 'Петя': 36,
 'Оля': 43,
}
print(dict(sorted(students_dict.items(), key=lambda x: x[1])))

data = [
    (82, 191),
    (68, 174),
    (90, 189),
    (73, 179),
    (76, 184)
]
print(list(sorted(data, key=lambda x: x[0] / (x[1]/100)**2)))

students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36,
    },
    {
        "name": "Оля",
        "age": 43,
    },
]
print(list(sorted(students_list, key=lambda x: x['age']))[0])