
# 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).

n = int(input("Input number N: "))
pos_1 = int(input("Input position of the first element: "))
pos_2 = int(input("Input position of second element: "))

if pos_1 > n * 2 + 1 or pos_2 > n * 2 + 1:
    print("There are no such positions in the list")

elif pos_1 < 1 or pos_2 < 1:
    print("Incorrect input (input position > 0)")

else:
    elements = []

    for i in range(-n, n + 1):
        elements.append(i)

    print(elements)

    product = elements[pos_1 - 1] * elements[pos_2 - 1]
    print(product)
