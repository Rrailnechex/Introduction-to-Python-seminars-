import random
import Debug
import csv


def load_csv():
    global Cabinets_DB, Classes_DB, Students_DB, Teachers_DB

    with open('Cabinets_DB.csv', 'r') as file:
        reader = csv.reader(file)
        Cabinets_DB = list(reader)

    with open('Classes_DB.csv', 'r') as file:
        reader = csv.reader(file)
        Classes_DB = list(reader)

    with open('Students_DB.csv', 'r') as file:
        reader = csv.reader(file)
        Students_DB = list(reader)

    with open('Teachers_DB.csv', 'r') as file:
        reader = csv.reader(file)
        Teachers_DB = list(reader)


def save_csv():
    with open('Cabinets_DB.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(Cabinets_DB)

    with open('Classes_DB.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(Classes_DB)

    with open('Students_DB.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(Students_DB)

    with open('Teachers_DB.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(Teachers_DB)


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
