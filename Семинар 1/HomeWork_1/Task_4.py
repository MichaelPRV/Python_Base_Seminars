
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input("Input quarter number: "))

if quarter == 1:
    print("Points in the quarter will have the following coordinates: x > 0, y > 0")
elif quarter == 2:
    print("Points in the quarter will have the following coordinates: x < 0, y > 0")
elif quarter == 3:
    print("Points in the quarter will have the following coordinates: x < 0, y < 0")
elif quarter == 4:
    print("Points in the quarter will have the following coordinates: x > 0, y < 0")
else:
    print("Input correct number of quarter")
