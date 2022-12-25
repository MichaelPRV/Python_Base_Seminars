
# 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import random

def create_random_list(length):
    new_list = []
    for i in range(length):
        element = random.uniform(0, 100)
        new_list.append(round(element, 2))
    return new_list

def dif_min_max_fractional(numbers):

    min = numbers[0] - int(numbers[0])
    max = numbers[0] - int(numbers[0])

    for i in range(1, len(numbers)):
        if numbers[i] - int(numbers[i]) < min:
            min = numbers[i] - int(numbers[i])
        elif numbers[i] - int(numbers[i]) > max:
            max = numbers[i] - int(numbers[i])
    
    min = round(min, 2)
    max = round(max, 2)
    dif = round(max - min, 2)
    return min, max, dif


quant_of_nums = int(input("Input quantity of numbers in the list: "))

if quant_of_nums > 1:
    my_list = create_random_list(quant_of_nums)
    print(my_list)
    results = dif_min_max_fractional(my_list)
    print("Min: ", results[0], "; Max: ", results[1], "; Difference: ", results[2])
else:
    print("Input correct quantity")
