#--------------------------------------------Lekce 4 Vstup a výstup-----------------------------------------
'''
kurz = 25
eur = input("Zadej pocet eur: ") #funkce input() vždy vrací řetězec
eur = int(eur) #funkci int() převádí řetězec na celé číslo
cena = kurz * eur
print(f"cena je: {cena} korun")
'''

#----------------------------------------Cvičení 1 Jednoduchý výstup-----------------------------------------
'''
nazev = 'Divadlo Pěst na oko'
#cas = '19:30'
#print(f'Představení {nazev} zacina v {cas}')
hod = 19
min = 30
print(f'Představení {nazev} zacina v {hod}:{min}')
'''
#----------------------------------------Cvičení 2 Jednoduchý vstup ------------------------------------------
'''
name = input('Zadejte své jméno: ')
surname = input('Zadejte své příjmení: ')
#print(f'Hello, {name} {surname}')
age = input('Zadejte své vek: ')
age = int(age)
print(f"Uživatel: {name} {surname} ma {age} let")
'''

#----------------------------------------Cvičení 3 Zakázka pro divadlo ----------------------------------------
'''
print('Divadlo Pěst na oko')
print('Vítejte v online rezervaci vstupenek')
print('Pro vstup do systému je potřeba registrace')
jmeno = input('Zadejte své jméno: ')
prijmeni = input('Zadejte své příjmení: ')
age = input('Zadejte své vek: ')
age = int(age)
print(f"Uživatel: {jmeno} {prijmeni} ma {age} let")
'''

#----------------------------------------Cvičení 4 Házení kostkami ---------------------------------------------
import random
print(random.randint(1, 6))

#----------------------------------------Cvičení 5 Generátor čísel ----------------------------------------------
'''
print('Program vytváří náhodné číslo ve vámi určeném intervalu')
number1 = input('zadejte prosím první číslo: ')
number1 = int(number1)
number2 = input('zadejte druhé číslo: ')
number2 = int(number2)
print(f'Náhodné číslo v intervalu od {number1} do {number2} bude: {random.randint(number1, number2)}')
'''
#------------------------------------------Čtení na doma-----------------------------------------------------------
cena = 25
print("Cena je", cena, "Kč.") #Pokud bychom z jakéhokoliv důvodu nechtěli použít f-stringy, můžeme jednotlivé informace oddělit čárkami
print("Cena je", cena, "Kč.", sep=" ") #sep="" nastavíme, jak oddělit slova mezerou, pomlčkou nebo něčím jiným 

print("hurá", end="! ") # end, nastavuje jak se má výpis funkcí print() ukončit. Ve výchozím nastavení je to znak nového řádku end='\n', ale toto chování můžeme upravit, aby nám například šlo vypsat více volání funkce print() na jeden řádek.
print("hurá", end="! ")
print("hurá", end="! ")
print() # print() bez argumentů přidá znak nového řádku a vytvoří nový řádek ve výstupu.

cena = str(cena) #převedeme číslo na řetězec
print("Cena je " + cena + " Kč.") #v horní podmínce jsme oddělili parametry čárkami

