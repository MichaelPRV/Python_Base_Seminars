
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". 
# В тексте используется разделитель пробел.

def create_random_string(num):
    
    from random import sample
    array = []
    string = ''
    for i in range(num):
        array.append(sample('abv', 3))
        string += ''.join(array[i]) + ' '

    return string

def delete_word_from_string(string, word):
    array = string.split()
    corrected_array = [i for i in array if i != word]
    new_string = ' '.join(corrected_array)
    return new_string

n = int(input("Input number of words: "))

if n > 0:
    new_str = create_random_string(n)
    print(new_str)
    final_str = delete_word_from_string(new_str, 'abv')
    print(final_str)
else:
    print("The data is incorrect")