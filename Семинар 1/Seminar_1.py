
# Задача 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# n = int(input("input number N: "))
# m = int(input("input number M: "))

# if n == m ** 2 or m == n ** 2:
#     print("Yes")
# else:
#     print("No")



# Задача 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# num_max = 0

# for i in range (5):
#     n = int(input("Input number: "))
#     if n > num_max:
#         num_max = n

# print("Maximal number is ", num_max)



# Задача 3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

# n = int(input("Input number N: "))

# if n >= 0:
#     print(*range(-n, n + 1))
# else:
#     print(*range(-n, n - 1, -1))

# print(list(range(-n, n+1)))

# for i in range(-n, n + 1):
#     print(i)



# Задача 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# n = float(input("Input number: "))

# n_fractional = int(n * 10 % 10)

# print(n_fractional)



# Задача 5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# n = int(input("Input number: "))

# if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
#     print("Yes")
# else:
#     print("No")

# print((n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0)



# 6. Пример проверки ложности утверждения (x ≡ z ) ∨ (x → (y ∧ z))

# print("x y z")

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not (x == z or x <= y and z):
#                 print(x, y, z)


# Возведение в степень (опеделение корня)

n = float(input("Input number N: "))

from math import sqrt
print(sqrt(n))
# второй вариант:
n_sqrt = f"{n ** 0.5: .3f}"    #  форматирование результата вычислений
# или
n_sqrt = round(n ** 0.5, 3)

print(n_sqrt)
