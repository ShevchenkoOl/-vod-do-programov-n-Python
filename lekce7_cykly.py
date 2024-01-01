#-------------------------------------------------------Lekce 7 Cykly (FOR) ----------------------------------------------------------
'''
znamky = [1, 3, 2, 1, 1, 2]
for z in znamky:
    # c = z + 1
    print(z, end=", ") #end=" " - slouží k zobrazení výsledku na jednom řádku, uprostřed uvozovek označujeme, jak budou hodnoty odděleny


jmena = ['petr', 'pavel', 'jitka', 'jana']
for jmeno in jmena:
    mail = jmeno + '@gmail.com'
    print(mail)


znamky = [1, 3, 2, 1, 1, 2]
pocet_jednicek = 0
for z in znamky:
    if z == 1:
        pocet_jednicek = pocet_jednicek + 1
print("Počet jedniček:", pocet_jednicek)


soucet = 0                       #Tuto smyčku můžeme nahradit funkcí sum(), která je určena k výpočtu součtu prvků v sekvenci (seznam, n-tice atd.).
cisla = [2, 4, -1, 50, 0, 42, 3] #cisla = [2, 4, -1, 50, 0, 42, 3]
for cislo in cisla:              #total = sum(cisla)
    soucet = soucet + cislo      #print(total)
print("Součet:", soucet)
'''

#-----------------------------------------------------Cvičení 1 Seznam hodnocení ----------------------------------------------
hodnoceni = [7, 9, 6, 7, 9, 8]
for h in hodnoceni:
    new = str(h) + '/10' #aby program správně fungoval, musíme seznam převést na řetězec str()
    print(new)

#-----------------------------------------------------Cvičení 2 Procházení seznamu -------------------------------------------
hesla = [
    "xyz101",
    "punťa",
    "razor-blade",
    "1234",
    "12011986",
    "martin111",
    "trhnisi",
    "hokuspokus",
    "jeník15",
    "kristus-te-spasi",
    "beruška",
    "strčprstskrzkrk",
]

for heslo in hesla:
    if len(heslo) > 8:
        print(heslo)

# Druhou možností je vyřešit tento problém pomocí prázdného seznamu
bezpecni_hesla = []
for h in hesla:
    if len(h) >= 8:
        bezpecni_hesla.append(h)
        #print(bezpecni_hesla)  #když necháme výstup (print()) na této úrovni, pak program vypíše nový seznam pokaždé, když je přidán
print(bezpecni_hesla)           # na této úrovni - program zapíše nový seznam jednou, při přidávání všech prvků seznamu

# Třetí možnost je vyřešit tento problém pomocí generátoru seznamů (list comprehension)
bezpecni_hesla = [h for h in hesla if len(h) >= 8]
print(bezpecni_hesla)

#-----------------------------------------------------Cvičení 3 Složitější seznam ---------------------------------------------
mesice = [
    ["leden", 31],
    ["únor", 28],
    ["březen", 31],
    ["duben", 30],
    ["květen", 31],
    ["červen", 30],
    ["červenec", 31],
    ["srpen", 31],
    ["září", 30],
    ["říjen", 31],
    ["listopad", 30],
    ["prosinec", 31],
]
for m in mesice:
    print(m[0], end=",")

for m in mesice:
    print(m[1], end=",")

# Druhou možností
for m in mesice:
    print(m[0]) #po iteraci seznamem přiřadíme názvu měsíce index 0, to znamená, že bude na prvním místě v novém seznamu

for m in mesice:
    print(f"{m[0]}: {m[1]} dní")

#-----------------------------------------------------Cvičení 4 Hry ------------------------------------------------------
hry = [
    ["Ňadro na ňadru na nádru", 180],
    ["Útok plyšových krokodýlů", 95],
    ["Cesta do říše zelí", 128],
    ["Romance na zdymadle", 144],
    ["Zátiší s mimozemšťanem", 135],
    ["Čtyři facky a dortík", 100],
    ["Motorová okurka", 165],
    ["Johnny Noir", 140],
    ["Pražská kavárna vrací úder", 130],
    ["Pět sester ve vratech", 111],
    ["Stařec a krajta", 187],
    ["Růžová nemoc", 210],
    ["Smrt v přímém přenosu", 265],
]
print('seznam všech her: ')
for h in hry:
    print(h[0])

print('seznam her, které trvají více než 120 minut: ')
for h in hry:
  if h[1] >= 120:
   print(h)

print('seznam her, spolu s jejich trváním v hodinách a minutách: ')
for h in hry:
    hod = h[1] // 60
    min = h[1] % 60
    print(f'{h[0]}, trva: {hod} hod., {min} min.')

#-----------------------------------------------------Cvičení 5 Průměr ------------------------------------------------

numbers = [
    10.5,
    54.2,
    37.89,
    789.321,
    1.2,
    4.5
]                       # Může to být chyba v rozhodnutí, že začneme počítat průměrnou hodnotu v cyklu FOR
prumer = 0              # nejprve každý prvek, a pak vypočítáme průměrnou hodnotu
for number in numbers:
    prumer += number
prumer = round((prumer / len(numbers)), 2) #zaokrouhleme výsledek na 2 desetinná místa
print(prumer)

#-----------------------------------------------------Cvičení 6 Největší prvek-----------------------------------------
cisla = [
    15,
    4,
    65,
    12,
    98,
    4,
    18
]
max_cislo = cisla[0] # deklarovat proměnnou, která bude porovnána s ostatními prvky seznamu, obvykle se jedná o první prvek seznamu
for c in cisla:
    if c > max_cislo:
        max_cislo = c
print(max_cislo)