import random
from takvim import takvim_oyunu
from işlem import işlem_oyunu


oyun_türü = ["AlışVeriş", "İşlem", "YaşProblemi1", "YaşProblemi2"
             "Paragraf", "Problem1", "Problem 2", "Problem3", "Saat", "Takvim"]

seçilmiş_tür = random.choice(oyun_türü)
print(seçilmiş_tür)

if seçilmiş_tür == "Takvim":
    takvim_oyunu()
elif seçilmiş_tür == "İşlem":
    işlem_oyunu()

elif seçilmiş_tür != "Takvim" "İşlem":
    print("Henüz kodlamakla uğraşmadın")
