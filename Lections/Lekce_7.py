# FUNKCE

ciselna_r_1 = (1, 2, 3, "a")
ciselna_r_2 = (1, 2, 3, 4)
ciselna_r_3 = (5, 6, 7, 8)
ciselna_r_4 = (9, 10, 11, 12)


def secti_vsechny_cisla(sekvence):
    soucet_cisel = 0

    for cislo in sekvence:
        if isinstance(cislo, str) and not cislo.isnumeric():
            continue
        soucet_cisel = soucet_cisel + int(cislo)
    else:
        print(soucet_cisel)


secti_vsechny_cisla(ciselna_r_1)
secti_vsechny_cisla(ciselna_r_2)
secti_vsechny_cisla(ciselna_r_3)
secti_vsechny_cisla(ciselna_r_4)



# Původní definice funkce
def scitej_dve_hodnoty(cislo_1, cislo_2):
    """Vraci soucet dvou hodnot uvnitr parametru."""
    return cislo_1 + cislo_2


# Spuštění funkce
soucet_1 = scitej_dve_hodnoty(1, 14)
soucet_2 = scitej_dve_hodnoty(2, 8)

print(soucet_1, soucet_2, sep="\n")