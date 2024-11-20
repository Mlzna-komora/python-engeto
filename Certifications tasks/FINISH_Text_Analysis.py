"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kateřina Volšičková
email: slunecnice.kd@seznam.cz
"""

'''
author = Kateřina Volšičková
'''

# tady bude začínat tvůj kód:
print("$ python projekt1.py")

cara = "-" * 40

# Vyžádání JMÉNA a HESLA:
uzivatelska_jmena = ["bob", "ann", "mike", "liz"] # list
hesla = ["123", "pass123", "password123", "pass123"] # list

prihlas_jmeno = input("username: ")
heslo = input("password: ")

if prihlas_jmeno in uzivatelska_jmena:
  index = uzivatelska_jmena.index(prihlas_jmeno) # oindexovala jsem oba listy a dala jsem, že jediná správná volba je, pokud se indexy v obou listech rovnají
  if hesla[index] == heslo:
    print(cara)
    print(f"Welcome to the app, {prihlas_jmeno}!")
    print("We have 3 texts to be analyzed.")
  else:
    print("Wrong password.")
    quit()
else:
  print("Unregistered user, terminating the program..")
  quit()

print(cara)

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


vyber_textu = input("Enter a number btw. 1 and 3 to select: ")

print(cara)

if not vyber_textu.isdigit() or not (1 <= int(vyber_textu) <= 3):
  print("The selected value is not a digit or does not match the available texts .")
  quit()

vybrany_text = TEXTS[int(vyber_textu) - 1]


# ANALÝZA VYBRANÉHO TEXTU
# Počet slov
pocet_slov = len(vybrany_text.split())
print(f"There are {pocet_slov} words in the selected text.")


# Počet slov začínajících velkým písmenem
slova_s_velkym = 0

for slovo in vybrany_text.split():
  if slovo.istitle():
    slova_s_velkym += 1
print(f"There are {slova_s_velkym} titlecase words.")


# Počet slov psaných velkými písmeny
velka_slova = 0

for slovo in vybrany_text.split():
  if slovo.isupper() and slovo.isalpha():
    velka_slova += 1
print(f"There are {velka_slova} uppercase words.")


# Počet slov psaných malými písmeny
mala_slova = 0

for slovo in vybrany_text.split():
  if slovo.islower():
    mala_slova += 1
print(f"There are {mala_slova} lowercase words.")


# Počet čísel (ne cifer)
cisla_pocet = 0
cisla_v_textu = []

for slovo in vybrany_text.split():
  if slovo.isdigit():
    cisla_pocet += 1
    cisla_v_textu.append(int(slovo))
print(f"There are {cisla_pocet} numeric strings.")

# Součet všech čísel
soucet_cisel_v_textu = sum(cisla_v_textu)
print(f"The sum of all the numbers {soucet_cisel_v_textu}.")


# SLOUPCOVÝ GRAF 
# slovo na 1 písmeno je v textu 1.
# ... slovo na 3 písmena je v textu 6.

# kolikrát je slovo na x písmen obsaženo v textu

vycistena_slova = [] # nastavuji prázdný list - PŘEVZATO Z DOMÁCÍHO ÚKOLU

for slovo in vybrany_text.split():
    ciste_slovo = slovo.strip(".,<>") # fce strip ořízne všechny znaky, které vypíšu v závorce
    vycistena_slova.append(ciste_slovo.lower()) # fce append pridava do listu - do prázdného listu vyčištěná slova přidá očištěná slova (proměnná ciste_slovo)


# Slovník s délkou slov a jejich četností
slovnik = {}

for slovo in vycistena_slova: # Výpočet četnosti podle délky slov
  delka = len(slovo) 
  if delka not in slovnik:
    slovnik[delka] = 0
  slovnik[delka] += 1


max_delka = max(slovnik.keys()) # Nejdelší slovo
for delka in range(1, max_delka + 1):
  if delka not in slovnik:
    slovnik[delka] = 0


serazeni_slovniku = dict(sorted(slovnik.items())) # key: value - uspořádání podle klíčů od nejmenšího po největší
#print(serazeni_slovniku) - jen kontrola

print(cara)

print("LEN|".center(4), "OCCURENCES".center(18), "|NR.".center(4))

print(cara)
# varianta se sorted()
for index, cetnost in enumerate(serazeni_slovniku, 1):
    hvezdicka = "*" * slovnik[cetnost]
    print(f"{index:<3}| {hvezdicka:<18} |{slovnik[cetnost]:<80}")