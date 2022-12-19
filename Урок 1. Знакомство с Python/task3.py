

""" Напишите программу, которая
принимает на вход координаты точки (X и Y),
    причём X ≠ 0 и Y ≠ 0 и
выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

Пример:

- x=34; y=-30 -> 4
- x=2; y=4-> 1
- x=-34; y=-30 -> 3 """


print("Enter 'x' please")
x = int(input())
print("Enter 'y' please")
y = int(input())


def Print_quater(x, y):
    if x > 0 and y > 0:
        print("point in 1st quater")
    elif x < 0 and y > 0:
        print("point in 2nd quater")
    elif x < 0 and y < 0:
        print("point in 3rd quater")
    elif x > 0 and y < 0:
        print("point in 4th quater")


def Print_axis(x, y):
    if x == 0 and y > 0:
        print("point at y+ axis")
    elif x == 0 and y < 0:
        print("point at y- axis")
    elif x > 0 and y == 0:
        print("point at x+ axis")
    elif x < 0 and y == 0:
        print("point at x- axis")


if x == 0 and y == 0:
    print("point at the center")
elif x != 0 and y != 0:
    print("hell yeah!!!")
    Print_quater(x, y)
elif x == 0 or y == 0:
    print("lets go!!!")
    Print_axis(x, y)
