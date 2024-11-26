# Vytvořit program, který uživateli umožní vybrat ze zadaných hodnot
ovoce = ("jablko", "banan", "citron", "pomeranc")
print("Dostupné ovoce: ", ", ".join(ovoce))

while True:
    vyber = input("vyber z dostupnaho ovoce:".upper())
    if vyber not in ovoce:
        print("Ovoce není v nabídce.")
    else:
        print("Bezva, toto ovoce je v nabídce.")
        break
