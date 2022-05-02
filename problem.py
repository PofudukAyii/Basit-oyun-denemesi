from operator import iadd
import random

soru_sayısı = 5
soru = ["problem"]
soruTipi = random.choice(soru)


def random_soru():
    kişiler_normal = ["Ahmet", "Mehmet", "Kerem",
                      "Kaan", "Ayşe", "Elif", "Azra", "Ela"]
    seçilmiş_kişi = random.choice(kişiler_normal)

    kişiler_ekli = ["Ahmetin", "Mehmetin", "Keremin",
                    "Kaanın", "Ayşenin", "Elifin", "Azranın", "Elanın"]
    seçilmiş_ekli = kişiler_normal.index([kişiler_ekli])

    problemCevap = asd
    if soruTipi == "problem":
        print(
            f"kişinin cebinde x para var ve canı dondurma yemek istiyor fakat dondurmacı her bir topun y tl olduğunu söylüyor ve bunu gören kişi 4 top alamıyacağını söylüyor ama 3 top alabiliyor. Buna göre bu kişinin cebinde en çok kaç tl para vardır ")
        return problemCevap


def problem_doğru_cevap():
    doğruCevap = random_soru()
    tahmin = int(input())
    return tahmin == doğruCevap


def problem_oyunu():
    skor = 0
    for i in range(soru_sayısı):
        if problem_doğru_cevap() == True:
            skor += 1
            print("--------------------------")
            print("Doğru")
            print("--------------------------\n")
        else:
            print("--------------------------")
            print("Yanlış")
            print("--------------------------\n")

    print(f"Skorunuz: {skor}")
