
# 5. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

my_list = list(range(10))
print(my_list)

import random

for i in range(5):

    n = random.randint(0, 9)
    m = random.randint(0, 9)

    temp = my_list[n]
    my_list[n] = my_list[m]
    my_list[m] = temp

print(my_list)