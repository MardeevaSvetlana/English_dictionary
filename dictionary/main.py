from numpy.core.defchararray import strip, lower

from words import words
import random
from phrases import *

br = ('*' * 60)
print(br)
print('Привет! How do you do?')

""" Выбор : перевод слов или устойчивых выражений"""


def change_user():
    try:
        print('Что хочешь переводить?:\n -слова -(1)\n -устойчивые выражения -(2)')
        ch_user = int(strip(input()))
        if ch_user == 1 or ch_user == 2:
            change(ch_user)
        else:
            print('Почти получилось! Попробуй еще раз\nТолько "1" или "2"')
            change_user()


    except Exception as error:
        print('Что- то пошло не так:', error)


""" Выбор режима перевода: англ- русс/ русс- анг"""


def change(ch_user):
    try:
        print('Выбери режим перевода:\n -c английского на русский -(1)\n -с русского на английский -(2)')
        ch = int(strip(input()))
        if ch == 1 or ch == 2:
            introduction(ch, ch_user)
        else:
            print('Ну нет, так не работает, пробуй еще.\nТолько "1" или "2"')
            change(ch_user)


    except Exception as error:
        print('Что- то пошло не так:', error)


""" Выбор количества слов/ фраз"""


def introduction(ch, ch_user):
    try:
        print(br)
        print('Доступно не более', len(words), 'слов (а) и', len(phrases), 'устойчивых выражений')
        print('Сколько слов\ фраз переведем?:')
        answer = int(strip(input()))
        if answer <= 0:
            print('С пути свернуть нельзя!')
            introduction(ch, ch_user)
        elif (ch_user == 1 and answer > len(words)) or (ch_user == 2 and answer > len(phrases)):

            print('Ты выбрал ношу не по плечу, сбавь обороты.')
            introduction(ch, ch_user)

        else:
            print('Ну что ж,вперед!')
            print(br)
            if ch_user == 1:
                train_word(answer, ch)
            else:
                train_ph(answer, ch)
    except Exception as error:
        print('Что- то пошло не так:', error)


list_error = []
"""Перевод слов"""


def train_word(answer, ch):
    try:
        print('По дефолту- глаголы, без "to", мужской род')
        count, mist = 0, 0
        random.shuffle(words)
        for i in range(answer):
            if ch == 1:
                word, key = words[i]
            else:
                key, word = words[i]
            print('\nВведи перевод слова "', word, '"')
            ans_user = lower(input())
            if ans_user == key:
                count += 1
                print('Отлично!!! Слово "', (word), '"', 'переводится как "', (key), '"')
                print('Правильных ответов:', count, 'ошибок:', mist)
            else:
                mist += 1
                list_error.append(word)
                list_error.append(key)
                print('Ошибочка вышла. Слово "', (word), '"', 'переводится как "', (key), '"')
                print('Правильных ответов:', count, 'ошибок:', mist)

        results(count, mist)
    except Exception as error:
        print('Что- то пошло не так:', error)


"""Перевод устойчивых выражений"""


def train_ph(answer, ch):
    try:
        print('По дефолту глаголы вида "ходить, учить" и т д без "to", мужской род, буква "Ё" не используется')
        count, mist = 0, 0
        random.shuffle(phrases)
        for i in range(answer):
            if ch == 1:
                word, key = phrases[i]
            else:
                key, word = phrases[i]

            print('\nПереведи фразу -', word)
            ans_user = lower(input())
            if ans_user == lower(key):
                count += 1
                print('Отлично!!! Фраза "', (word), '"', 'переводится как "', (key), '"')
                print('Правильных ответов:', count, 'ошибок:', mist)
            else:
                list_error.append(word)
                list_error.append(key)
                mist += 1
                print('Ошибочка вышла.Фраза "', (word), '"', 'переводится как "', (key), '"')
                print('Правильных ответов:', count, 'ошибок:', mist)

        results(count, mist)
    except Exception as error:
        print('Что- то пошло не так:', error)


"""Итоги"""


def results(count, mist):
    print(br)
    try:
        if mist == 0:
            print('\nПотрясающе! Ни одной ошибки !!!')
        else:
            print('\nУ тебя всё получится, вот увидишь!\nПравильных ответов:', count, '\nОшибок:', mist)
        print('\nНеплохо бы провести работу над ошибками:', (list_error))
        print("Я нуждаюсь в доработке , HELP ME")
    except Exception as error:
        print('Что- то пошло не так:', error)
    finally:
        print('\nИспытание закончено.\nGoogbye')


change_user()
input()
