
"""
Напишите программу, которая
найдёт произведение пар чисел списка.
Парой считаем первый и последний элемент,
второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
 """

list_original = [2, 3, 4, 5, 6]
# list_original = [2, 3, 5, 6]
list_final = []

for i in range(len(list_original)):
    if i < len(list_original) / 2:
        list_final.append(list_original[i] * list_original[-i-1])
        # print(i, list_final, list_original[i], '*', list_original[-i-1])

print(f"{list_original} => {list_final}")
