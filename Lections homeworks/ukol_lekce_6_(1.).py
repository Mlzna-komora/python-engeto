# HRA KÁMEN, NŮŽKY, PAPÍR
import random

moznosti = ["kamen", "nuzky", "papir"]
hrac = "kamen"
print(hrac)
pocitac = random.choice(moznosti)
print(pocitac)
if pocitac == "nuzky":
    print("Vyhrál jsi!")
elif pocitac == "papir":
    print("Prohrál jsi :(")
elif pocitac == "kamen":
    print("Nerozhodně")
