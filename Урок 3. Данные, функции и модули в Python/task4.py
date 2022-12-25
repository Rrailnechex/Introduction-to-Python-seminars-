
""" 
Напишите программу, 
которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
 """
import time


def convert_cards_to_1010100(card):
    card101001 = []
    # делаем лист из 1иц и 0ей а не из True False
    for i in range(len(card)):
        if card[i] is True:
            card101001.append(1)
        else:
            card101001.append(0)
    # сокращаем 0000000001011 число в 1011
    """ for i in range(len(card)):
        if card101001[i] != 1:
            del card101001[0]
        elif card101001[i] == 1:
            break
        else:
            break """
    # соеденяем лист в строку
    string1010110 = ''.join(map(str, card101001))
    return string1010110


number_original = 45
# number_original = 3
# number_original = 2

cards = []
for i in range(32):
    cards.append(False)


def flip(bool):
    return not bool


def flip_last_card(card_ori):
    card_ori[-1] = flip(card_ori[-1])
    return card_ori


def flip_next_cards(card_ori):
    card_ori = card_ori.reverse()
    for
    #card_new = card_ori.reverse()
    return card_ori

    # def flip_cycle(iteration):
for i in range(len(cards)):
    flip_last_card(cards)
    flip_next_cards(cards)

    print(convert_cards_to_1010100(cards))
    time.sleep(0.01)


print("end")
print(convert_cards_to_1010100(cards))

