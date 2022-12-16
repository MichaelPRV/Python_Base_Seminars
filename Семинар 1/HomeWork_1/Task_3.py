
# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x = int(input("Input X coordinate: "))
y = int(input("Input Y coordinate: "))

if x == 0 or y == 0:
    print("Input correct coordinates (X ≠ 0, Y ≠ 0)")
else:
    if x > 0 and y > 0:
        print("The point is located in the 1 quarter")
    elif x < 0 and y > 0:
        print("The point is located in the 2 quarter")
    elif x < 0 and y < 0:
        print("The point is located in the 3 quarter")
    else:
        print("The point is located in the 4 quarter")
