

""" Напишите программу, удаляющую из текста все слова, содержащие ""абв"". """
""" Задача: предложить улучшения кода для уже решённых задач:
С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension """




import os
def remove_from_word_abc(text_in, abc):
    text_out = " ".join([word for word in text_in.split() if abc not in word])
    return text_out


os.chdir("5_Знакомство с языком Python\Урок 6. Ускоренная обработка данных продолжение")
with open("text1input.txt", "r") as input_file:
    text_in = input_file.read()

abc = "cons"
#abc = "er"

print("Cluster of Consonants:", abc)
print("Original text:", text_in)
text_out = remove_from_word_abc(text_in, abc)
print("Processed text", text_out)

with open("text1output.txt", "w") as output_file:
    output_file.write(text_out)
