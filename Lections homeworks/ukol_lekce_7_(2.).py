from collections import Counter


# Největší spol. dělitel (greates common divisor - GCD)

prvni_cislo = int(input("Zadej první číslo: "))
druhe_cislo = int(input("Zadej druhé číslo: "))


# rozklad čísel na prvnocisla
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

def spolecna_prvocisla(num1, num2):
      """
    Najde společná prvočísla ze dvou seznamů rozkladů, včetně duplicit.
    
    Parametry:
    rozklad1 (list): První seznam prvočísel.
    rozklad2 (list): Druhý seznam prvočísel.
    
    Návratová hodnota:
    list: Seznam společných prvočísel s ohledem na četnost.
    """
      counter_1 = Counter(num1)
      counter_2 = Counter(num2)

      #průnik:
      prunik = counter_1 & counter_2
      return list(prunik.elements()) # elements seřadí znaky 

print(vysledek_pruniku := spolecna_prvocisla(vysledek_rozkladu_1, vysledek_rozkladu_2))



def nejvetsi_spol_delitel(vysledek_pruniku):
    """
    Vynásobí všechny čísla, která jsou v množině průniku po rozkladu na prvočísla.

    Parametry:
    list čísel

    Návratová hodnota:
    int

    """
    soucin = 1 # startovní hodnota, která neovlivní násobení
    for cislo in vysledek_pruniku:
        soucin *= cislo # soucin = soucin * cislo
        podil_soucinu = int((prvni_cislo * druhe_cislo)/soucin)
    return soucin, podil_soucinu

print(nejvetsi_spol_delitel(vysledek_pruniku))


    
