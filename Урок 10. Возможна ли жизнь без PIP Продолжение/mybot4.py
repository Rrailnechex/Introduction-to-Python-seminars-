import telebot
from telebot import types
import math
import re

bot = telebot.TeleBot("5997337531:AAGYp6im2UYRSzb_QGrvhoUtBY32dEpclr0")


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


def lsumm(message):
    summ = sum(list(map(int, message.text.split())))
    bot.send_message(message.chat.id, str(summ))
    button(message)


def lsub(message):
    num = list(map(int, message.text.split()))
    number = num[0] - num[1]
    bot.send_message(message.chat.id, str(number))
    button(message)


def ldiv(message):
    num = list(map(int, message.text.split()))
    number = num[0] / num[1]
    bot.send_message(message.chat.id, str(number))
    button(message)


def lmlt(message):
    num = list(map(int, message.text.split()))
    number = num[0] * num[1]
    bot.send_message(message.chat.id, str(number))
    button(message)


def lpow(message):
    num = list(map(int, message.text.split()))
    number = pow(num[0], num[1])
    bot.send_message(message.chat.id, str(number))
    button(message)


def lroot(message):
    num = list(map(int, message.text.split()))
    number = math.sqrt(num[0])
    bot.send_message(message.chat.id, str(number))
    button(message)


# @bot.message_handler(commands=["button"])
@bot.message_handler(commands=["start"])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but11 = types.KeyboardButton("summ")
    but12 = types.KeyboardButton("substraction")
    but21 = types.KeyboardButton("division")
    but22 = types.KeyboardButton("multiplication")
    but31 = types.KeyboardButton("power")
    but32 = types.KeyboardButton("sqwre root")
    markup.add(but11)
    markup.add(but12)
    markup.add(but21)
    markup.add(but22)
    markup.add(but31)
    markup.add(but32)
    bot.send_message(message.chat.id, "Choose operation", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def controller(message):
    if message.text == "summ":
        bot.send_message(
            message.chat.id, "Enter two number separeted by spase for summ: ")
        bot.register_next_step_handler(message, lsumm)
    elif message.text == "substraction":
        bot.send_message(
            message.chat.id, "Enter two number separeted by spase for substraction: ")
        bot.register_next_step_handler(message, lsub)
    elif message.text == "division":
        bot.send_message(
            message.chat.id, "Enter two number separeted by spase for division: ")
        bot.register_next_step_handler(message, ldiv)
    elif message.text == "multiplication":
        bot.send_message(
            message.chat.id, "Enter two number separeted by spase for multiplication: ")
        bot.register_next_step_handler(message, lmlt)
    elif message.text == "power":
        bot.send_message(
            message.chat.id, "Enter two number separeted by spase for power: ")
        bot.register_next_step_handler(message, lpow)
    elif message.text == "sqwre root":
        bot.send_message(message.chat.id, "Enter one number for sqwre root: ")
        bot.register_next_step_handler(message, lroot)


bot.infinity_polling()
