mesta = ["Praha", "Vídeň", "Olomouc", "Svitavy", "Zlín", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
slevy = ('Olomouc', 'Svitavy', 'Ostrava')
domeny = ('gmail.com', 'seznam.cz', 'email.cz')
dvojita_cara = '=' * 35
cara = "-" * 35
nabidka = """
1 - Praha   | 150,- Kč
2 - Vídeň   | 200,- Kč
3 - Olomouc | 120,- Kč
4 - Svitavy | 120,- Kč
5 - Zlín    | 100,- Kč
6 - Ostrava | 180,- Kč
"""

AKT_ROK = 2021

print("VÍTEJTE V NAŠÍ APLIKACI DESTINATIO!")

print(dvojita_cara)
print(nabidka)
print(dvojita_cara)

destinace_cislo = int(input('Vyber číslo destinace: '))
jmeno = input("Jméno: ")
prijmeni = input("Příjmení: ")
email = input("e-mail: ")


cilova_stanice = mesta[destinace_cislo-1]
finalni_cena = ceny[destinace_cislo-1]


if 1 <= destinace_cislo <= 6:
    print(cilova_stanice)
    print(finalni_cena, ",-Kč")
else:
    print('Destinace číslo ' + str(destinace_cislo) + 'NEEXISTUJE')
    quit()

print(cara)
