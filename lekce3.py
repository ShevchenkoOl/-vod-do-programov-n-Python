#-------------------------------------Lekce 3 Funkce a moduly-----------------------------------------------
cislo = 3.141592
zaokrugleni = round(cislo, 2) # 3.14

jmeno = 'Theodor Holohlávek'
delka_jmena = len(jmeno) # 18

import math
zaokrouhlene_horu = math.ceil(cislo) # 4
zaokrouhlene_dolu = math.floor(cislo) # 3

import random
nahodne_cislo = random.randint(1, 6) # výsledkem bude libovolné celé číslo od 1 do 6
nahodne_cislo_s_desitnou = random.uniform(0, 1) # výsledkem bude libovolné zlomkové číslo od 0 do 1, například  0.8019414964167082
nahodne_cislo_s_sotinou = round(random.uniform(0, 1), 2) # výsledkem bude libovolné zlomkové číslo od 0 do 1 se dvěma čislamy po čarký například  0.14

#-------------------------------Cvičení 1 Délka názvu ----------------------------------------------- 
nazev = "Divadlo Pěst na oko"
delka_napisu = len(nazev) * 30
print(f'délku nápisu {nazev} je {delka_napisu} cm')