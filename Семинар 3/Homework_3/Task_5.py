
# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def nega_fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        return nega_fib(n - 2) - nega_fib(n - 1)


def create_fib_range(n):
    fib_list = []
    for i in range(1, n + 1):
        fib_list.append(fib(i))
    return fib_list


def create_negafib_range(n):
    negafib_list = []
    for i in range(1, n + 1):
        negafib_list.append(nega_fib(i))
    return negafib_list


num = int(input("Input number of elements in range: "))

fib_range = create_fib_range(num)
nega_fib_range = create_negafib_range(num)
nega_fib_range.reverse()

general_range = [*nega_fib_range, 0, *fib_range]
print(general_range)
