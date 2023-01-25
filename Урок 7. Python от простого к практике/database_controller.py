import pickle
import database_controller as DC
import Model
import json
import random
from a_database import a_database

global the_database
the_database = a_database


def main_controller():
    n_of_op = int(input("Input number of operation = "))
    if n_of_op == 1:
        create_new_phone_number()
    elif n_of_op == 2:
        create_new_random_phone_number()
    elif n_of_op == 3:
        delete_phone_number()
    elif n_of_op == 4:
        save_database_as()
    elif n_of_op == 5:
        load_database_as()
    elif n_of_op == 6:
        exit_programm()
    else:
        print("***wrong operation***")
        main_controller()


def create_new_phone_number():  # "1 - add new number"
    new_number = ["", "", ""]

    print("-- Create new number menu --")
    new_number[0] = str(input("Phone number = "))
    new_number[1] = str(input("Owner name = "))
    new_number[2] = str(input("Comment = "))

    the_database.reverse()
    the_database.append(new_number)
    the_database.reverse()


def create_new_random_phone_number():  # "2 - add new rendom number"
    new_number = ["", "", ""]
    names = ["Piotr", "Karpiński", "Tomasz", "Pawlak",
             "Henryk", "Leszczyński", "Michał", "Małek",
             "Lech", "Tomaszewski", "Przybysław", "Kowalewski",
             "Paweł", "Romanowski", "Franciszek", "Skrzypczak",
             "Michał", "Zawadzki", "Karol", "Sobolewski",
             "Sebastian", "Wilk", "Łukasz", "Karpiński"]

    new_number[0] = f"8(9{random.randint(0,99)}) {random.randint(100,999)} {random.randint(1000,9999)}"
    new_number[1] = f"{random.choice(names)} {random.choice(names)}"
    new_number[2] = "---"

    the_database.reverse()
    the_database.append(new_number)
    the_database.reverse()


def delete_phone_number():  # "3 - delete number"
    to_pop = int(input("Phone number = "))
    the_database.pop(to_pop)


def save_database_as(database_to_save):  # "4 - save phonebook"
    print("-- Save menu --")
    print("-- in development --")
    print("1 - save as pickle")
    print("2 - save as json")
    print("3 - go to main menu")

    way_to_save = int(input("way to save = "))
    if way_to_save == 1:
        DC.save_database_pickle(database_to_save)
    elif way_to_save == 2:
        DC.save_database_pickle(database_to_save)
    else:
        print("***wrong operation***")
        save_database_as(database_to_save)


def load_database_as(database_to_load):  # "5 - load phonebook"
    print("-- Load menu --")
    print("-- in development --")
    print("1 - load from pickled")
    print("2 - load from json")
    print("3 - go to main menu")

    way_to_load = int(input("way to save = "))
    if way_to_load == 1:
        DC.load_database_pickle(database_to_load)
    elif way_to_load == 2:
        DC.load_database_pickle(database_to_load)
    elif way_to_load == 3:
        Model.start()
    else:
        print("***wrong operation***")
        save_database_as(database_to_load)


def exit_programm():  # "6 - exit"
    exit()


def save_database_json(database_to_save):
    with open('5_Знакомство с языком Python\Урок 7. Python от простого к практике\database.json', "w") as outfile:
        json.dump(database_to_save, outfile)


def load_database_json(database_to_load):
    with open('5_Знакомство с языком Python\Урок 7. Python от простого к практике\database.json', 'r') as openfile:
        # Reading from json file
        database_to_load = json.load(openfile)


def save_database_pickle(database_to_save):
    data = []
    file = open(database_to_save, 'wb')
    pickle.dump(data, file)
    file.close()
    return data


def load_database_pickle(database_to_load):
    file = open(database_to_load, 'rb')
    data = pickle.load(file)
    file.close()
    return data
