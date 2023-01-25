import csv
""" from csv import reader """

""" with open('5_Знакомство с языком Python\Урок 7. Python от простого к практике\database.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row) """

with open('5_Знакомство с языком Python\Урок 7. Python от простого к практике\database.csv', newline='') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        if not line:
            continue  # skip empty lines
        print(line)
