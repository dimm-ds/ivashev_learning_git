import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Создание таблицы
create_table_query = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE NOT NULL
)
'''
cursor.execute(create_table_query)
conn.commit()

# Вставка данных
insert_data_query = '''
INSERT INTO users (name, age, email) VALUES (?, ?, ?)
'''
users = [
    ('Alice', 25, 'alice@example.com'),
    ('Bob', 30, 'bob@example.com'),
    ('Charlie', 35, 'charlie@example.com')
]
cursor.executemany(insert_data_query, users)
conn.commit()

# Чтение данных
select_query = '''
SELECT * FROM users
'''
cursor.execute(select_query)
all_users = cursor.fetchall()
for user in all_users:
    print(user)

# Обновление данных
update_query = '''
UPDATE users
SET age = ?
WHERE name = ?
'''
cursor.execute(update_query, (28, 'Alice'))
conn.commit()

# Удаление данных
delete_query = '''
DELETE FROM users
WHERE name = ?
'''
cursor.execute(delete_query, ('Bob',))
conn.commit()

# Закрытие соединения
cursor.close()
conn.close()


from sqlite3 import connect

# Создаем соединение, передаем просто строку с названием файла,
# он будет создан - это и будет наша база данных
conn = connect("my_database_name")

# Создаем объект курсора, с его помощью можно исполнять SQL-запросы
cursor = conn.cursor()

# Создадим таблицу users с полями id, name, age
# Поле id будет первичным ключом, и при каждой записи оно автоматически
# будет увеличиваться на 1 для следующей.
# Поле name - текстовое поле, age - числовое поле,
# причем age может быть пустым(если вдруг пользователь не захотел указывать возраст)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER DEFAULT NULL
    );
    """
)

# Добавим первого пользователя
cursor.execute(
    """
    INSERT INTO users (name, age) 
    VALUES (?, ?);
    """,
    ("Bob", 25) # Эти значения будут подставлены вместо символов ?
)

# Добавим второго пользователя без указания возраста
cursor.execute(
    """
    INSERT INTO users (name) 
    VALUES (?);
    """,
    ("Martin",)
)

conn.commit() # Зафиксируем наши изменения

# Получим список пользователей и распечатаем результат на экране
print(
    cursor.execute(
        """SELECT * FROM users;"""
    ).fetchall()
)
# Получим вот такой список [(1, 'Bob', 25), (2, 'Martin', None)]

# Закроем соединение и курсор после выполнения работы
cursor.close()
conn.close()