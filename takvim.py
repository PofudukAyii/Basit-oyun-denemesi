import random
from re import X

sorusayisi = 5


def random_soru():
    soru = ["Takvim"]
    soruTipi = random.choice(soru)

# Takvim sorusu için gereken atamalar başlangıç #

    günler = ["pazartesi", "salı", "çarşamba",
              "perşembe", "cuma", "cumartesi", "pazar"]
    xTakvimGün = random.choice(günler)
    xTakvimSayı = random.randint(1, 30)
    takvimSeçim = (günler.index(xTakvimGün) + xTakvimSayı - 1) % 7
    takvimCevap = günler[takvimSeçim]
    print(takvimCevap)

# Takvim sorusu için gereken atamalar bitiş #

    if soruTipi == "Takvim":
        print(
            f"Bugün günlerden {xTakvimGün} ise {xTakvimSayı} gün sonraki gün nedir? ")
        return takvimCevap
    if soruTipi == "İşlem":
        print()

# Takvim kodları başlangıç #


def takvim_doğru_cevap():
    doğruCevap = random_soru()
    tahmin = input()
    return tahmin == doğruCevap


def takvim_oyun():
    skor = 0
    for i in range(sorusayisi):
        if takvim_doğru_cevap() == True:
            skor += 1
            print("Tebrikler")
        else:
            print("Üzgünüm")
    print(f"Skorunuz: {skor}")
# Takvim kodları bitiş #
