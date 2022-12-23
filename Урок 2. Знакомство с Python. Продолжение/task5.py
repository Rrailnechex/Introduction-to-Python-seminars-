

"""
Реализуйте алгоритм перемешивания списка.
 """

import random
from pprint import *


def create_list12345(length, target_list):
    for i in range(length):
        target_list.append(i)
    return target_list


def unsort_list(target_l, help_l):
    steps = 999
    for i in range(steps):
        a = round(random.random()*(target_l-1))
        b = round(random.random()*(target_l-1))
        (help_l[a], help_l[b]) = (help_l[b], help_l[a])
    return help_l


the_l = int(input("Enter 'List length' = "))
a_l = []

print(create_list12345(the_l, a_l))
print(unsort_list(the_l, a_l))
