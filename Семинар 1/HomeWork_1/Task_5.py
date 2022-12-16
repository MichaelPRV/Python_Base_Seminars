
# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

xa = float(input("Input point A x-coordinate: "))
ya = float(input("Input point A y-coordinate: "))
xb = float(input("Input point B x-coordinate: "))
yb = float(input("Input point B y-coordinate: "))

distance = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
distance = round(distance, 3)

print("Distance between the points is ", distance)
