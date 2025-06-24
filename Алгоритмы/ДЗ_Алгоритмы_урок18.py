def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            not_sorted_element = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > not_sorted_element:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                j -= 1
    return arr


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print("Отсортированный список:", my_list)
