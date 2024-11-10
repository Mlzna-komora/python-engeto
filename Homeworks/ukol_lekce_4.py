# ÚKOL 1: Vytvoření programu, který spočítá obsah samohlásek a souhlásek v zadaném str:
veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'
samohlasky = "aeiouáéíóú"
souhlasky = "bcčdďfghjklmnňprřsštťvzžcdž"
selekce_slov = []
vysledek = {
    "samohlásky": [],
    "souhlásky": []
}
print(type(vysledek)) # dict - OK

for slova in veta.split(): # fce SPLIT vytvoří list!!!
    slova.strip(",.")
    selekce_slov.append(slova.lower())
print(selekce_slov) # ['zvuk', 'řeči', 'je', 'produkován', 'poměrně', 'otevřenou', 'konfigurací', 'vokálního', 'traktu']


for pismeno in veta.lower():
    pismeno.strip(",.")
    if pismeno in samohlasky:
        vysledek["samohlásky"].append(pismeno)
    elif pismeno in souhlasky:
        vysledek["souhlásky"].append(pismeno)
print(vysledek) 
# {'samohlásky': ['u', 'e', 'i', 'e', 'o', 'u', 'o', 'á', 'o', 'o', 'e', 'e', 'o', 'u', 'o', 'i', 'u', 'a', 'í', 'o', 'á', 'í', 'o', 'a', 'u'], 'souhlásky': ['z', 'v', 'k', 'ř', 'č', 'j', 'p', 'r', 'd', 'k', 'v', 'n', 'p', 'm', 'r', 'n', 't', 'v', 'ř', 'n', 'k', 'n', 'f', 'g', 'r', 'c', 'v', 'k', 'l', 'n', 'h', 't', 'r', 'k', 't']}

# mám list, kde klíči odpovídá několik hodnot - ty chci spočítat
pocet_samohlasek = len(vysledek["samohlásky"])
print(pocet_samohlasek) # 25

pocet_souhlasek = len(vysledek["souhlásky"])
print(pocet_souhlasek) # 35

print("Počet souhlásek: ", pocet_souhlasek, " | Počet samohlásek: ", pocet_samohlasek)
# Počet souhlásek:  35  | Počet samohlásek:  25

print("=" * 80)
#================================================================================



# ÚKOL 2: Součet odděleně všechna sudá a lichá čísla ze seznamu. Na konci vypsat absolutní hodnotu rozdílu mezi těmito součty
cisla_seznam = [1, 2, 3, 4, 5, 6, 7, 8]
rozdeleni_cisel = {
    "suda": [],
    "licha": []
}

for cisla in cisla_seznam:
    if cisla % 2 == 0:
        rozdeleni_cisel["suda"].append(cisla)
    else:
        rozdeleni_cisel["licha"].append(cisla)

pocet_sudych = len(rozdeleni_cisel["suda"])
print(pocet_sudych) # 4

pocet_lichych = len(rozdeleni_cisel["licha"])
print(pocet_lichych) # 4

# TO DO: součet všech sudých a všech lichých čísel
soucet_sudych = sum(rozdeleni_cisel.get("suda", [])) # fce GET v DICT slouží k získání hodnoty přiřazené ke klíči!!!
print(soucet_sudych) # 20

soucet_lichych = sum(rozdeleni_cisel.get("licha", []))
print(soucet_lichych) # 16

absolutni_soucet_1 = abs(soucet_sudych - soucet_lichych)
print(absolutni_soucet_1) # 4

absolutni_soucet_2 = abs(soucet_lichych - soucet_sudych)
print(absolutni_soucet_2) # 4 - OK

print("=" * 80)

#================================================================================



# ÚKOL 3: Program potřebuje od uživatele START, STOP, DELITEL. Po zapracování vypíše všechna CELÁ ČÍSLA v intervalu od START do STOP, která jsou dělitelná hodnotou v DĚLITEL

vysledek = list()
start = 3
stop = 9
delitel = 3

# TO DO: ověřit, že jsou proměnné výše datový typ int pomocí fce isinstance
print(isinstance(start, int)) # vše TRUE - OK
print(isinstance(stop, int))
print(isinstance(delitel, int))

if isinstance(start, int) and isinstance(stop, int) and isinstance(delitel, int):
    print("Zadaný rozsah: <", start, ", ", stop, ">", sep="") # Zadaný rozsah: <3, 9>

    for cisla in range(start, stop + 1): # NUTNÉ PŘIDAT +1, protože stop jde do -1
        if cisla % int(delitel) == 0:
            vysledek.append(cisla)

    print("Čísla dělitelná ", delitel, ":", vysledek) # Čísla dělitelná  3 : [3, 6]
else:
    print("Zadané vstupy musí být čísla.")

print("=" * 80)

#================================================================================



# ÚKOL 4: Slovníková komprehence spočítat délky slov v zadané sekvenci:

seznam_slov = ["jablko", "pomeranč", "banán", "kiwi", "hruška"]
pocet_slov = len(seznam_slov)
print(pocet_slov) # 5 - vypíše počet hodnot v listu

for ovoce in seznam_slov:
        print(ovoce)

# Chci délky slov:
slovnik = {}

for ovoce in seznam_slov:
    slovnik[ovoce] = " "
print(slovnik) # {'jablko': ' ', 'pomeranč': ' ', 'banán': ' ', 'kiwi': ' ', 'hruška': ' '}

delka_slov = slovnik.values()
print(delka_slov)


