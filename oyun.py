import random
from saat import saat_oyunu
from takvim import takvim_oyunu
from işlem import işlem_oyunu
from alışveriş import alışveriş_oyunu

oyun_türü = ["AlışVeriş", "İşlem", "Paragraf",
             "Problem1", "Problem 2", "Problem3", "Saat", "Takvim"]

seçilmiş_tür = random.choice(oyun_türü)
print(seçilmiş_tür)

if seçilmiş_tür == "Takvim":
    takvim_oyunu()
elif seçilmiş_tür == "İşlem":
    işlem_oyunu()
elif seçilmiş_tür == "Saat":
    saat_oyunu()
elif seçilmiş_tür == "AlışVeriş":
    alışveriş_oyunu()
elif seçilmiş_tür != "Takvim" "İşlem" "Saat" "AlışVeriş":
    print("Henüz kodlamakla uğraşmadın")
