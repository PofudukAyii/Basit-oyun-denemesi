import operator
import random
from re import S
import time
soru_sayısı = 5
soru = ["saat"]
soruTipi = random.choice(soru)


def random_soru():

    saat_ek = random.randint(1, 23)
    dakika_ek = random.randint(1, 59)
    timer = time.localtime()
    saat = timer.tm_hour
    dakika = timer.tm_min

    yeni_saat = saat + saat_ek
    yeni_dakika = dakika + dakika_ek

    if yeni_dakika >= 59:
        yeni_dakika = yeni_dakika - 60
        yeni_saat = yeni_saat + 1

    if yeni_saat >= 24:
        yeni_saat = yeni_saat - 24

    saatCevap = (f"{yeni_saat}:{yeni_dakika}")

    if soruTipi == "saat":
        print(saatCevap)
        print(
            f"Şuan saat {saat}:{dakika} ise {saat_ek}:{dakika_ek} sonra saat kaç olur?")
        return saatCevap


def saat_doğru_cevap():
    doğruCevap = random_soru()
    tahmin = input()
    return tahmin == doğruCevap


def saat_oyunu():
    skor = 0
    for i in range(soru_sayısı):
        if saat_doğru_cevap() == True:
            skor += 1
            print("--------------------------")
            print("Doğru")
            print("--------------------------\n")
        else:
            print("--------------------------")
            print("Yanlış")
            print("--------------------------\n")

    print(f"Skorunuz: {skor}")


saat_oyunu()
