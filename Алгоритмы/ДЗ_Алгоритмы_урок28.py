# Алгоритм проверки наличия дубликатов в массиве.
def has_duplicates(arr):
    for i in range(len(arr)):#Линейная сложность, в худшем случае считает все элементы O(N)
        for j in range(i + 1, len(arr)): #Линейная сложность, в худшем лучае N/2 от входящих данных внешнего цикла. Сложность  O(N) - не учитываем константу
            if arr[i] == arr[j]:
                return True
    return False
'''Общая сложность алгоритма O(N^2)'''

# Алгоритм проверки наличия дубликатов в массиве.
def find_max(arr):
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val
'''O(N) алгоритм пройдет весь массив 1 раз'''

# Алгоритм сортировки выбором (Selection Sort).
def selection_sort(arr):
    for i in range(len(arr)):# Линейная сложность - 1 проход через весь массив O(N)
        min_idx = i
        for j in range(i + 1, len(arr)): #Линейная сложность, в худшем лучае N/2 от входящих данных внешнего цикла. Сложность O(N) - не учитываем константу
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

'''Общая сложность O(N^2)'''

# Алгоритм быстрой сортировки (Quick Sort).
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
'''В худдшем случае придется поменять все элементы разделенных массивов местами и потом объединить их меняя индексы в смежных вновь соединяемых массивах
Сложность O(N^2)
В среднем случае сложность O(nlogN) - данные из открытых источников, для самостоятельного обьяснения недостаточно математической базы'''


# Алгоритм вычисления n-го числа Фибоначчи (рекурсивно).
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

'''этот алгоритм имеет экспоненциальную сложность, ведь каждый новый вызов рекурсии будет увеличивать объем вычислений в 2е
2-4-8-16-32-..... O(2^N)'''
