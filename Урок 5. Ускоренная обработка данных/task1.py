

""" Напишите программу, удаляющую из текста все слова, содержащие ""абв"". """


import os
import time
import pprint


def remove_from_word_abc(text_in, abc):
    words = text_in.split()
    filtered_words = []
    for word in words:
        if abc not in word:
            filtered_words.append(word)
    text_out = " ".join(filtered_words)
    return text_out


os.chdir("5_Знакомство с языком Python\Урок 5. Ускоренная обработка данных")
with open("text1input.txt", "r") as input_file:
    text_in = input_file.read()

abc = "abc"
#abc = "er"

print("Cluster of Consonants:", abc)
print("Original text:", text_in)
text_out = remove_from_word_abc(text_in, abc)
print("Processed text", text_out)

with open("text1output.txt", "w") as output_file:
    output_file.write(text_out)
