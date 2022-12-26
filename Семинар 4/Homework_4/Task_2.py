
# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def find_deviders(n: int):

    deviders = []

    for i in range(2, n + 1):
        while n % i <= 0:
            deviders.append(i)
            n /= i         

    return deviders


num = int(input("Input number: "))

print(f"Prime factors of {num} is: ")
print(find_deviders(num))