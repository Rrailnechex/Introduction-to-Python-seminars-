# Я обьеденил файлы так как не получилось с глобальными переменными сквозь файлы работать


# ------- INIT ALL -------


import os
import csv
from tabulate import tabulate

global Cabinets_DB, Classes_DB, Students_DB, Teachers_DB, path_to_save_load

Cabinets_DB = []
Classes_DB = []
Students_DB = []
Teachers_DB = []
path_to_save_load = "5_Знакомство с языком Python\Урок 8. Python от простого к практике. Продолжение\Database"


# ------- ETC -------


def Debug_simple_debug(error_text):
    if False:
        print(f"/// Debuged [{error_text}] ///")


# ------- CONTROLLER -------

# 5_Знакомство с языком Python\Урок 8. Python от простого к практике. Продолжение\Database\Students_DB.csv


def simple_load_from_csv(load_directory, file_name):
    Debug_simple_debug("simple_load_from_csv(load_directory, file_name):")

    file_path = os.path.join(load_directory, file_name)
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return [row for row in reader if row]


def simple_save_to_csv(save_directory, file_name, data):
    Debug_simple_debug("simple_save_to_csv(save_directory, file_name, data):")

    file_path = os.path.join(save_directory, file_name)
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def Controller_load_csv():
    Debug_simple_debug("load_csv():")

    global Cabinets_DB, Classes_DB, Students_DB, Teachers_DB, path_to_save_load

    Teachers_DB = simple_load_from_csv(path_to_save_load, "Teachers_DB.csv")
    Students_DB = simple_load_from_csv(path_to_save_load, "Students_DB.csv")
    Cabinets_DB = simple_load_from_csv(path_to_save_load, "Cabinets_DB.csv")
    Classes_DB = simple_load_from_csv(path_to_save_load, "Classes_DB.csv")


def Controller_save_csv():
    Debug_simple_debug("def add_object():")

    global Cabinets_DB, Classes_DB, Students_DB, Teachers_DB, path_to_save_load

    simple_save_to_csv(path_to_save_load, "Teachers_DB.csv", Teachers_DB)
    simple_save_to_csv(path_to_save_load, "Students_DB.csv", Students_DB)
    simple_save_to_csv(path_to_save_load, "Cabinets_DB.csv", Cabinets_DB)
    simple_save_to_csv(path_to_save_load, "Classes_DB.csv", Classes_DB)


def Controller_main_controller():
    n_of_op = int(input("Input number of operation = "))
    if n_of_op == 1:
        add_object()
    elif n_of_op == 2:
        get_rid_of_an_object()
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
        Controller_main_controller()


def generate_list():
    Debug_simple_debug("generate_list():")
    list_length = int(input("List length = "))
    items = []

    for i in range(list_length):
        item = input(f"Enter item {i+1}: ")
        items.append(item)

    return items


def add_row_to_sheet(sheet, new_row):
    Debug_simple_debug("add_row_to_sheet(sheet, new_row):")
    sheet.append(new_row)


def add_object():  # "1 - add new number"
    Debug_simple_debug("def add_object():")

    global Cabinets_DB, Classes_DB, Students_DB, Teachers_DB

    print("-- Add Object menu --")
    print("1 - add new theacher")
    print("2 - add new student")
    print("3 - add new cabinet")
    print("4 - add new class")

    chousen_variant = int(input("Input number of operation = "))
    chousen_db = []

    if chousen_variant == 1:
        chousen_db = Teachers_DB
    elif chousen_variant == 2:
        chousen_db = Students_DB
    elif chousen_variant == 3:
        chousen_db = Cabinets_DB
    elif chousen_variant == 4:
        chousen_db = Classes_DB
    else:
        print("***wrong operation***")
        add_object()

    add_row_to_sheet(chousen_db, generate_list())


def remove_row_from_sheet(sheet, index):
    del sheet[index-1]


def get_rid_of_an_object():  # "1 - add new number"
    Debug_simple_debug("def add_object():")

    global Cabinets_DB, Classes_DB, Students_DB, Teachers_DB

    print("-- Get rid of an object --")
    print("1 - get rid of theacher")
    print("2 - get rid of student")
    print("3 - get rid of cabinet")
    print("4 - get rid of class")

    chousen_variant = int(input("Input number of operation = "))
    id_to_delete = int(input("Input id to delete = "))
    chousen_db = []

    if chousen_variant == 1:
        chousen_db = Teachers_DB
    elif chousen_variant == 2:
        chousen_db = Students_DB
    elif chousen_variant == 3:
        chousen_db = Cabinets_DB
    elif chousen_variant == 4:
        chousen_db = Classes_DB
    else:
        print("***wrong operation***")
        get_rid_of_an_object()

    # chousen_db.reverse()
    remove_row_from_sheet(chousen_db, id_to_delete-1)
    # chousen_db.reverse()


def send_mail():
    Debug_simple_debug("def send_mail():")
    print("Mail had been send")


def create_new_class():
    Debug_simple_debug("def create_new_class():")
    print("in")


def exit_programm():  # 0
    Debug_simple_debug("def exit_programm():")
    exit()


def pass_program():
    Debug_simple_debug("def pass_program():")
    pass

# ------- VIEW -------


def print_table_style(DB):
    print(tabulate(DB,
                   showindex="always",
                   headers="firstrow",
                   tablefmt="orgtbl",
                   missingval=""))


def View_do_ui():
    Debug_simple_debug("View_do_ui():")

    print(">>> MY COLLEGE DATABASE <<<")

    print(">> Students <<")
    print_table_style(Students_DB)

    print(">> Teachers <<")
    print_table_style(Teachers_DB)

    print(">> Cabinets <<")
    print_table_style(Cabinets_DB)

    print(">> Classes  <<")
    print_table_style(Classes_DB)

    print("--- Main menu ---")
    print("1 - add_object")
    print("2 - get_rid_of_an_object")
    print("0 - exit_programm")
    print("99 - pass_step_program")


# ------- MODEL -------


def Model_start():
    Debug_simple_debug("Model_start():")
    while True:
        Debug_simple_debug("Model_start(): - new cycle")
        Controller_load_csv()
        View_do_ui()
        Controller_main_controller()
        Controller_save_csv()


# ------- MAIN -------


Model_start()
