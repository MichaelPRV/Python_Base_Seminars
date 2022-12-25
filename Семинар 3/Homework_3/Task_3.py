
# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

def decimal_to_binary(num):
    
    bin_num = 0
    count = 0

    while num:
        binar_digit = num % 2
        bin_num += binar_digit * (10 ** count)
        num //= 2
        count += 1  

    return bin_num


decimal = int(input("Input number: "))
binary = decimal_to_binary(decimal)
print("The result of decimal converting to binary is ", binary)
