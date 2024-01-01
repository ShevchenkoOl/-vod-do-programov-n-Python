#-------------------------------------Lekce 3 Funkce a moduly-----------------------------------------------
cislo = 3.141592
zaokrugleni = round(cislo, 2) # 3.14

jmeno = 'Theodor Holohlávek'
delka_jmena = len(jmeno) # 18

import math # Při použití modulu jej nejprve importujeme z interní knihovny
zaokrouhlene_horu = math.ceil(cislo) # 4
zaokrouhlene_dolu = math.floor(cislo) # 3

import random  # Při použití modulu jej nejprve importujeme z interní knihovny
nahodne_cislo = random.randint(1, 6) # výsledkem bude libovolné celé číslo od 1 do 6
nahodne_cislo_s_desitnou = random.uniform(0, 1) # výsledkem bude libovolné zlomkové číslo od 0 do 1, například  0.8019414964167082
nahodne_cislo_s_sotinou = round(random.uniform(0, 1), 2) # výsledkem bude libovolné zlomkové číslo od 0 do 1 se dvěma čislamy po čarký například  0.14

#-------------------------------Cvičení 1 Délka názvu ----------------------------------------------- 
nazev = "Divadlo Pěst na oko"
delka_napisu = len(nazev) * 30
print(f'délku nápisu {nazev} je {delka_napisu} cm') # 570 cm

#-------------------------------Cvičení 2 Zaokrouhlování --------------------------------------------------------
eur = 24
vstupenka_student = 0.65 * 12
koruny = round(vstupenka_student * eur)
print(f'studentské vstupné činí {koruny} kč') # 187 kč

#-------------------------------Cvičení 3 Zaokrouhlování nahoru--------------------------------
print(f'cena za vstupenky zaokrouhlování na horu bude: {math.ceil(vstupenka_student * eur)} kč') # 188 kč

#-------------------------------Cvičení 4 Náhodná čísla--------------------------------------------------------
nahodne_cislo = random.randint(1, 24) # napriklad 18

#-----------------------------------Cvičení na doma Klasické zaokrouhlování----------------------------------------
zaokrouhlene_cislo = round(3.5) # 4 (3,5 se zaokrouhlí na nejbližší sudé číslo, takže výsledek je 4.)

zaokrouhlene_cislo = round(2.5) # 2 (2,5 se zaokrouhlí na nejbližší sudé číslo, takže výsledek je 2.)

cislo = 2.6
print(round(cislo))
