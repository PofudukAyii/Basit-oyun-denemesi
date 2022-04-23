import random
from takvim import takvim_oyun


oyun_türü = ["AlışVeriş", "İşlem", "YaşProblemi",
             "Paragraf", "Problem1", "Problem 2", "Problem3", "Saat", "Takvim"]

seçilmiş_tür = random.choice(oyun_türü)
print(seçilmiş_tür)

if seçilmiş_tür == "Takvim":
    takvim_oyun()

elif seçilmiş_tür != "Takvim":
    print("Takvim sorusu değil")
