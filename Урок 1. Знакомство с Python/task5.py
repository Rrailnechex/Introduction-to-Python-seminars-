

""" 
Напишите программу, которая 
принимает на вход координаты двух точек и 
находит расстояние между ними в 2D пространстве.

Пример:

- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21
 """


import math


print("Enter coordinates of first point please")
print("Enter 'x' please")
x1 = int(input())
print("Enter 'y' please")
y1 = int(input())

print("Enter coordinates of second point please")
print("Enter 'x' please")
x2 = int(input())
print("Enter 'y' please")
y2 = int(input())


def Get_2d_distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist


print(f"Distance is {Get_2d_distance(x1, y1, x2, y2)}")
