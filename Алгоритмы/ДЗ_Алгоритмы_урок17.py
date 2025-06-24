def bubble_sort(arr):
    n = 0
    while n < (len(arr) - 1):
        for i in range(len(arr) - 1 - n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
    return arr


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 10]
bubble_sort(my_list)
print("Отсортированный список:", my_list)
