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

# Ověření, zda zadané číslo destinace je v rozmezí platných indexů
if destinace_cislo < 1 or destinace_cislo > len(mesta):
    print('Destinace číslo', destinace_cislo, 'neexistuje!'.upper())
    quit()

cilova_stanice = mesta[destinace_cislo - 1]
finalni_cena = ceny[destinace_cislo - 1]
finalni_cena_sleva = ceny[destinace_cislo - 1] * 0.75

print(cilova_stanice.upper())
#print(finalni_cena, ",-Kč")

# pokud bude zadaná destinace bude v seznamu slev - napsat: Získáváte 25 % slevu! Nová cena:...
if cilova_stanice in slevy:
    nova_cena = 0.75 * ceny[destinace_cislo - 1]  # snížení ceny o 25 %
    print('Získáváte slevu 25 %! Nová cena: ', finalni_cena_sleva, ' Kč')
else:
    print('Jízdenka bez slevy. Cena: ', finalni_cena, ",-Kč")

print(cara)


# Vyplnit celé jméno, ale pracovat jen s křestním

cele_jmeno = input('Vaše celé jméno: ')
krestni_jmeno = cele_jmeno.split()[0]

if krestni_jmeno.isalpha(): # Kontrola, zda jméno obsahuje pouze alfabetické znaky
    print('Křestní jmeno: ', krestni_jmeno)
else:
    print('Neplatné jméno!')

print(cara)


# Omezení věkem

rok_narozeni = int(input('Váš rok narození: '))
#if rok_narozeni < 2006: - je to správně, ale bez použití aktivního roku
if (AKT_ROK - rok_narozeni) >= 18:
    print('Přístup povolen...')
else:
    print('Jste příliš mladý na nákup jízdenek!')
    print('Ukončuji program')
    quit()

print(cara)


# Validní email - pokud je domena e-mailu v seznamu domén
#domeny = ('gmail.com', 'seznam.cz', 'email.cz') - TUPLE

email = input('Napiště Vaši emailovou adresu: ')
email_domena = email.split('@')[-1]

if email_domena in domeny:
    print('Ověření emailu proběhlo v pořádku.')
else:
    print('Tento email je neplatný!')
    print('Ukončuji program')

print(dvojita_cara)

print('Děkuji, ', krestni_jmeno, ' za objednávku jízdenky.')
print('Cílová destinace: ', cilova_stanice, ', cena jízdného: ', nova_cena, ',-')
print('Na Váš email: ', email, ' jsme odeslali e-jízdenku.')

print(dvojita_cara)
