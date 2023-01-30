import os
import Debug
import csv
import Data

# 5_Знакомство с языком Python\Урок 8. Python от простого к практике. Продолжение\Database\Students_DB.csv


def simple_load_from_csv(load_directory, file_name):
    Debug.simple_debug("simple_load_from_csv(load_directory, file_name):")

    file_path = os.path.join(load_directory, file_name)
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return list(reader)


def simple_save_to_csv(save_directory, file_name, data):
    Debug.simple_debug("simple_save_to_csv(save_directory, file_name, data):")

    file_path = os.path.join(save_directory, file_name)
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def load_csv():
    Debug.simple_debug("load_csv():")

    path_to_save_load = "5_Знакомство с языком Python\Урок 8. Python от простого к практике. Продолжение\Database"

    Teachers_DB = simple_load_from_csv(path_to_save_load, Teachers_DB)
    Students_DB = simple_load_from_csv(path_to_save_load, Students_DB)
    Cabinets_DB = simple_load_from_csv(path_to_save_load, Cabinets_DB)
    Classes_DB = simple_load_from_csv(path_to_save_load, Classes_DB)

    return Cabinets_DB, Classes_DB, Students_DB, Teachers_DB


def save_csv(Cabinets_DB, Classes_DB, Students_DB, Teachers_DB):
    Debug.simple_debug("def add_object():")

    path_to_save_load = "5_Знакомство с языком Python\Урок 8. Python от простого к практике. Продолжение\Database"

    simple_save_to_csv(path_to_save_load, "Teachers_DB", Teachers_DB)
    simple_save_to_csv(path_to_save_load, "Students_DB", Students_DB)
    simple_save_to_csv(path_to_save_load, "Cabinets_DB", Cabinets_DB)
    simple_save_to_csv(path_to_save_load, "Classes_DB", Classes_DB)


def main_controller():
    n_of_op = int(input("Input number of operation = "))
    if n_of_op == 1:
        add_object()
    elif n_of_op == 2:
        send_mail()
    elif n_of_op == 3:
        create_new_class()
    elif n_of_op == 4:
        print_object_stats()
    elif n_of_op == 0:
        exit_programm()
    elif n_of_op == 99:
        pass_program()
    else:
        print("***wrong operation***")
        main_controller()


def add_object():  # "1 - add new number"
    Debug.simple_debug("def add_object():")

    print("-- Add Object menu --")
    print("-- in development --")
    print("1 - save as pickle")
    print("2 - save as json")
    print("3 - go to main menu")

    new_object = ["", "", ""]

    print("-- Create new object menu --")
    new_object[0] = str(input("Phone object = "))
    new_object[1] = str(input("Owner name = "))
    new_object[2] = str(input("Comment = "))


def send_mail():
    Debug.simple_debug("def send_mail():")


def create_new_class():
    Debug.simple_debug("def create_new_class():")


def print_object_stats():
    Debug.simple_debug("def print_object_stats():")


def exit_programm():  # 0
    Debug.simple_debug("def exit_programm():")
    exit()


def pass_program():
    Debug.simple_debug("def pass_program():")
    pass
