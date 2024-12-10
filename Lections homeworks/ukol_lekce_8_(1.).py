# IDENTIFIKACE ANAGRAMŮ
# anagramy = 2 a více slov složených ze stejných znaků (např. ship, hips)

def je_anagram(*args) -> bool:
    """
    Vrati boolean True, pokud jsou všechny parametry anagramy.
    Jinak vrátí False.

    Priklad:
    >>> print(je_anagram("ship", "hips", "hisp"))
    True
    >>> print(je_anagram_matous("ship", "hips", "duck"))
    False))
    """

    # z první hodnoty v sekvenci stanoví vzor, jehož písmena seřadí
    vzor = sorted(args[0]) # fce sorted přo třídění seznamů, řetězců, uteratovatelných objektů
    # sorted vrací nový tříděný seznam, aniž by měnila původní iterovatelný objekt

    for slovo in args:
        if sorted(slovo) != vzor:
            return False
    else:
        return True
    
print(
    je_anagram("ship", "hips", "hisp"), # True
    je_anagram("ship", "hips", "duck"), # False
    sep="\n"
)

# ---------------------------------------------------------------------------------------------------

# Vytvoř program, který ze zadaného listu vytáhne emaily, které obsahují čísla
adresy = [
   "matous@holinka.com",
   "danek11@seznam.cz",
   "rennud15@gmail.com",
   "pepa@centrum.cz"
]

def filtruj_adresy_s_cisly(adresy: list) -> list:
    list_adres_s_cisly = []

    for adresa in adresy:
        for znak in adresa:
            if not znak.isnumeric():
                continue
            list_adres_s_cisly.append(adresa)
            break
    return list_adres_s_cisly


vysledek = filtruj_adresy_s_cisly(adresy)
print(vysledek)


# ---------------------------------------------------------------------------------------------------


prvni_cislo = int(input("Zadej první číslo: "))
druhe_cislo = int(input("Zadej druhé číslo: "))


# rozklad čísel na prvocisla
def rozklad_na_prvocisla(n):
    """
    Rozklad čísla n na prvočísla, jejichž součin dá zpět rozkládané číslo.
    """
    delitel = 2  # Začínáme s nejmenším prvočíslem
    ukladani_prvocisel = []  # Sem ukládáme prvočinitele

    while delitel * delitel <= n:  # Projdeme všechny možné dělitele
        while n % delitel == 0:  # Pokud je n dělitelné beze zbytku
            ukladani_prvocisel.append(delitel)  # Přidáme dělitel do seznamu
            n //= delitel  # Snížíme n
        delitel += 1  # Zkusíme další číslo

    if n > 1:  # Pokud zůstane zbytek větší než 1, je to také prvočíslo
        ukladani_prvocisel.append(n)

    return ukladani_prvocisel  # Spojíme činitele jako řetězec

# Příklad použití
vysledek_rozkladu_1 = rozklad_na_prvocisla(prvni_cislo)
print(vysledek_rozkladu_1)  # Výstup: 2 * 2 * 3
print(vysledek_rozkladu_2 := rozklad_na_prvocisla(druhe_cislo))


# rozklad čísel na prvocisla

def je_prvocislo(ciso: int, prvocisla:int):


def generuj_interval_prvocisel(interval: list):
    


