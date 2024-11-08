mesta = ["Praha", "Vídeň", "Olomouc", "Svitavy", "Zlín", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """
1 - Praha   | 150,- Kč
2 - Vídeň   | 200,- Kč
3 - Olomouc | 120,- Kč
4 - Svitavy | 120,- Kč
5 - Zlín    | 100,- Kč
6 - Ostrava | 180,- Kč
"""

print("VÍTEJTE V NAŠÍ APLIKACI DESTINATIO!")

print(cara)
print(nabidka)
print(cara)

destinace = input("Napiš číslo destinace: ")
jmeno = input("Jméno: ")
prijmeni = input("Příjmení: ")
email = input("e-mail: ")

#print(cara)

#print("Číslo destinace: ", destinace)

print(cara)

cilova_stanice = mesta[int(destinace)-1]
finalni_cena = ceny[int(destinace)-1]

print(cilova_stanice)
print(finalni_cena, ",-Kč")

print(cara)

print("Cestující: ", jmeno , prijmeni)
print("Cílová destinace: ", cilova_stanice)
print("Cena jízdného: ", finalni_cena,",-Kč")
print("Jízdenku jsme odeslali na e-mail: ", email)