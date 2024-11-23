# Program, který udává slova, která mají délku 4 znaky, jakmile uloží 3 taková slova, skončí¨
slova = set() # MNOŽINA

while len(slova) != 3:
    slovo = input("Zadej 1 slovo ze 4: ".upper())
    if slovo in slova:
        print(f"Slovo {slovo} už je uložené.")
    elif len(slovo) != 4:
        print(f"Slovo není dlouhé 4 znaky.")
    else:
        slova.add(slovo)

else:
    print(f"Už mám uložená tři slova.")

