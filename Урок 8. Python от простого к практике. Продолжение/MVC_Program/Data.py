import csv


global Cabinets_DB, Classes_DB, Students_DB, Teachers_DB


with open("5_Знакомство с языком Python\Урок 8. Python от простого к практике. Продолжение\Database\Cabinets_DB.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    Cabinets_DB = list(csv.reader(file))

with open("5_Знакомство с языком Python\Урок 8. Python от простого к практике. Продолжение\Database\Classes_DB.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    Classes_DB = list(csv.reader(file))

with open("5_Знакомство с языком Python\Урок 8. Python от простого к практике. Продолжение\Database\Students_DB.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    Students_DB = list(csv.reader(file))

with open("5_Знакомство с языком Python\Урок 8. Python от простого к практике. Продолжение\Database\Teachers_DB.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    Teachers_DB = list(csv.reader(file))
