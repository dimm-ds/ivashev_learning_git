import itertools

# Задача 1: Комбинации чисел из списка
# Дан список чисел [1, 2, 3, 4]. Используя модуль itertools,
# создайте все возможные комбинации чисел длиной 2 и выведите их.


for i in itertools.combinations([1, 2, 3, 4], 2):
    print(i)

# Задача 2: Перебор перестановок букв в слове
# Для слова 'Python' найдите все возможные перестановки букв. Выведите каждую перестановку на отдельной строке.

for i in itertools.permutations(list('Python')):
    print(i)

# Задача 3: Объединение списков в цикле
# Даны три списка: ['a', 'b'], [1, 2, 3], ['x', 'y']. Используя itertools.cycle, объедините их в один список в цикле,
# повторяя этот цикл 5 раз.

a, b, c = ['a', 'b'], [1, 2, 3], ['x', 'y']
iterator_len = len(a) + len(b) + len(c)
iterator = itertools.chain(a, b, c)
count = 0
for w in itertools.cycle(iterator):
    count += 1
    if count == iterator_len * 5:
        break


# Задача 4: Генерация бесконечной последовательности чисел
# Создайте бесконечный генератор, который будет возвращать последовательность чисел Фибоначчи.
# Выведите первые 10 чисел Фибоначчи.


def fib():
    f, s = 0, 1
    while True:
        yield f
        f, s = s, f + s


for e in itertools.islice(fib(), 10):
    print(e)

# Задача 5: Составление всех возможных комбинаций слов
# Используя itertools.product, создайте все возможные комбинации слов из двух списков:
# ['red', 'blue'] и ['shirt', 'shoes']. Выведите каждую комбинацию на отдельной строке.

for r in itertools.product(['red', 'blue'], ['shirt', 'shoes']):
    print(r)
