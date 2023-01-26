# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. Use comprehension.

def create_random_list(length):
    from random import sample
    new_list = sample(range(1, length * 5), k=length)
    return new_list


n = int(input("Input quantity of numbers: "))

array = create_random_list(n)
increasing_nums = [array[i] for i in range(1, len(array)) if array[i] > array[i - 1]]
print(array)
print(increasing_nums)
