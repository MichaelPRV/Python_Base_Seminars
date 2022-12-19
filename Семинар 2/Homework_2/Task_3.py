
# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input("Input quantity of numbers: "))
numbers = []
sum_of_nums = 0

for i in range(1, n + 1):
    i = round((1 + 1 / i) ** i, 3)
    numbers.append(i)
    sum_of_nums += i

print(numbers)
print(sum_of_nums)
