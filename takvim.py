import random
from re import X

soru_sayısı = 5


def random_soru():
    soru = ["Takvim"]
    soruTipi = random.choice(soru)

    günler = ["pazartesi", "salı", "çarşamba",
              "perşembe", "cuma", "cumartesi", "pazar"]
    xTakvimGün = random.choice(günler)
    xTakvimSayı = random.randint(1, 30)
    takvimSeçim = (günler.index(xTakvimGün) + xTakvimSayı - 1) % 7
    takvimCevap = günler[takvimSeçim]

    if soruTipi == "Takvim":
        print(
            f"Bugün günlerden {xTakvimGün} ise {xTakvimSayı - 1} gün sonraki gün nedir? ")
        return takvimCevap


def takvim_doğru_cevap():
    doğruCevap = random_soru()
    tahmin = input()
    return tahmin == doğruCevap


def takvim_oyunu():
    skor = 0
    for i in range(soru_sayısı):
        if takvim_doğru_cevap() == True:
            skor += 1
            print("--------------------------")
            print("Doğru")
            print("--------------------------\n")
        else:
            print("--------------------------")
            print("Yanlış")
            print("--------------------------\n")

    print(f"Skorunuz: {skor}")
