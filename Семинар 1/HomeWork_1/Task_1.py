
# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

weekday = int(input("Input day of a week number: "))

if 0 < weekday < 6:
    print("The day is not weekend")
elif 5 < weekday < 8:
    print("The day is weekend")
else:
    print("Incorrect input!")

# проверка связи во воторой раз