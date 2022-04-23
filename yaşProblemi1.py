import random
import operator

soru_sayısı = 5

ilk_kişi = ["Zeynep", "Elif", "Yağmur", "Azra",
            "Elanur", "Nehir", "Meryem", "Irmak"]

ilk_kişi_ekli = ["Zeynep'in", "Elif'in", "Yağmur'un", "Azra'nın",
                 "Elanur'un", "Nehir'in", "Meryem'in", "Irmağın"]

ikinci_kişi = ["Yusuf", "Berat", "Emir", "Ahmet",
               "Ali", "Çınar", "Enes", "Kerem"]

ikinci_kişi_ekli = ["Yusuf'un", "Berat'ın", "Emir'in", "Ahmet'in",
                    "Ali'nin", "Çınar'ın", "Enes'in", "Kerem'in"]

ilk_seçilen_kişi = random.choice(ilk_kişi)
ilk_seçilen_kişi_index = int(ilk_seçilen_kişi.index)
ilk_seçilen_kişi_ekli = ilk_kişi_ekli[ilk_seçilen_kişi_index]

ikinci_seçilen_kişi = random.choice(ikinci_kişi)
ikinci_seçilen_kişi_index = int(ikinci_seçilen_kişi.index)
ikinci_seçilen_kişi_ekli = ikinci_kişi_ekli[ikinci_seçilen_kişi_index]


def random_soru():
    operators = {
        '-': operator.sub
    }
    sayı1 = random.randint(1, 5)  # fazla olan miktar
    sayı2 = random.randint(6, 20)  # 1. kişi yaşı

    operatoion = random.choice(list(operators.keys()))
    soruCevap = operators[operatoion](sayı2, sayı1)

    print("--------------------------")
    print(f"{ilk_seçilen_kişi_ekli} yaşı {ikinci_seçilen_kişi_ekli} yaşından {sayı1} fazladır, buna göre {ilk_seçilen_kişi} {sayı2} yaşında ise {ikinci_seçilen_kişi} kaç yaşındadır? ")
    print("--------------------------\n")
    return soruCevap


def soru():
    doğruCevap = random_soru()
    tahmin = float(input())
    return tahmin == doğruCevap


def yaşProblemi1():
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


soru()
