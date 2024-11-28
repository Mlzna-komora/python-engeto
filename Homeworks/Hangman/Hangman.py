# HANGMAN
import random
import slova
from grafika import obesenec

zivoty = 7
hra_bezi = True
slovo = random.choice(slova.hadana_slova)
tajenka = len(slovo) * ["_"]


while hra_bezi and zivoty > 0:
    print(f"Tajenka: {" ".join(tajenka)}; životy: {zivoty}",
          obesenec[7 - zivoty],
          sep="\n"
          )
    hadani = input("Hádej písmeno/slovo: ")

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


