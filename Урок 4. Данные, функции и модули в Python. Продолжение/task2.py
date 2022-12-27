
"""
Задайте натуральное число N.
Напишите программу,
которая составит
    список простых множителей числа N.
 """

from math import trunc


def combinedT_or_simpleF_number_it_is(n):
    i = 2
    j = 0

    # плиск написан блок схеме с википедии [https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D0%B1%D0%BE%D1%80_%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D0%B5%D0%B9]
    while i*i <= n and j != 1:
        # print(f"n = {n}; i - {i}; j = {j}")
        j = 1 if n % i == 0 else j
        i += 1

    return True if j == 1 else False


def breack_down(the_n):

    working_n = the_n
    print(f"{working_n}")

    for i in range(9999):
        # остонавливаемся если число неделимое
        if combinedT_or_simpleF_number_it_is(working_n) == False:
            return working_n
        # делим число
        else:
            # ищем минимальный делитель без остатка
            x = 2
            while working_n / x != trunc(working_n / x):
                x += 1
            # если мин делитель == числу то выходим
            if working_n == x:
                return working_n
            # делим число и повторяем цикл

            working_n /= x
            print(f"{i}; {working_n} | {x}")

    # return working_n


breack_down(84)
