

""" Напишите программу, которая 
по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y). """

print("Enter 'quater number' please")
q_n = int(input())


def Show_diapazon(q_n):
    if q_n == 1:
        print("diapazon is from '+1, +1' to '+inf, +inf'")
    elif q_n == 2:
        print("diapazon is from '-1, +1' to '-inf, +inf'")
    elif q_n == 3:
        print("diapazon is from '-1, -1' to '-inf, -inf'")
    elif q_n == 4:
        print("diapazon is from '+1, -1' to '+inf, -inf'")


Show_diapazon(q_n)
