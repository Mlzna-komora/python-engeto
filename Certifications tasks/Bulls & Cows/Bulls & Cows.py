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

print(cara)


#TODO: Vytvoření random 4-ciferného čísla (číslice unikátní a nesmí začínat 0)
# ošetření, že číslo je dlouhé 4 znaky, neobsahuje číselné znaky, atd

def hadani_cisla():
    generovani_cisla = random.sample(range(10), 4)
    unikatni_cislo = int("".join(map(str, generovani_cisla)))
    #if unikatni_cislo == 4:
    #    print(unikatni_cislo)

    return unikatni_cislo

print(hadani_cisla())














