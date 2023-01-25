from tabulate import tabulate
from a_database import a_database


def print_ui():
    print()
    print(">>> My Phone Book <<<")
    a_database.reverse()
    print(tabulate(a_database,
                   headers=['№', 'Number', 'Name', 'Comment'],
                   tablefmt='orgtbl',
                   showindex="always",
                   missingval="---"))
    a_database.reverse()
    print("--- Main menu ---")
    print("1 - add new number")
    print("2 - add new rendom number")
    print("3 - delete number")
    print("4 - save phonebook")
    print("5 - load phonebook")
    print("6 - exit")
