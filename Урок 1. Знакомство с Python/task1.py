
""" Напишите программу, которая 
принимает на вход цифру, обозначающую день недели, и 
проверяет, 
является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет """


print("Enter 'day_of_week' please")
day_of_week = int(input())


if day_of_week == 6 or day_of_week == 7:
    print("да")
else:
    print("нет")
