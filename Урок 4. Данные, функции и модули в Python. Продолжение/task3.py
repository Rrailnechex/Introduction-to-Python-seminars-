
""" 
Задайте последовательность чисел. 
Напишите программу, которая 
выведет список 
    неповторяющихся элементов исходной последовательности.
 """


""" def create_list_of_unique_values_from(inp_l):

    # i = 0
    # j = 0

    # итерации по каждому обьекту
    for i in range(len(inp_l)):
        originality_of_i = False
        # i += 1
        #print("i =", i)

        # проверка на оригинальность сравнением
        for j in range(len(inp_l)):
            # j += 1
            # print("j =", j)
            originality_of_i = False if inp_l[i] == inp_l[j] else True

        # удаляем если не оригинален
        if originality_of_i == False:
            del inp_l[0]
        print(inp_l)
    return inp_l """


""" def check_number_for_originality(l, n):
    originality_of_i = False

    # проверка на оригинальность сравнением
    for i in range(len(l)):
        originality_of_i = originality_of_i if n == l[i] else True

    return originality_of_i """


""" from random import randint
from pprint import pprint
the_list = []


for i in range(60):
    the_list.append(randint(0, 10))


the_list.sort()

new_list = []
while len(the_list) != 0:
    temp = the_list[0]
    new_list.append(the_list[0])
    the_list.pop(0)


print(the_list)
print("---")
# print(create_list_of_unique_values_from(the_list))

print(new_list) """


from random import randint
the_list = []
for i in range(60):
    the_list.append(randint(0, 10))

print(the_list)
print(list(dict.fromkeys(the_list)))
