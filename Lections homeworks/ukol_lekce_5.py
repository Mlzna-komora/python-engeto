# Program, který udává slova, která mají délku 4 znaky, jakmile uloží 3 taková slova, skončí¨
slova = []
slovo = input("Zadej slovo")

if len(slovo) == 5:
    slova.append(slovo)
    if slovo == slova:
        print(f"Slovo {slovo} už je uložené.")
    else:
        print(f"Slovo není dlouhé 4 znaky")
#print(f"Už mám uložené tři slova.")

