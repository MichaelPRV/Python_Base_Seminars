
# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from itertools import groupby, starmap
from os import path


def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):

    if path.exists(text):
        with open(text) as my_text, \
                open(code_text, "a") as my_code:
            for i in my_text:
                my_code.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("The files do not exist in the system!")


def rle_decode(name):

    if path.exists(name):
        with open(name) as my_code:
            n = ""
            for k in my_code:
                word_numbers = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        word_numbers.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x * y, word_numbers)))
    else:
        print("The files do not exist in the system!")



rle_encode(input("Enter the name of the file with the text: "), input("Enter the file name to record: "))
rle_decode(input("Enter the name of the file to decode: "))
