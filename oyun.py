import random
from uygulamalar.saat import saat_oyunu
from uygulamalar.takvim import takvim_oyunu
from uygulamalar.işlem import işlem_oyunu
from uygulamalar.alışveriş1 import alışveriş_oyunu
from uygulamalar.alışveriş2 import alışveriş_oyunu_2


oyun_türü = ["AlışVeriş1", "Alışveriş2", "İşlem", "Saat", "Takvim"]

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
