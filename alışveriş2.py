from operator import iadd
import random

soru_sayısı = 5
soru = ["alışveriş2"]
soruTipi = random.choice(soru)


def random_soru():
    kişiler = ["Ahmet", "Mehmet", "Kerem",
               "Kaan", "Ayşe", "Elif", "Azra", "Ela"]
    seçilmiş_kişi = random.choice(kişiler)

    mağza = ["Teknoloji", "Moda", "Gözlük", "Spor",
             "Ayakkabı", "Kozmetik", "Denizcilik", "Eğlence"]
    seçilmiş_mağza = random.choice(mağza)

    beğenilen_ürün_sayısı = random.randint(2, 6)
    toplam_fiyat = beğenilen_ürün_sayısı * random.randint(10, 15)

    alışveriş2Cevap = int(toplam_fiyat / beğenilen_ürün_sayısı)

    if soruTipi == "alışveriş2":
        print(
            f"{seçilmiş_kişi} bir {seçilmiş_mağza} mağzasına gidiyor gittiği mağzadan {beğenilen_ürün_sayısı} ürün beğeniyor ve şans eseri her ürünün fiyatının aynı olduğunu görüyor, aldığı ürünlerin toplam fiyatı {toplam_fiyat} olmak üzere kişinin aldığı ürünlerden bir tanesinin fiyatı nekadardır?")
        return alışveriş2Cevap


def alışveriş_doğru_cevap():
    doğruCevap = random_soru()
    tahmin = int(input())
    return tahmin == doğruCevap


def alışveriş_oyunu_2():
    skor = 0
    for i in range(soru_sayısı):
        if alışveriş_doğru_cevap() == True:
            skor += 1
            print("--------------------------")
            print("Doğru")
            print("--------------------------\n")
        else:
            print("--------------------------")
            print("Yanlış")
            print("--------------------------\n")

    print(f"Skorunuz: {skor}")
