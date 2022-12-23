
""" 
Напишите программу, которая 
принимает на вход вещественное число и 
показывает сумму его цифр.

Пример:

- 6782 -> 23
- 0,56 -> 11
 """

number = int(input("Enter 'Number' = "))

digits = [int(x) for x in str(number)]


def get_digits_summ(digits):
    summ = 0
    for i in range(len(digits)):
        summ += digits[i]
    return summ


print(f"Result = {get_digits_summ(digits)} ")
