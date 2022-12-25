
""" 
Задайте число. 
Составьте список чисел Фибоначчи, 
в том числе для отрицательных индексов.

Пример:

- для k = 8 список будет выглядеть так: 
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
 """


list_fib = []


def fibonnachi(k):
    a, b = 0, 1
    for i in range(k-1):
        b, a = a + b, b
        # print(f"i = {i}, fib bumber = {b}")

    b2, a2 = a, -b
    # print("a, b =", a, -b)

    for i in range(-k, k):
        b2, a2 = a2 + b2, b2
        list_fib.append(b2)
        # print(f"i = {i}, fib bumber = {b2}")


fibonnachi(8)  # что-то сложновато с отрицательных начать

print(list_fib)
