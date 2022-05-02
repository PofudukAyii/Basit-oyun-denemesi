import random
from re import A
kişiler_normal = ["Ahmet", "Mehmet", "Kerem",
                  "Kaan", "Ayşe", "Elif", "Azra", "Ela"]
seçilmiş_kişi = random.choice(kişiler_normal)

kişiler_ekli = ["Ahmetin", "Mehmetin", "Keremin",
                "Kaanın", "Ayşenin", "Elifin", "Azranın", "Elanın"]

seçilmiş_ekli_sıra = kişiler_normal.index
seçilmiş_ekli = kişiler_ekli(seçilmiş_ekli_sıra)

print(seçilmiş_kişi)
print(seçilmiş_ekli)
