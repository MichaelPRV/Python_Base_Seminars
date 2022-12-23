
# Задача 1. Наапишите программу, которая принимает на вход число N и выдает последовательность из N членов.
# Пример: N = 5, то 1, -3, 9, -27, 81

# n = int(input("Input number N: "))

# for i in range(n):
#     print((-3) ** i, end = " ")



# # Задача 2. Создать список, длины n, значения формируются по формуле 3k + 1,
# # где k принимает значения от 1 до n включительно.

# n = int(input("Input number N: "))

# num_list = []

# for k in range(1, n + 1):
#     num_list.append(3 * k + 1)

# print(num_list)



# Задача 3. Напишите программу, в которой пользователь будет задавать две строки,
# программа - определять количество вхождений одной строки в другой.

user_str_input = input("Input first string: ")
user_str_find = input("Input what should find: ")

print(user_str_input.count(user_str_find))
