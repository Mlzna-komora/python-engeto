# Smyčka WHILE
# VYKONÁVÁNÍ SKRIPTU DOKUD TO JE POTŘEBA

index = 1

while index < 6:
    print("Ještě nemáš 6, ale ", index, ", pokračuji...", sep="")
    index = index + 1

print("Hotovo, máš 6!")

index = 0

while index < 5:
    print("index", index)
    index += 1

print("Splněno")


index_1 = 0
while index_1 < 15:
    if index_1 % 2 == 0:
        print("index_1:", index_1)
    index_1 += 1

print("Sudá čísla")


index_2 = 0
while index_2 < 5 or index_2 == 10:
    print(f"Index_2: {index_2}")
    index_2 += 1
print("Konec")

# BREAK - ukončení jakmile se splní podmínka
znak = 1
while znak <= 6:
    print(f"index: {znak}")
    if znak == 4:
        print("Mám hodnotu 4")
        break
    znak += 1


# CONTINUE - přeskakování
symbol = 0

while symbol <= 19:
    symbol += 1
    if symbol % 2 == 0:
        continue
    print(f"index: {symbol}") # vynechává SUDÉ hodnoty


# ELSE & while
cislo = 0

while cislo < 5:
    print(f"index: {cislo}")
    cislo += 1
print("Pokračuji...") # Ale když chci dostat nějaké ohlášení, že došlo k nějaké situaci (např. dosažení čísla 5)



cislo_1 = 0

while cislo_1 < 5:
    print(f"index: {cislo_1}")
    cislo_1 += 1

else:
    print(f"index: {cislo_1} --> hodnoty jsou si rovny, ukončuji smyčku.")

print("Pokračuji...")


# NEKONEČNÁ ŘÍZENÁ SMYČKA
dotazovani = True

while dotazovani:
    odpoved = input("Zadej celé číslo od 1 do 5")
    if odpoved.isnumeric() and int(odpoved) in range(1, 6):
        print("Výborně")
        dotazovani = False # tímto ukončuji smyčku, když uživatel zadá správný vstup
    else: 
        print("Špatná hodnota, zkus to znovu:)")