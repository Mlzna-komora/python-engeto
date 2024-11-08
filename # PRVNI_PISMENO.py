# PRVNÍ PÍSMENO - ověřování správnosti prvního písmene každého dne v týdnu
vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ['p', 'ú', 's', 'č', 'p', 's', 'n']
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')

cislo_dne = float(input('Napiš číslo: '))
#cislo_dne_int = int(cislo_dne)

den_tydne = (input('Napiš počáteční písmeno dne v týdnu: '))

cislo_dne.insert(1, 'p')
cislo_dne.insert(2, 'ú')
cislo_dne.insert(3, 's')
cislo_dne.insert(4, 'č')
cislo_dne.insert(5, 'p')
cislo_dne.insert(6, 's')
cislo_dne.insert(7, 'n')


# ověření, jestli hodnota v cislo_dne je v listu vstupni_cisla:
if cislo_dne in vstupni_cisla:
    print('Správná vstupní hodnota!')
    if den_tydne in vstupni_pismena: # indexace z čísla na den v týdnu (např. : 2 --> 'úterý')
        print('Správné písmeno!')
else:
    print('Špatná vstupní hodnota!')



