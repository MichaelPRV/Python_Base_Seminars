
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Без работы с методами строк.

n = float(input("Input real number: "))

while n > (n // 10) * 10:
    n *= 10

n = int(n)
sum_of_digits = int(0)

while n > 0:
    sum_of_digits += n % 10
    n = n // 10
    
sum_of_digits += n
    
print(sum_of_digits)
