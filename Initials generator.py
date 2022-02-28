import random

#Создаём глобальный список имён
names = [
    "Павел",
    "Василий",
    "Даниил",
    "Егор",
    "Кирилл",
    "Артём"
]

Consonant = list("клнпстхт")
Vowel = list("аеоуяюэ")
Ending = "о ов ин ий ев ич".split()

#Генератор слога

def syllable_generator():
    first  = random.choice(list(Consonant))
    second = random.choice(list(Vowel))
    return first+second

#Состав генерируемой фамилии: некоторое количество слогов (произвольное) + окончание из списка Ending
def surname_generator(start,stop):
    temp = "".join([syllable_generator() for i in range (start, stop + 1)])
    return temp + random.choice(Consonant) + random.choice(Ending)


#от трёх до 5 слогов, capitalize - для заглавной буквы на 1 месте
def random_fio_generator():
    name=random.choice(names)
    suranme = surname_generator(2,random.randint(2,6)).capitalize()
    return name + " " + suranme


for i in range(50):
    print (random_fio_generator())
