from collections import Counter
import math
import os


# vypsání nabídky
def nabidka():
    operace = ["+", "-", "*", "/", "avg", "sum", "pow","gcd", "scm", "quit"]
    spojeni = " | ".join(operace)
    cara = "-" * len(spojeni)
    print(cara, spojeni, cara, sep="\n")  
#nabidka()

# KALKULAČKA

def kalkulacka() -> str:
     """
    Main function
    """
    while True:
        nabidka()
        vyber_operace = input("vyber operaci: ")
        os.system("cls")

        if vyber_operace == "quit":
            print("Good bye!")
            break
        elif vyber_operace == "avg":
            vypocti_prumer()
        elif vyber_operace == "pow":
            vypocti_umocneni()
        elif vyber_operace == "sum":
            vypocti_soucet()
        elif vyber_operace == ("+", "-", "*", "/"):
            aritmeticke_operatory()
        elif vyber_operace == "gcd":
            vypocti_gcd()
        elif vyber_operace == "scm":
            vypocti_scm()
        else:
            print("Neplatná volba, zkus to znovu.")
kalkulacka()


# Průměr
def vypocti_prumer():
    list_cisel = []
    while True:
        cislo = input("Zadej číslo (nebo '=' pro ukončení): ")
        if cislo == "=":
            break
        else:
            list_cisel.append(float(cislo))
    vysledek = sum(list_cisel)/len(list_cisel)
    print(vysledek)
    return vysledek
#vypocti_prumer()


# Umocňování
def vypocti_umocneni() -> int:
    cislo = int(input("Zadej číslo: "))
    mocnina = int(input("Zadej mocninu: "))
    vysledek = cislo**mocnina
    print(vysledek)
vypocti_umocneni()


# Součet
def vypocti_soucet():
    list_cisel = []

    while True:
      cislo = input("Zadej číslo: . (nebo '='pro ukončení): ")
      if not cislo.isnumeric() or cislo == "=":
        break
      else:
          list_cisel.append(float(cislo))

    vysledek = sum(list_cisel)
    print(vysledek)
    return vysledek
#vypocti_soucet()


# Nejvyšší společný dělitel
def vypocti_gcd():
    a = int(input("Zadej první číslo: "))
    b = int(input("Zadej druhé číslo: "))
    vysledek = math.gcd(a, b)
    print(f"Největší společný dělitel: {vysledek}")
    return vysledek


# Nejmenší společný násobek
def vypocti_scm():
    a = int(input("Zadej první číslo: "))
    b = int(input("Zadej druhé číslo: "))
    gcd = math.gcd(a, b)
    vysledek = abs(a * b) // gcd
    print(f"Nejmenší společný násobek: {vysledek}")
    return vysledek


# Základní aritmetické operátory
# Zadej číslo nebo operátor, "=" pro výsledek:

def aritmeticke_operatory() -> None:
    vstup = ""

    while True:
        tlacitko = input("Zadej číslo nebo operátor, '=' pro výsledek: ")

        if tlacitko.isnumeric() or tlacitko in ("+", "-", "*", "/"):
            vstup = vstup + tlacitko
        elif tlacitko == "=":
            print(f"{vstup} = {eval(vstup)}")
            break
#aritmeticke_operatory()





