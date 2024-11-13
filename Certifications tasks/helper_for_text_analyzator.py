vyber_textu = input("Enter a number btw. 1 and 3 to select: ")

if not vyber_textu.isdigit():
  print("Zadaná hodnota není číslice.")
  quit()

if int(vyber_textu) >= 4:
  print("Vybrané číslo neodpovídá dostupným textům.")
  quit()
else:
   print("K analýze byl zvolený text: ", vyber_textu)




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

# Počet slov

if int(vyber_textu) == 1:
  text_1 = TEXTS[0]
  print(text_1)

pocet_slov = len(text_1.split())
print(f"Počet slov v textu je: {pocet_slov}")


# Počet slov začínajících velkým písmenem
slova_s_velkym = 0

for slovo in text_1.split():
  if slovo.istitle():
    slova_s_velkym += 1
print(f"Počet slov začínajících velkým písmenem je: {slova_s_velkym}")


# Počet slov psaných velkými písmeny
velka_slova = 0

for slovo in text_1.split():
  if slovo.isupper() and slovo.isalpha():
    velka_slova += 1
print(f"Počet slov psaných velkým písmem je: {velka_slova}")


# Počet slov psaných malými písmeny
mala_slova = 0

for slovo in text_1.split():
  if slovo.islower():
    mala_slova += 1
print(f"Počet slov psaných malými písmeny: {mala_slova}")


# Počet čísel (ne cifer)
cisla_pocet = 0
cisla_v_textu = []

for slovo in text_1.split():
  if slovo.isdigit():
    cisla_pocet += 1
    cisla_v_textu.append(int(slovo))
print(f"Počet čísel je: {cisla_pocet}")
print(cisla_v_textu)

# Součet všech čísel
soucet_cisel_v_textu = sum(cisla_v_textu)
print(soucet_cisel_v_textu)



# SLOUPCOVÝ GRAF

vycistena_slova = [] # nastavuji prázdný list

for slovo in text_1.split(): # budu iterovat list rozsekaných slov, split tvoří list!
    ciste_slovo = slovo.strip(".,<>") # fce strip ořízne všechny znaky, které vypíšu v závorce
    vycistena_slova.append(ciste_slovo.lower()) # fce append pridava do listu - do prázdného listu vyčištěná slova přidá očištěná slova (proměnná ciste_slovo)

#print(vycistena_slova)

from collections import Counter

vyskyt_slov = {}
vyskyt_slov = Counter(vycistena_slova) # fce Counter automaticky vytváří slovník
print(vyskyt_slov) # OK



vyskyt_slov = {}
vyskyt_slov = Counter(vycistena_slova) # fce Counter automaticky vytváří slovník
print(vyskyt_slov) # OK