import collections
import random


#Задание 1: Анализ списка чисел с помощью Counter
#Сгенерируйте случайный список чисел.
#Используйте Counter, чтобы подсчитать количество уникальных элементов в списке.
#Найдите три наиболее часто встречающихся элемента в списке и выведите их с количеством вхождений.

random_list = [random.randint(1, 100) for i in range(100)]
print(collections.Counter(random_list).most_common(3))



#Задание 2: Работа с именованными кортежами
#Создайте именованный кортеж Book с полями title, author, genre.
#Создайте несколько экземпляров Book.
#Выведите информацию о книгах, используя атрибуты именованных кортежей.

Book = collections.namedtuple('Book', ['title', 'author', 'genre'])
book1 = Book("Преступление и наказание", "Фёдор Достоевский", "Классическая литература")
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", "Роман-фэнтези")
book3 = Book("Война и мир", "Лев Толстой", "Исторический роман")

book_list = [book1, book2, book3]
for e in book_list:
    print(f'Книга с названием "{e.title}", автор - {e.author} относится к жанру "{e.genre}".')

#Задание 3: Работа с defaultdict
#Создайте defaultdict с типом данных list.
#Добавьте несколько элементов в словарь, используя ключи и значения.
#Выведите содержимое словаря, где значения - это списки элементов с одинаковыми ключами.

dct = collections.defaultdict(list)
dct['a'].append('яблоко')
dct['b'].append('банан')
dct['c'].append('виноград')
dct['a'].append('абрикос')
dct['b'].append('бергамот')

print(dct)

#Задание 4: Использование deque для обработки данных
#Создайте deque и добавьте в него элементы.
#Используйте методы append, appendleft, pop и popleft для добавления и удаления элементов из deque.
#Проверьте, как изменяется deque после каждой операции.

deque = collections.deque([1, 2, 3])

deque.append('e1')
print(deque)
deque.appendleft('e2')
print(deque)
deque.pop()
print(deque)
deque.popleft()
print(deque)
print('_____________________________________')

#Задание 5: Реализация простой очереди с помощью deque
#Напишите функции для добавления и извлечения элементов из deque.
#Создайте пустой deque.
#Используйте написанные функции для добавления и извлечения элементов из очереди.

def add_element(queue, element):
    queue.append(element)
    return queue

def pop_element(queue):
    try:
        queue.popleft()
    except IndexError:
        print('Очередь пуста')
    return queue

queue = collections.deque([])

print(add_element(queue, 1))
print(add_element(queue, 2))
print(add_element(queue, 3))
print(pop_element(queue))
print(pop_element(queue))
print(pop_element(queue))
print(pop_element(queue))



