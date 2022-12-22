
# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import sample

def create_random_list(length):
    new_list = sample(range(1, length * 2), k=length)
    return new_list

def nums_pairs_prod(numbers):

    pairs_products = []

    if len(numbers) % 2 == 0:
        for i in range(int(len(numbers) / 2)):
            product = numbers[i] * numbers[len(numbers) - 1 - i]
            pairs_products.append(product)
    else:
        for i in range(int(len(numbers) / 2 - 0.5)):
            product = numbers[i] * numbers[len(numbers) - 1 - i]
            pairs_products.append(product)
        pairs_products.append(numbers[int(len(numbers) / 2 - 0.5)])

    return pairs_products


list_length = int(input("Input quantity of elements in the list: "))

my_list = create_random_list(list_length)
print(my_list)
pairs_products_list = nums_pairs_prod(my_list)
print(pairs_products_list)
