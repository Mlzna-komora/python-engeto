# Hádání tajného 4-ciferného čísla


"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Kateřina VOlšičková
email: slunecnice.kd@seznam.cz
"""


import random
from string import digits


print("Zdravím tě!")

cara = "-" * 40

print(cara)
print("Vygenerovala jsem pro tebe 4 random číslice.")
print("Pojďme si zahrát bulls & cows hru.")
print(cara)

#hadani_cisla = input("Zadej číslo: ")


#TODO: Vytvoření random 4-ciferného čísla (číslice unikátní a nesmí začínat 0)
# ošetření, že číslo je dlouhé 4 znaky, neobsahuje číselné znaky, atd

def tvorba_cisla():
    while True:
        generovani_cisla = random.sample(range(10), 4) # tuple
        if generovani_cisla[0] == 0:
            print("číslo začíná 0, generuji nové.")
        else:
            break

    unikatni_cislo = int("".join(map(str, generovani_cisla))) # int
    #print(f"Číslo v pořádku: {unikatni_cislo}")
    return unikatni_cislo

#print(tvorba_cisla())
tvorba_cisla()



#def hadani_cisla(zadane_cislo: int) -> int:
#    zadane_cislo = int(input("Zadej 4-místné číslo: "))
#    if zadane_cislo != 4:
#        print("Nezadal jsi 4-ciferné číslo.")
#    if not zadane_cislo.isdigit():
#        print("Nezadal jsi číslo.")
#
#    return zadane_cislo















