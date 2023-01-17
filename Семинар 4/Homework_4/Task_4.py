
# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (от 0 до 10) 
# многочлена, записать в файл полученный многочлен не менее 3-х раз.

import random

def polynomial(leng: int):

    coefficients = random.sample(range(0, 10), k=leng)
    polynomials = []
    signs = ['+', '-']

    for i in range(leng, -1, -1):
        if i > 0:
            if coefficients[i-1] == 0:
                polynomials.append(f'')
            else:
                polynomials.append(f'{coefficients[i-1]}*x^{i} {random.choice(signs)} ')
        else:
            polynomials.append(f'{coefficients[i-1]}')

    return polynomials


for i in range(3):

    k = int(input("Input degree k: "))
    my_list = polynomial(k)
    my_string = "".join(my_list)
    my_string = my_string + ' = 0'
    print(my_string)

    with open("polynomial.txt", "a", encoding="utf-8") as file_polynomial:
        file_polynomial.write(f"{my_string}\n")
