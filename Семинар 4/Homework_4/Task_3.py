
# 3. Задайте последовательность чисел. Напишите программу, которая выведет список 
#    неповторяющихся элементов исходной последовательности в том же порядке.

def user_input(num):
    
    new_list = []

    for i in range(num):
        new_list.append(input("Input element: "))

    return new_list


def show_not_repeat_elements(numbers: list):
    
    elements = numbers.copy()
    repeatable = []
    
    for i in range(len(elements)):
        for j in range(len(elements)):
            if i != j:
                if elements[i] == elements[j]:
                    repeatable.append(elements[i])

    for i in range(len(repeatable)):
        if repeatable[i] in elements:
            elements.remove(repeatable[i])
    
    return elements


n = abs(int(input("Input number of elements: ")))

my_list = user_input(n)
print(my_list)
nonrep_list = show_not_repeat_elements(my_list)
print(nonrep_list)
