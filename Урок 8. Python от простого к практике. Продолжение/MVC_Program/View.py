from tabulate import tabulate
import os
from Controller import Cabinets_DB, Classes_DB, Students_DB, Teachers_DB


def clear(): return os.system('cls')


a_database = [312, "fda"]


def do_ui():
    clear()
    print(">>> MY COLLEGE DATABASE <<<")
    print(">> Students <<")
    print(tabulate(Students_DB,
                   headers="firstrow",
                   tablefmt='orgtbl',
                   showindex="always",
                   missingval="---"))
    print(">> Teachers <<")
    print(tabulate(Teachers_DB,
                   headers="firstrow",
                   tablefmt='orgtbl',
                   showindex="always",
                   missingval="---"))
    print(">> Cabinets <<")
    print(tabulate(Cabinets_DB,
                   headers="firstrow",
                   tablefmt='orgtbl',
                   showindex="always",
                   missingval="---"))
    print(">> Classes  <<")
    print(tabulate(Classes_DB,
                   headers="firstrow",
                   tablefmt='orgtbl',
                   showindex="always",
                   missingval="---"))

    print("--- Main menu ---")
    print("1 - add_object")
    print("2 - send_mail")
    print("3 - create_new_class")
    print("4 - print_object_stats")
    print("5 - load phonebook")
    print("0 - exit_programm")
