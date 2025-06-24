# Создайте базу данных с именем library.db.
# Создайте таблицу books со следующими полями:
# id (INTEGER, PRIMARY KEY, AUTOINCREMENT)
# title (TEXT, не может быть пустым)
# author (TEXT, не может быть пустым)
# year (INTEGER, может быть пустым)
# Реализуйте функции для выполнения следующих операций:
# Добавление новой книги: Функция должна принимать название книги, автора и год издания и добавлять новую запись в таблицу books.
# Получение всех книг: Функция должна возвращать список всех книг, хранящихся в базе данных.
# Обновление информации о книге: Функция должна принимать идентификатор книги и новые данные (название, автора, год издания)
# и обновлять соответствующую запись в таблице.
# Напишите тестовый код, который демонстрирует работу всех функций.

from sqlite3 import connect


def great_table(cursor):
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER DEFAULT NULL
        );
        """
    )


def add_book(cursor, title: str, author: str, year: int | None = None):
    answer = great_query('find', title, author, year)
    if len(answer) > 0:
        print('Книга уже внесена в реестр')
        return
    cursor.execute(
        """
        INSERT INTO books (title, author, year) 
        VALUES (?, ?, ?);
        """,
        (title, author, year)
    )


def find_book(cursor, title: str, author: str, year: int | None = None):
    result = cursor.execute(
        '''
        SELECT id FROM books
        WHERE title=? AND author=? AND (year=? OR year ISNULL)
        ''',
        (title, author, year)
    )
    return result.fetchall()


def change_info(cursor, row_id: int, title: str, author: str, year: int | None = None):
    cursor.execute(
        '''
        UPDATE books
        SET title=?, author=?, year=?
        WHERE id=?
        ''',
        (title, author, year, row_id)
    )


def get_info(cursor):
    print(
        *cursor.execute(
            """SELECT * FROM books;"""
        ).fetchall(), sep='\n'
    )


def great_query(action: str, *args, **kwargs):
    action_dict = {
        'great': great_table,
        'add': add_book,
        'find': find_book,
        'change': change_info,
        'info': get_info
    }
    conn = connect("library.db")
    cursor = conn.cursor()

    result = action_dict[action](cursor, *args, **kwargs)

    conn.commit()
    cursor.close()
    return result


great_query('great')

great_query('add', "Преступление и наказание", "Фёдор Достоевский", 1866)
great_query('add', "Война и мир", "Лев Толстой", 1869)
great_query('add', "Мастер и Маргарита", "Михаил Булгаков", 1967)
great_query('add', "Евгений Онегин", "Александр Пушкин")
great_query('add', "Идиот", "Фёдор Достоевский", 1868)
great_query('add', "Мёртвые души", "Николай Гоголь", 1842)
great_query('add', "Анна Каренина", "Лев Толстой")
great_query('add', "Доктор Живаго", "Борис Пастернак", 1957)
great_query('add', "Три товарища", "Эрих Мария Ремарк")
great_query('info')

great_query('change', 9, "Маленький принц", "Антуан де Сент-Экзюпери")
great_query('info')
