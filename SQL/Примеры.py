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
# причем age может быть пустым(если вдруг пользовтаель не захотел указывать возраст)
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