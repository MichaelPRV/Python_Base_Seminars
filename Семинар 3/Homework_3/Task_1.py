
# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def create_random_list(length):
    new_list = sample(range(1, length * 5), k=length)
    return new_list

def sum_odd_pos_elements(elements):
    sum = int(0)
    for i in list(range(0, len(elements), 2)):
        sum += elements[i]
    return sum

nums_quant = int(input("Input quantity of numbers in the list: "))

if nums_quant > 0:
    my_list = create_random_list(nums_quant)
    print(my_list)
    odd_pos_sum = sum_odd_pos_elements(my_list)
    print("Sum of elements on odd positions is ", odd_pos_sum)
else:
    print("Input correct number of elements")
