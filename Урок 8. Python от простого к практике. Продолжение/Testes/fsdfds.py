import csv
import os
from tabulate import tabulate


mydata = [['bc', 'afsd'],
          ['fdas', '341'],
          ['rewq', '12']]


def save_to_csv(save_directory, file_name, data):
    file_path = os.path.join(save_directory, file_name)
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def load_from_csv(load_directory, file_name):
    file_path = os.path.join(load_directory, file_name)
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return list(reader)


path_to_save_load = "5_Знакомство с языком Python\Урок 8. Python от простого к практике. Продолжение\Testes"
""" save_to_csv(path_to_save_load, "my_super_new_data", mydata)
 """

g4as5_gmalsk5_b54y3qjbk = load_from_csv(path_to_save_load, "my_super_new_data")

print(tabulate(g4as5_gmalsk5_b54y3qjbk,
               headers="firstrow",
               tablefmt='orgtbl',
               showindex="always",
               missingval="---"))
