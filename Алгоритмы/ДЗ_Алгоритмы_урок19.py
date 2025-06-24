def selection_sort(arr):
    for i in range(len(arr)-1):
        min_element = (float('inf'), None)
        for j in range(i+1, len(arr)):
            if arr[j] < min_element[0]:
                min_element = (arr[j], j)
        if min_element[0] < arr[i]:
            arr[i], arr[min_element[1]] = arr[min_element[1]], arr[i]
    return arr


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Отсортированный список:", my_list)