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

prihlas_jmeno = input("Zadej přihlašovací jméno: ")
heslo = input("Zadej heslo: ")

if prihlas_jmeno in uzivatele:
    if heslo in uzivatele.values():
        print("Zatím dobrý") # ještě ošetřit heslo 
    else:
        print("Šptané heslo")
else:
    print("Neregistrovaný uživatel")
    quit()