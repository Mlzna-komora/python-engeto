# Fce pracuje se vstupy
# - parametry: obecné proměnné při definici
# - argumenty: konkrétní hodnoty, které vkládám při spouštění

def spoj_cele_jmeno(jmeno, prijmeni): # zde jsou to parametry
    """
    Spoj zformatovane hodnoty v parametrech.

    Priklad:
    >>> formatuj_cele_jmeno("Petr", "Svetr")
    p.svetr
    """
    return ".".join(
        (
            jmeno[0].lower(),
            prijmeni.lower()
        )
    )

print(spoj_cele_jmeno("Adam", "Novak")) # a.novak, zde jsou to argumenty

# Seznam všech dostupných variant:
# - poziční parametry (argumenty),
def uloz_informace(jmeno, prijmeni, telefon):
    return {
        "jmeno": jmeno,
        "prijmeni": prijmeni,
        "telefon": telefon
}

print(uloz_informace("Petr", "Svetr", "+420 777 666 555"))

#--------------------------------------------------------------------------

def vypocitej_hodnotu(koef_1, koef_2, koef_3):
    """
    Vypocitej hodnotu na zaklade tri zadanych koeficinetu.
    """
    return (1/koef_1) * (koef_2 ** koef_3)

print(vypocitej_hodnotu(1, 2, 4))

#--------------------------------------------------------------------------

def vypocitej_hodnotu(koef_1, koef_2, koef_3):
    """
    Vypocitej hodnotu na zaklade tri zadanych koeficinetu.
    """
    return (1 / koef_1) * (koef_2 ** koef_3)

print(vypocitej_hodnotu(koef_1=0.5, koef_2=3, koef_3=2))
# toto je lepší varianta - koeficienty jsou lépe určené
# pořadí v tomto případě je libovolné - ROZHODUJÍCÍ JE VZTAH MEZI HODNOTOU A PARAMETREM


# - klíčové argumenty,
# - defaultní parametry,

# Někdy dojdeš k závěru, že funkce, kterou tvoříš, potřebuje jeden parametr,
# který bude v naprosté většině spouštění používat tutéž hodnotu

def vytvor_pozdrav(jmeno = "Matous"):
    print("Ahoj,", jmeno)

vytvor_pozdrav()

#--------------------------------------------------------------------------

def vytvor_pozdrav(jmeno="Matous"):
    print("Ahoj,", jmeno)

vytvor_pozdrav() # Ahoj, Matous
vytvor_pozdrav("Lukas") # Ahoj, Lukas - lze parametr takto nahradit


# - position-only parametry,
# Účelem tohoto typu zápisu parametrů, je vynutit od uživatele zápis všech parametrů
# nalevo od lomítka / jako poziční parametry (resp. argumenty)

def napis_pozdrav(jmeno, /, registrovany):
    if not registrovany:
        print("Nejsi uzivatel!")
    print("Ahoj,", jmeno)


napis_pozdrav("Matous", True) # Ahoj, Matous


# - *args,
# možnost VKLÁDÁNÍ LIBOVOLNÉHO MNOŽSTVÍ VSTUPŮ

def vypocitej_prumer(args): # funguje i bez *
    return sum(args) / len(args)


moje_cisla = [1, 2, 3, 4, 5]
print(vypocitej_prumer(moje_cisla))

#--------------------------------------------------------------------------

def vypocitej_prumer(*args): # zde už je nutní *, protože se jedná o různý počet potenciálních hodnot vkládaných do fce
    return sum(args) / len(args)


print(vypocitej_prumer(1, 2, 3, 4, 5))

# - **kwargs
def vytvor_slovnik(**kwargs):
    vysledek = dict()

    for klic, hodnota in kwargs.items():
        vysledek[klic] = hodnota
    return vysledek

print(vytvor_slovnik(jmeno="Matous", prijmeni="Holinka")) # {'jmeno': 'Matous', 'prijmeni': 'Holinka'}

#--------------------------------------------------------------------------

def vytvor_slovnik(**kwargs):
    vysledek = dict()

    for klic, hodnota in kwargs.items():
        vysledek[klic] = hodnota
    return vysledek 
print(vytvor_slovnik(jmeno="Matous", prijmeni="Holinka", vek=90, email="matous@holinka.cz"))
# {'jmeno': 'Matous', 'prijmeni': 'Holinka', 'vek': 90, 'email': 'matous@holinka.cz'}


# ZABUDOVANÉ FCE:
# jejich přítomnost lze zkontrolovat pomocí
print(dir(__builtins__))

