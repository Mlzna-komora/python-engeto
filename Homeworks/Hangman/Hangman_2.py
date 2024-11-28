# HANGMAN
import slova
import random
from grafika import obesenec


zivoty = 7
hra_bezi = True
slovo = "obesenec"
tajenka = len(slovo) * ["_"]

# mohu si definovat fci
while hra_bezi and zivoty > 0:
    print(f"Tajenka: {" ".join(tajenka)}; životy: {zivoty}",
          obesenec[7 - zivoty],
          sep="\n"
          )
    hadani = input("Hádej písmeno/slovo: ")

# CHCI: aby se do tajenky vypsalo uhádnuté písmenko

def vymen_pismeno(slovo, tajenka, index):
    pismena = list(slovo) # převedení slova na list
    print(type(pismena))
    #if index < len(pismena) and index < len(tajenka):
    pismena[index] = tajenka[index][0]
    #else:
    print("Index je mimo rozsah nebo seznam je prázdný.")
    return "".join(pismena)


for index, pismeno in enumerate(slovo):
    print(f"Index: {index}, Pismeno: {pismeno}")

print(tajenka)
tip = input("Hadej pismeno/slovo:")

if hadani == slovo:
    print(f"Tajenka: {slovo}")
    print("Vyhrál jsi! Gratuluji...")
    hra_bezi = False
elif len(hadani) == 1 and hadani in slovo:
    print("Uhodl jsi písmeno!")
    print()
else:
    zivoty = zivoty - 1
    print("chyba!")
    print(f"")
    while zivoty == 0:
        print(f"Prohrál jsi :( snad příště)", f"Hledané slovo: *{slovo}*", sep="\n")
        print(obesenec[7 - zivoty])
        break