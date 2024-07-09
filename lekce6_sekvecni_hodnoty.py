#---------------------------------------------Lekce 6 Sekvenční hodnoty -----------------------------------------------------------
'''
jmeno = 'hubert'
print(jmeno[0])  # 'h'
print(jmeno[4])  # 'r'

uzivatele = ['mark', 'carl', 'eve', 'ellen']
print(uzivatele[1]) # carl
print(uzivatele[1] [2]) #r

body = [[140, 120], [60, 92], [34, 68]]
print(body[2]) #[34, 68]
print(body[2][0]) #34

jmeno = 'Hubert'

# indexujeme zleva od nuly
print(jmeno[2])
print(jmeno[4])
print(jmeno[0])

# zprava pomocí záporných od -1
print(jmeno[-1])
print(jmeno[-2])
# prvni tři hodnoty
print(jmeno[:3])
# poslední tři hodnoty
print(jmeno[-3:])

# do cisla indexovat nelze
# musíme si ho napřed převést na text
cislo = 1597862
cislo_text = str(cislo)
print(cislo_text[-4])
'''
#--------------------------------------------Cvičení 1 Řetězce jako sekvence-----------------------------------------------------
# name = 'Oleksii'
# print(name[3], name[5], name[6]) # k i i

#--------------------------------------------Cvičení 2 Seznamy------------------------------------------------------------------
# pocet = [56, 78, 14, 23, 1, 41, 5]
# # zaplnenost = [10.1, 1.2, 0.5, 14.5, 7.8]
# hry = ['Avatar', 'Leon king', 'Madagaskar', 'Milada', 'Cezar']
# druha_polozka = hry[1]
# print(druha_polozka)


hodnoceni = [
                ['The Times', 9], 
                ['Economist', 7], 
                ['Vecerka', 10], 
                ['Seznam.cz', 5]
            ]
print(f"Divadelna hra Plyšáci na útěku, v různých časopisech: {hodnoceni}")

#--------------------------------------------Cvičení 3 Ověřování hesla ----------------------------------------------------------
import random
heslo = 'czechitas'

symbol2 = input('Zadej 2. znak hesla: ')
symbol5 = input('Zadej 5. znak hesla: ')
symbol7 = input('Zadej 7. znak hesla: ')

if (symbol2.lower() == heslo[1]) and (symbol5.lower() == heslo[4]) and (symbol7.lower() == heslo[6]):
    print('Vstup povolen!')
else:
    print('Vstup zamítnut')
    
# req_random1 = random.randint(1, len(heslo))
# req_random2 = random.randint(1, len(heslo))
# req_random3 = random.randint(1, len(heslo))  # req_positions = random.sample(range(1, len(heslo)), 3) - Tato funkce umožňuje získat tři náhodná čísla od 1 do len(heslo))
# symbol1 = input(f'Zadej {req_random1} znak hesla: ')
# symbol2 = input(f'Zadej {req_random2} znak hesla: ')
# symbol3 = input(f'Zadej {req_random3} znak hesla: ')
# if (symbol1.lower() == heslo[req_random1-1]) and (symbol2.lower() == heslo[req_random2-1]) and (symbol3.lower() == heslo[req_random3-1]):
#     print('Vstup povolen!')
# else:
#     print('Vstup zamítnut')
    
# Pro správnější kontrolu hesla můžeme kromě kontroly velikosti písmen přidat metodu pro odstranění nadbytečných mezer .strip() (symbol2.strip().lower())
