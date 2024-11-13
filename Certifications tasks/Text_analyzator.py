"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kateřina Volšičková
email: slunecnice.kd@seznam.cz
"""

'''
author =
'''



# tady bude začínat tvůj kód:

# Vyžádání JMÉNA a HESLA:

uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

uzivatelska_jmena = ["bob", "ann", "mike", "liz"] # list
hesla = ["123", "pass123", "password123", "pass123"] # list


prihlas_jmeno = input("Zadej přihlašovací jméno: ")
heslo = input("Zadej heslo: ")

if prihlas_jmeno in uzivatelska_jmena:
  index = uzivatelska_jmena.index(prihlas_jmeno) # oindexovala jsem oba listy a dala jsem, že jediná správná volba je, pokud se indexy v obou listech rovnají
  if hesla[index] == heslo:
    print(f"Zdravím tě, {prihlas_jmeno}!")
   # print(heslo)
  else:
    print("Špatné heslo, blbečku :(.")
    #opak_heslo = input("Chceš znovu zadat heslo?")
    #if opak_heslo == "ano".lower() or "jo".lower():
    #  heslo = input("Zadej heslo: ")
    #else:
    #  print("Nazdar bazar...")
else:
  print("Nejsi v seznamu uživatelů, hňupe.")
  quit()




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


if int(vyber_textu) == 1:
  text_1 = TEXTS[0]
  print(text_1)
elif int(vyber_textu) == 2:
  text_2 = TEXTS[1]
  print(text_2)
elif int(vyber_textu) == 3:
  text_3 = TEXTS[2]
  print(text_3)


# Analýza vybraného textu

# 1: POČET SLOV




