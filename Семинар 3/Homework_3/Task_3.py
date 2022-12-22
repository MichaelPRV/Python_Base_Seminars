
# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

def decimal_to_binary(num):

    binar = []
    
    while num:
        binar_digit = num % 2
        binar.append(binar_digit)
        num //= 2

    bin_num = 0
    for i in range(len(binar)):
        bin_num += binar[i] * (10 ** i)   

    return bin_num


decimal = int(input("Input number: "))
binary = decimal_to_binary(decimal)
print("The result of decimal converting to binary is ", binary)
