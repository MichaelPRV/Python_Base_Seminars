
# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.

n = int(input("Input number N: "))

product_list = []
product_num = int(1)

if n > 1:
    for i in range(1, n + 1):
        product_num *= i
        product_list.append(product_num)
    print(product_list)
else:
    print("Input N > 1")
