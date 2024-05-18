#---------------------------------------------Lekce 5 Podmínky ----------------------------------------------

#-----Porovnávací operátory
'''
rovno: ==  #jedno rovná se už používáme k přiřazení hodnoty do proměnné
nerovno: !=
větší: >
větší nebo rovno: >=
menší: <
menší nebo rovno: <=
'''
'''
vek = input('Zadejte prosím svůj věk: ')
vek = int(vek)
'''
'''
if vek >= 15: # Blok vždy začíná dvojtečkou na konci předchozího řádku. Tím říkáme k jaké konstrukci (v našem případě if) náš blok příkazů patří.
    print('Vítej na představení')
else:
    print('Dnes to není pro tebe') # budeme držet oficiálního doporučení autorů Pythonu a používat čtyři mezery na odsazení.
'''
#------Podmínky s více větvemi
'''
if vek < 6:
    print('Předškolák')
elif vek < 15:
    print('Školák')
elif vek < 18:
    print('Mladistvý')
else:
    print('Dospělý')
'''

#---------------------------------------------------Cvičení 1 Jednoduché podmínky ---------------------------------------------

import getpass # Tento modul umožňuje zadat heslo bez jeho zobrazení v konzole

jmeno = input('Zadejte své jméno: ')
heslo = input('Zadejte heslo: ') #getpass.getpass() vrací řetězec a zde není vyžadována žádná další konverze na řetězec (heslo = str(heslo))
# heslo = getpass.getpass('Zadejte heslo: ')
if  heslo.lower() != 'simsalabim': # .lower() - metoda, která umožňuje převést řetězec na malá písmena a .upper() - velká
    print('Vstup nepovolen')
    exit()
else: 
    age = input('Zadejte prosím svůj věk: ')
    age = int(age)
    if  age >= 18:
        print('Uživateli ' + jmeno + ' vstup povolen')
    else:
        print('Vstup povolen od 18 let')
    exit()
   
#---------------------------------------------------Cvičení 2 Cena vstupenky --------------------------------------------------------------

# print('Divadlo Pěst na oko')
# print('Vítejte v online rezervaci vstupenek')
# age = input('Zadejte své vek: ')
# age = int(age)
# plna_cena = 12

# if age < 6:
#     cena = 0
#     print(f'Cena vstupenky {cena} Kč')
# elif age <= 26:  # nebo 6 <= age <= 26
#     cena = round(plna_cena * 0.65)
#     print(f'Jste žák nebo student. Cena vstupenky {cena} Kč')
# elif age <= 64: 
#     cena = plna_cena
#     print(f'Jste dospělý. Cena vstupenky {cena} Kč')
# else:
#     cena = round(plna_cena * 0.5)
#     print(f'Jste senior. Cena vstupenky {cena} Kč')

#---------------------------------------------------Cvičení 3 Registrace --------------------------------------------------------

# jmeno = input('Zadejte své jméno: ')
# heslo1 = input('Zadejte heslo: ')
# heslo1 = str(heslo1)
# heslo2 = input('Zopakujte prosím své heslo: ')
# heslo2 = str(heslo2)
# if  heslo1 != heslo2:
#     print('Omlouváme se, vstup nepovolen, zadal jste jiná hesla')
#     exit()
# elif len(heslo1) < 8:
#      print('Vaše heslo není bezpečné, zkuste to prosím znovu')
# else:
#     print(f'{jmeno}, gratulujeme k úspěšné registraci')   

#---------------------------------------------------Cvičení 4 Přestupný rok -----------------------------------------------------

# rok = input('Zadejte prosím rok, který chcete zkontrolovat: ')
# rok = int(rok)
# if rok % 4 == 0:
#     if rok % 100 == 0:
#         if rok % 400 == 0:
#             print('Rok je přestupný')
#         else:
#             print('Rok není přestupný')
#     else:
#         print('Rok je přestupný')
# else:
#     print('Rok není přestupný')

#---------------------------------------------------Čtení na doma: Vícenásobné podmínky---------------------------------------------
#------------------------------------------------------Dělitelnost více čísly-------------------------------------------------------
'''
number = input('Zadejte prosím celé číslo: ')
number = int(number)
if number % 3 == 0 and number % 4 == 0: # Můžete zadat dvě podmínky buď v závorkách, nebo bez nich
    print('Vaše číslo je zároveň dělitelné 3 a 4')
else:
    print('Vaše číslo neni zároveň dělitelné 3 a 4')
'''
#---------------------------------------------------------Gymnázium-----------------------------------------------------------------
'''
znamka = input('Zadejte známky z matematiky: ')
znamka = int(znamka)
stredni = input('Zadejte průměru všech známek na posledním vysvědčení: ')
stredni = float(stredni) # Může být float(), pokud jsou vstupem čísla s pohyblivou řádovou čárkou
if stredni <= 1.8 and znamka <= 2:
    print('Přijmeme vás bez přijímací zkoušky')
else:
    print('Musíte splnit přijímací zkoušku.')
'''

#------------------------------------------------------------------Gymnázium 2 ---------------------------------------------------------
'''
znamka = input('Zadejte známky z matematiky: ')
znamka = int(znamka)
stredni = input('Zadejte průměru všech známek na posledním vysvědčení: ')
stredni = float(stredni)
if znamka > 2:
    test = input("Zúčastnil ses okresního kola krajské olympiády? [a/n] ") #nebo test = input("Zúčastnil ses okresního kola krajské olympiády? [a/n] ").lower() == a
    test = test.lower() == 'a'
    if test and stredni <= 1.8:       
        print('Přijmeme vás bez přijímací zkoušky')
    else:
        print('Musíte splnit přijímací zkoušku.')
else:
    print('Musíte splnit přijímací zkoušku.')
'''
#---------------------------------------------------------------Ruleta-------------------------------------------------------------
'''
cislo = input('Zadejte celé číslo: ')
cislo = int(cislo)

if (1 <= cislo <= 10 and 19 <= cislo <= 28) or (11 <= cislo <= 20 and 29 <= cislo <= 35):
    if cislo % 2 == 0:
        print('číslo je černé')
    else:
        print('číslo je červené')
elif 0 <= cislo <= 36:
    if cislo == 0:
        print('číslo je zelené')
    elif cislo % 2 == 0:
        print('číslo je červené')
    else:
        print('číslo je černé')
else:
    print('Neplatné číslo')
'''
#---------------------------------------------------------------Soutěž-------------------------------------------------------------
'''
print('Divadlo Pěst na oko pořádá soutěž o lístky na premiéru nového představení Zločin v podmínce.')
clen = input("Jste členem klubu? [a/n] ").lower() == 'a'
if clen:
    print('Gratulujeme, účastníte se soutěže!')
else:
    sdilel = input('Kolik příspěvků jste přidali na sociální sítě? ')
    sdilel = int(sdilel)
    navsteni = input('Kolikrát jste letos divadlo navštívili? ')
    navsteni = int(navsteni)
    if sdilel >= 5 and navsteni >= 5:
        print('Gratulujeme, účastníte se soutěže!')
    else: print('Bohužel se nemůžete zúčastnit soutěže')
'''
