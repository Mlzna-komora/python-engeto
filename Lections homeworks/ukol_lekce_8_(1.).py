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


cislo = rozklad_na_prvocisla(564)
print(cislo) # [2, 2, 3, 47]


# ---------------------------------------------------------------------------------------------------

# Vytvoř program, který ze zadaného textu vytáhne emaily

text = """\
Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc tristique
fringilla congue. Donec ante diam cnn@info.com, dapibus
lacinia vulputate vitae, ullamcorper in justo. Maecenas
massa purus, ultricies a dictum ut, dapibus vitae massa.
Cras abc@gmail.com vel libero felis. In augue elit, 
porttitor nec molestie quis, auctor a quam. Quisque b2b@money.fr pretium dolor et tempor feugiat. Morbi libero lectus, porttitor eu mi sed, luctus lacinia risus. Maecenas posuere leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam erat volutpat. Donec eleifend felis at leo ullamcorper cursus. Pellentesque id dui viverra, auctor enim ut, fringilla est. Maecenas gravida turpis nec ultrices aliquet.
"""

import re

def uloz_emailove_adresy(text: str) -> list:
    """
    r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}':
        a-zA-Z0-9._%+- odpovídá uživatelské části e-mailu
        @ odpovídá symbolu zavináče.
        a-zA-Z0-9.- odpovídá doménové části.
        \.[a-zA-Z]{2,} odpovídá koncovce domény (např. .cz, .com).

    re.findall:
        Vrací seznam všech nalezených e-mailů v textu.
    """

    email_adresy = []

    email_vzor = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    email_adresy = re.findall(email_vzor, text)

    return email_adresy

vysledek = uloz_emailove_adresy(text) 
print(vysledek)





def uloz_emailove_adresy_2(text: str) -> list:
    """
    Uloz vsechny ocistene emailove adresy ze zadaneho textu.

    Priklad:
    >>> print(uloz_emailove_adresy("Ahoj, tady matous@gmail.com."))
    {'matous@gmail.com'}

    >>> print(uloz_emailove_adresy("Ahoj, tady matous"))
    {}
    """
    return [
        slovo.strip(",.:;")
        for slovo in text.split() # fce split rozdělí text na slova a uloží je do listu
        if "@" in slovo # když se ve slovu objeví @ je splněná podmínka if a uloží se to
    ]


# Uloz vystup funkce do promenne
vysledek = uloz_emailove_adresy_2(text)

# Vytiskni obsah promenne vysledek
print(vysledek)
