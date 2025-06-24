import json

'''
# ПРЕОБРАЗОВАНИЕ PYTHON В JSON

# Объект Python
person = {
    "имя": "Анна",
    "возраст": 25,
    "город": "Москва",
    "знания": ["Python", "JavaScript", "SQL"]
}

# Преобразование в JSON
json_data = json.dumps(person)
print(json_data)'''


'''
# ПРЕОБРАЗОВАНИЕ PYTHON JSON В PYTHON

# JSON строка
json_string = '''
{
  "имя": "Анна",
  "возраст": 25,
  "город": "Москва",
  "знания": ["Python", "JavaScript", "SQL"]
}
'''

# Чтение JSON и преобразование в объект Python
data = json.loads(json_string)
print(data["имя"])
print(data["возраст"])'''

'''# ЧТЕНИЕ ИЗ ФАЙЛА

# Открываем файл с данными JSON для чтения
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


# Выводим данные
print(data["имя"])
print(data["возраст"])
print(data["город"])
print(data["знания"])'''

'''#Запись данных в JSON файл:

# Создаем данные для записи в формате словаря Python
person = {
    "имя": "Анна",
    "возраст": 25,
    "город": "Москва",
    "знания": ["Python", "JavaScript", "SQL"]
}

# Записываем данные в файл JSON
with open('новые_данные.json', 'w') as file:
    json.dump(person, file)'''


