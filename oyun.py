import random
from takvim import takvim_doğru_cevap


oyun_türü = ["AlışVeriş", "İşlem", "YaşProblemi",
             "Paragraf", "Problem1", "Problem 2", "Problem3", "Saat"]

seçilmiş_tür = random.choice(oyun_türü)
print(seçilmiş_tür)

if seçilmiş_tür == "Takvim":
    takvim_doğru_cevap()

elif seçilmiş_tür != "Takvim":
    print("Takvim sorusu değil")
