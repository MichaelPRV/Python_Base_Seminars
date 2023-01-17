
# 2. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность.
# Порядок элементов менять нельзя.

from random import choices

def create_array():
    n = int(input("Input array length: "))
    array = choices(range(n * 2), k=n)
    return array

def sort_list(array):
    sort_array = []
    for i in range(len(array)):
        temp = array[i]
        new_list = [temp]
        for j in range(i + 1, len(array)):
            if array[j] > temp:
                temp = array[j]
                new_list.append(temp)
        if len(new_list) > 1:
            sort_array.append(new_list)
    return sort_array


my_list = create_array()
print(my_list)
print(sort_list(my_list))
