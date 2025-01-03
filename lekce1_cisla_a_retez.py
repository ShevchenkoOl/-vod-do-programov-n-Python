'''
Základní příkazy v terminálu

python --version - zobrazí verzi v terminálu;
python nazev souboru.py (python test.py) - spustí soubor v terminálu;
exit() - vymaže terminál;
print (2+2) - zobrazí výsledek v terminálu;

Středník (;) je volitelný na konci výrazu v Pythonu. V Pythonu se k oddělení příkazů používají zalomení řádků. Pokud však chcete na jeden řádek uvést více příkazů, můžete použít středník. Příklad: print(2 ** 8); print("Hello, World!")

'''

#----------------------------------------Lekce 1 Čísla a řetězce-----------------------------------
'''
Aritmetické operátory
sčítání: +
odčítání: -
násobení: *
dělení: /
mocnění: **                возводит в степень 2 ** 3 (2 в 3 степени) zvyšuje na sílu 2 ** 3 (2 na 3)
celočíselné dělení: //     делит числа без остатка 7 // 2 = 3
zbytek po dělení: %        vzít zbytek dělení 7 / 2, abyste dostali celé číslo 3 a zbyde nám 1 (2*3=6 7-6=1)

print(f'studentské vstupné činí {koruny} kč') - F-řetězce (formátované řetězce) umožňují vložit hodnoty proměnných přímo do řetězce bude to na lekce 4
print("Divadlo Pěst na oko \n",  "Vítejte v online rezervaci vstupenek \n", "Pro vstup do systému je potřeba registrace \n")
'''
# print("Hello, World!")
# print(12 * 13 + 10)

# a = 12
# b = 13
# print(a ** b)

# print(7 / 2)
# print(7 // 2)
# print(7 % 2)

# print(3.14)  # 3.14 desetinná čísla vždycky píší s tečkou, nikoliv s čárkou.
# print(3,14)  # 3 14

# print('12. března 2018')
# print("prací prášek")
# a = '12. března 2018'
# print(a)       
# print('martin' + ' ' + 'podloucký') # martin podloucký 
# print('bla ' * 10)                  # bla bla bla bla bla bla bla bla bla bla
# print('bla\10' * 10)                # bla
                                      # bla
                                      # bla 
                                      # bla 
                                      # bla
                                      # bla
                                      # bla
                                      # bla
                                      # bla
                                      # bla


#----------------------------------Cvičení 1 Jednoduchá aritmetika----------------------------------
print(12*174*15) # plna cena
print((12*0.65)*(174//2)*15) # cena se slevou
print((12*(174//2)*15)-((12*0.65)*(174//2)*15)) # rozdil cen

#--------------------Variant 2
# ticket = 12
# spectators = 174
# performances = 15
# print('měsíční příjem divadla ze vstupného přichází je ' + str(ticket * spectators * performances) + ' eur') # Funkce str() se používá k převodu čísla na řetězec před zřetězením

# #pokud víme, že polovina návštěvníků jsou studentky a studenti
# total = (ticket * (spectators//2) * performances) + (0.65 * ticket * (spectators//2) * performances) # Dělení používáme beze zbytku //, protože pokud celkový počet není sudý, můžeme získat pulku osoby, a to není správné.
# print(f"Spolu se slevou pro studenty byly měsíční výdělky divadla: {total} eur")   # pokud použijeme vložení {...} uprostřed řádku, pak by před uvozovkami mělo být f v poslušném pořadí

# #----------------------------------Cvičení 2 Hrátky s řetězci--------------
print('Národní divadlo')
print('Národní ' + 'divadlo')
print('Národní divadlo ' * 3)
result = '1' * 256 + '0' * 256
print(result)
print('1' * 256 + '0' * 256)

#----------------------------------Cvičení 3 Shannonovo číslo
shannon_number = 10 ** 123
print("1" + "0" * 120)
print("1" + "000 " * 41)

# --------------------Variant 2
# print(str(shannon_number))   #1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#print(f'{shannon_number:,}') #1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000
#print('{:,}'.format(shannon_number))
#Oba přístupy mají své výhody a lze je použít v závislosti na kontextu a preferencích. Ve většině případů jsou f-řetězce modernější a čitelnější syntaxí pro formátování řetězců v Pythonu.