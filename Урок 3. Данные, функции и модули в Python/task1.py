
"""
Задайте список из нескольких чисел.
Напишите программу,
которая найдёт сумму элементов списка,
    стоящих на нечётной позиции.

Пример:

- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

 """

# from my_python_defs import *


# list_the = input_list_v1(5)
list_the = [2, 3, 5, 9, 3]
list_final = []

for i in range(len(list_the)):
    # print(i, list_final)
    if (i % 2) != 0:
        list_final.append(list_the[i])

print(f'orig = {list_the}')
print(f'final = {list_final}')

summ_final = 0

for i in range(len(list_final)):
    summ_final = summ_final + list_final[i]

print(f'summ_final = {summ_final}')
