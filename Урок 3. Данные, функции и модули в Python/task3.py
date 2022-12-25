
""" 
Задайте список из вещественных чисел. 
Напишите программу, 
которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
 """

import math

list_original = [1.1, 1.2, 3.1, 5, 10.01]
list_final = []

list_final = list(map(lambda x: (x - int(x)), list_original))
difference = round((abs(min(list_final) - max(list_final))), 2)

print(f"{list_original} => {difference}")
