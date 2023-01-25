
from csv import writer

List = [789633, 'dsa', 1.222, 1.0001, 'нертог']


with open('5_Знакомство с языком Python\Урок 7. Python от простого к практике\database.csv', 'a') as f_object:
    
    writer_object = writer(f_object)
    
    
    writer_object.writerow(List)

