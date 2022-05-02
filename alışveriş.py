from operator import iadd
import random

soru_sayısı = 5
soru = ["alışveriş"]
soruTipi = random.choice(soru)


def random_soru():
    kişiler = ["Ahmet", "Mehmet", "Kerem",
               "Kaan", "Ayşe", "Elif", "Azra", "Ela"]
    seçilmiş_kişi = random.choice(kişiler)

    elma_sayısı = random.randint(5, 10)
    şeftal_sayısı = random.randint(5, 10)
    çürük_sayısı = random.randint(1, 5)

    alışverişCevap = elma_sayısı + şeftal_sayısı - çürük_sayısı

    if soruTipi == "alışveriş":
        print(alışverişCevap)
        print(
            f"{seçilmiş_kişi} bakkala gidiyor bakkaldan {elma_sayısı} tane 🍎 ve {şeftal_sayısı} tane 🍑 alıyor, {seçilmiş_kişi} eve geldiğinde aldığı ürünlerin toplamının {çürük_sayısı} tanesi çürük çıkıyor ve çöpe atıyor {seçilmiş_kişi} bu meyveleri yemek için sofraya oturduğunda önünde kaç tane meyve olur? ")
        return alışverişCevap


def alışveriş_doğru_cevap():
    doğruCevap = random_soru()
    tahmin = int(input())
    return tahmin == doğruCevap


def alışveriş_oyunu():
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
