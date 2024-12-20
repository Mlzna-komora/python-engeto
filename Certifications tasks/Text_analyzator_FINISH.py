"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kateřina Volšičková
email: slunecnice.kd@seznam.cz
"""

'''
author =
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
else:
  print("Unregistered user, terminating the program..")
  quit()

print(cara)

vyber_textu = input("Enter a number btw. 1 and 3 to select: ")

print(cara)

if not vyber_textu.isdigit() or int(vyber_textu) >= 4:
  print("The selected value is not a digit or does not match the available texts .")
  quit()

#if int(vyber_textu) >= 4:
#  print("The selected number does not match the available texts.")
 # quit()
#else:
#  print("K analýze byl zvolený text: ", vyber_textu)

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

if int(vyber_textu) == 1:
  text_1 = TEXTS[0]
  #print(text_1)
elif int(vyber_textu) == 2:
  text_2 = TEXTS[1]
  #print(text_2)
elif int(vyber_textu) == 3:
  text_3 = TEXTS[2]
  #print(text_3)


# Analýza vybraného textu:

# 1: Počet slov
pocet_slov = len(text_1.split())
print(f"There are {pocet_slov} words in the selected text.")

# Počet slov začínajících velkým písmenem
slova_s_velkym = 0

for slovo in text_1.split():
  if slovo.istitle():
    slova_s_velkym += 1
print(f"There are {slova_s_velkym} titlecase words.")


# Počet slov psaných velkými písmeny
velka_slova = 0

for slovo in text_1.split():
  if slovo.isupper() and slovo.isalpha():
    velka_slova += 1
print(f"There are {velka_slova} uppercase words.")


# Počet slov psaných malými písmeny
mala_slova = 0

for slovo in text_1.split():
  if slovo.islower():
    mala_slova += 1
print(f"There are {mala_slova} lowercase words.")


# Počet čísel (ne cifer)
cisla_pocet = 0
cisla_v_textu = []

for slovo in text_1.split():
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

vycistena_slova = [] # nastavuji prázdný list

for slovo in text_1.split(): # budu iterovat list rozsekaných slov, split tvoří list!
    ciste_slovo = slovo.strip(".,<>") # fce strip ořízne všechny znaky, které vypíšu v závorce
    vycistena_slova.append(ciste_slovo.lower()) # fce append pridava do listu - do prázdného listu vyčištěná slova přidá očištěná slova (proměnná ciste_slovo)

#print(vycistena_slova)

# Udělat slovník/list s delkou slov a jejich četností
slovnik = {}

for slovo in vycistena_slova:
  delka = len(slovo) 
  if delka in slovnik:
    slovnik[delka] += 1
  else:
    slovnik[delka] = 1


# seřazení slovníku podle klíčů

serazeni_klicu = sorted(slovnik.keys())
#print(serazeni_klicu)
serazeni_slovniku = dict(sorted(slovnik.items())) # key: value - uspořádány podle klíčů od nejmenšího po největší
#print(serazeni_slovniku)


print(cara)
print("LEN|".center(4), "OCCURENCES".center(15), "|NR.".center(2))


print(cara)
# varianta se sorted()
for index, cetnost in enumerate(serazeni_slovniku, 1):
    hvezdicka = "*" * slovnik[cetnost]
    #print(f"{index}|".center(5), f"{hvezdicka}", f"|{slovnik[cetnost]}".center(20))
    print(f"{index:<3}| {hvezdicka:<15} |{slovnik[cetnost]:<60}")



#----------------------------------------
#LEN|  OCCURENCES  |NR.
#----------------------------------------
#  1|*             |1
#  2|*********     |9
#  3|******        |6
#  4|***********   |11
#  5|************  |12
#  6|***           |3
#  7|****          |4
#  8|*****         |5
#  9|*             |1
# 10|*             |1
# 11|*             |1


#=======================================================================================================





