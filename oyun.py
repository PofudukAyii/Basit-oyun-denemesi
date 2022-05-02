import random
from saat import saat_oyunu
from takvim import takvim_oyunu
from işlem import işlem_oyunu
from alışveriş1 import alışveriş_oyunu
from alışveriş2 import alışveriş_oyunu_2

oyun_türü = ["AlışVeriş1", "Alışveriş2", "İşlem", "Paragraf",
             "Problem", "Saat", "Takvim"]

seçilmiş_tür = random.choice(oyun_türü)
print(seçilmiş_tür)

if seçilmiş_tür == "Takvim":
    takvim_oyunu()
elif seçilmiş_tür == "İşlem":
    işlem_oyunu()
elif seçilmiş_tür == "Saat":
    saat_oyunu()
elif seçilmiş_tür == "AlışVeriş1":
    alışveriş_oyunu()
elif seçilmiş_tür == "Alışveriş2":
    alışveriş_oyunu_2()
elif seçilmiş_tür != "Takvim" "İşlem" "Saat" "AlışVeriş1" "AlışVeriş2":
    print("Henüz kodlamakla uğraşmadın")
