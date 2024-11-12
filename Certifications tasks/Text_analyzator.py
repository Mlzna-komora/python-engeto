"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Kateřina Volšičková
email: slunecnice.kd@seznam.cz
"""
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

