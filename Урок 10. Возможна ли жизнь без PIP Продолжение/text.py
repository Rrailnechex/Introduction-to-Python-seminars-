import math


def mdiv(a, b):
    return a / b


def mmlt(a, b):
    return a * b


def madd(a, b):
    return a + b


def msub(a, b):
    return a - b


def mpow(a, b):
    return pow(a, b)


def mroot(a, b):
    return math.sqrt(a)


op = msub

print(op(5, 4))
