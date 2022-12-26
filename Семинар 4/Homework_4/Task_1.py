
# 1. Вычислить число c заданной точностью d

from decimal import Decimal

num = Decimal(input("Input number: "))
d = Decimal(input("Input accuracy: "))

num_rounded = num.quantize(d)
print(num_rounded)
