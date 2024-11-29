# vynásobení dvou čísel
prvni_cislo = 5
druhe_cislo = 5

def vynasob(num1, num2):
    return num1 * num2

vysledek = vynasob(prvni_cislo, druhe_cislo)
print(vysledek) # 25


# zdvojnásobení všech znaků typu string - AAhhoojj  vvššeemm
vstup = "Ahoj všem"

def zdvojnasob_vsechny_znaky(zadani:str) -> str:
    zdvojene = []

    for znak in zadani:
        zdvojene.append(znak * 2)
    return "".join(zdvojene)

vysledek_2 = zdvojnasob_vsechny_znaky(vstup)
print(vysledek_2)


# ověření, zda OS na pc je Win či nikoliv
import sys # pomocná knihovna s příslušnou metodou na ověření OS

def je_os_windows():
    """
    Vrať bool hodnotu True, pokud je můj os win. Jinak vrať False.
    """
    return sys.platform.startswith("win")

print(je_os_windows)
# startswith() je metoda řetězců, která kontroluje, zda řetězec začíná specifikovaným podřetězcem.
# V tomto případě kontrolujeme, zda hodnota sys.platform začíná řetězcem "win", což platí pro všechny verze Windows


# Největší spol. dělitel (greates common divisor -GCD)
prvni_cislo = 12
druhe_cislo = 16


# rozklad čísel na prvnocisla
def rozklad_na_prvocisla(n):
    """
    Rozklad čísla n na prvočísla, jejichž součin dá zpět rozkládané číslo.
    """
    delitel = 2 # delit začínáme od 2
    ukladani_prvocisel = []

# // dělení beze zbytku, % zbytek po dělení
    if n // delitel == 0:
        ukladani_prvocisel.append(delitel)
        delitel += 1
    else:









def najdi_gcd(num1, num2):
    num1 % num2

