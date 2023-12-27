#-----------------------------------------------Lekce 2 Proměnné--------------------------------------
sazba = 450
cena_zakazky = 8 * sazba
print(cena_zakazky)

sazba = sazba-50
print(cena_zakazky) #Vytiskne stale stejnou hodnotu. Python totiž provádí příkazy řádek po řádku a vždy pracuje s hodnotou, která je v proměnné aktuálně uložená.

#---------------------------------------------Cvičení 1 Základní aritmetické operace-------------------
a = 15
b = 3.14

soucet = a + b
print(f'Сумма a + b: {soucet}')

soucin = a * b
print(f'Součin a * b: {soucin}')

zbytek = a % b
print(f'Zbytek po dělení a % b: {zbytek}')

cele = a // b
print(f'Celočíselné dělení a // b: {cele}')

#---------------------------------------------Cvičení 2 Antikvariát---------------------

nazev_antikvariatu = "Poslední strana"
cena_za_kus = 50
sleva = 0.3
nova_cena_za_kus = cena_za_kus * (1 - sleva)

# Výpis informací
print(f"Název antikvariátu: {nazev_antikvariatu}")
print(f"Cena za jeden titul před slevou: {cena_za_kus} Kč")
print(f"Sleva: {sleva * 100}%")
print(f"Nová cena za jeden titul po slevě: {nova_cena_za_kus} Kč")


#---------------------------------------------Cvičení 3 Plánování svatby---------------------

cena_dospely = 990
cena_dite = cena_dospely * 0.5
celkovy_pocet_dospely = 60
celkovy_pocet_dite = 8
naklady = (cena_dospely * celkovy_pocet_dospely) + (cena_dite * celkovy_pocet_dite)
print(naklady)

nova_cena_dospely = 1000
nava_cena_dite = nova_cena_dospely * 0.5
nove_naklady = (nova_cena_dospely * celkovy_pocet_dospely) + (nava_cena_dite * celkovy_pocet_dite)
print(f'Po úpravě ceny pro dospělou osobu budou náklady na svatbu: {nove_naklady} kč')

#--------------------------------------------------Úlohy na doma  Hrátky s proměnnými -------------
holky = 15
klucy = 20
velikost_souboru = holky + klucy
print(f'Celkový počet lidí ve sboru: {velikost_souboru}')

mzda = 22392
mzdove_naklady = velikost_souboru * mzda
print(f'Měsíční náklady na platy ve sboru je: {mzdove_naklady} kč')

nazev_predstaveni = 'Avatar'
cena_vstupenky = 150
sleva_dite = 0.25
dospely = 15
dite = 8
celkova_castka = (cena_vstupenky * dospely) + (dite * (cena_vstupenky * (1 - sleva_dite)))
print(f'Divadelní zisk na představení {nazev_predstaveni} je: {celkova_castka} kč')

print(f'Z důvodu příchodu 2 nových sboristů budou měsíční náklady {(velikost_souboru + 2) * mzda} kč')