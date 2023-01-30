from tabulate import tabulate
import os
# from Data import Cabinets_DB, Classes_DB, Students_DB, Teachers_DB
import Data


def do_ui():
    """ def clear(): return os.system('cls')
    clear() """
    """ os.system('cls') """
    print(">>> MY COLLEGE DATABASE <<<")
    
    print(">> Students <<")
    print(tabulate(Data.Students_DB,
                   headers="firstrow",
                   tablefmt='orgtbl',
                   showindex="always",
                   missingval="---"))
    
    print(">> Teachers <<")
    print(tabulate(Data.Teachers_DB,
                   headers="firstrow",
                   tablefmt='orgtbl',
                   showindex="always",
                   missingval="---"))
    
    print(">> Cabinets <<")
    print(tabulate(Data.Cabinets_DB,
                   headers="firstrow",
                   tablefmt='orgtbl',
                   showindex="always",
                   missingval="---"))
    
    print(">> Classes  <<")
    print(tabulate(Data.Classes_DB,
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
    print("99 - pass_program")
