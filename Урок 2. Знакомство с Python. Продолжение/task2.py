"""
Напишите программу, которая
принимает на вход число N и
выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
 """

the_n = int(input("Enter 'n' = "))

print(f'Пусть N = {the_n}, тогда [', end='')


def solve_and_print_progression(the_n):
    count = 1
    for i in range(1, the_n):
        count = count * i
        print(count, end=', ')
    print(f'{count * (i+1)}]')


solve_and_print_progression(the_n)
