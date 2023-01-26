# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

n = int(input("Input number N: "))

array = [num for num in range(20, n + 1) if not num % 20 or not num % 21]

print(array)
