# 5. Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, 
# взятых из трёх списков (по одному из каждого)

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def create_random_sentence(n, condition):

    from random import choice

    sentences = []

    if condition == 'False':
        sentences = [f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}' for _ in range(n)]

    if condition == 'True':
        stop = len(nouns) - 1
        for i in range(n):
            if i > stop:
                break
            else:
                random_noun = choice(nouns)
                nouns.remove(random_noun)
                random_adverb = choice(adverbs)
                adverbs.remove(random_adverb)
                random_adjective = choice(adjectives)
                adjectives.remove(random_adjective)
                sentences.append(f'{random_noun} {random_adverb} {random_adjective}')

    return sentences
            

sent_num = int(input("Input number of random sentences: ")) 
type_of_creation = input("Input type of creation ('True' or 'False'): ")
print(create_random_sentence(sent_num, type_of_creation))
