from collections import Counter



def calculator() -> str:
    """
    Main function
    """
    print("Lets calculate!")

calculator()

# vypsání nabídky
def nabidka():
    operace = ["+", "-", "*", "/", "avg", "sum", "pow","gcd", "scm", "quit"]
    spojeni = " | ".join(operace)
    cara = "-" * len(spojeni)
    print(cara, spojeni, cara, sep="\n")


# KALKULAČKA
def kalkulacka():
    while True:
        nabidka()
        vyber_operace = input("vyber operaci: ")

        if vyber_operace == "quit":
            break
        elif vyber_operace == "avg":
            vypocti_prumer()
        elif vyber_operace == "pow":
            vypocti_umocneni()
        elif vyber_operace == "sum":
            vypocti_soucet()

kalkulacka()
            




# Průměr
def vypocti_prumer():
    list_cisel = []
    while True:
        cislo = input("Zadej číslo: ")
        if cislo.isinstance() and not cislo.isdigit():
            print("Nezadal jsi číslo nebo správný tvar.")
            continue
        else:
            list_cisel.append(int(cislo))
            vysledek = sum(list_cisel)/len(list_cisel)
            print(vysledek)
            break
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

    while (cislo := input("Zadej číslo: ")) != "=":
        if not cislo.isdigit():
            break

    list_cisel.append(int(cislo))
    vysledek = sum(list_cisel)
    print(vysledek)
vypocti_soucet()


# Nejvyšší společný dělitel



