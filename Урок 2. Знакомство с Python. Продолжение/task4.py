
"""
Задайте список из N элементов,
заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в файле file.txt
    в одной строке одно число.

 """


num_len = int(input("Enter 'N' = "))
list_original = list(range(-num_len, num_len+1))
print(list_original)

# file_temp = open('file.txt', 'r')
file_temp = open(
    r'5_Знакомство с языком Python\Урок 2. Знакомство с Python. Продолжение\file.txt', 'r')
list_of_indexes = file_temp.readlines()
file_temp.close()

list_of_indexes = [i.rstrip() for i in list_of_indexes]
list_of_indexes = [int(i) for i in list_of_indexes]
print("indexes = ", list_of_indexes)

list_of_elements = [list_original[i] for i in list_of_indexes]
print("elements = ", list_of_elements)


nums_mlt = 1
for i in range(len(list_of_elements)):
    nums_mlt = nums_mlt * list_of_elements[i]
    #print(i, nums_mlt)
print("multiplication =  ", nums_mlt)
