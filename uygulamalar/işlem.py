import operator
import random
from re import S

soru_sayısı = 20


def random_soru():
    operators = {
        '+': operator.add,
        '-': operator.sub, }

    sayı1 = random.randint(50, 90)
    sayı2 = random.randint(20, 49)

    operation = random.choice(list(operators.keys()))
    soruCevap = operators[operation](sayı1, sayı2)

    print("--------------------------")
    print(f"{sayı1} {operation} {sayı2} = ? ")
    print("--------------------------\n")
    return soruCevap


def soru():
    doğruCevap = random_soru()
    tahmin = float(input())
    return tahmin == doğruCevap


def işlem_oyunu():

    score = 0
    for i in range(soru_sayısı):

        if soru() == True:
            score += 1
            print("--------------------------")
            print("Doğru")
            print("--------------------------\n")
        else:
            print("--------------------------")
            print("Yanlış")
            print("--------------------------\n")

    print(f"Puanın: {score} ")
