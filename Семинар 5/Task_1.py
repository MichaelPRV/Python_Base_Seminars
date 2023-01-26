
# 1. Создайте список из N натуральных чисел(0 до N),
# упорядоченных по возрастанию. Среди чисел не хватает
# одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

from random import choice

def create_list():
    n = int(input("Input number: "))
    lst = [i for i in range(n + 1)]
    lst.remove(choice(lst))

    return lst

def find_num(array):
    for i in range(1, len(array)):
        if array[i] - 1 != array[i - 1]:
            return array[i] - 1
    return -1

new_array = create_list()
print(new_array)
print(find_num(new_array))