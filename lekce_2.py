
#BOOLEAN - DATOVÝ TYP URČUJÍCÍ TRUE A FALSE
#Boolen je podmnožinou datového typu int (true = 1, false = 0)
# = vyhodnocení, jestli je zápis (nebo hodnota) pravdivá nebo nepravdivá

#"==" srovnání dvou hodnot
print(True == 1) #true
print(False == 0) #true
print(6 > 4) #true
print(1000 < 100) #false

#POMOCNÁ ZABUDOVANÁ FCE BOOL - pracuje jako soudce
print(bool(2 > 1)) #true
print(bool(5 != 1)) #true, != NEROVNOST, == ROVNOST

print(bool(not True)) #false
print(bool(not False)) #true
print(1 < 5 and 5 > 10) #true and false = false

#V Pythonu lze porovnávat - jestli zabírá např. jedna věc stejně operačního prostoru (místo v paměti) jako věc druhá
#Každý objekt má svůj identifikátor (číslo, poznávací značka)
print(id("a")) #4564334344
# id porovnává id i hodnotu
# == porovnává pouze hodnotu

prijmeni_1 = "Kocour"
prijmeni_2 = prijmeni_1
print(prijmeni_1 is prijmeni_2) #true
print(prijmeni_1 == prijmeni_2) #true

print(bool("m" in "Matous")) #false
print(bool("M" in "Matous")) #true
print("m" is ("a", "n", "c", "ma")) #false 


# PODMÍNKY
if True:
    print("Ahoj, Matouši!")
print("Pokračuji...")

vek = 10
if vek > 18:
    print("Ahoj, Matouši!")
print("Pokračuji...") #vypíše pouze Pokračuji... (podmínka neplatí a program pokračuje)

vek = 20
if vek > 18:
    print("Ahoj, Matouši!")
    if vek > 30:
        print("Dobře ty!")
print("Pokračuji...") #vypíše všechno, #NUTNÉ SPRÁVNĚ ODSAZENÍ

# IF, ELSE
jmeno = "Matouš"
plnolety = True
if plnolety:
    print("Uživatel", jmeno, "je plnoletý.")
else:
    print("Uživatel", jmeno, "není plnoletý.") # když nevyjdouo podmínky předtím, else ...

# NESTOVANÁ podoba
jmeno = "Matouš"
dospely = False
uzivatel = True
if uzivatel:
    if dospely:
        print("Ahoj,", jmeno, "tady je naše kompletní nabídka.")
    else: 
        print("Ahoj,", jmeno, "tady je naše nabídka pro mladistvé.")



# CVIČENÍ:
cislo_1 = float(input("Zadej první číslo")) #input jsou automaticky stringy - MUSÍM PŘETYPOVAT
cislo_2 = float(input("Zadej druhé číslo"))
if cislo_1 > cislo_2:
    print("První číslo je větší než druhé číslo.")
    if cislo_1 < cislo_2:
        print("Druhé číslo je větší než první číslo.")
else: 
    print("Obě čísla jsou stejná.")

# BY MĚLA BÝT ALTERNATIVA PŘEDCHOZÍHO
cislo_1 = float(input("Zadej první číslo")) #input jsou automaticky stringy - MUSÍM PŘETYPOVAT
cislo_2 = float(input("Zadej druhé číslo"))
if cislo_1 > cislo_2:
    print("První číslo je větší než druhé číslo.")
if cislo_1 < cislo_2:
        print("Druhé číslo je větší než první číslo.")
if cislo_1 == cislo_2: 
    print("Obě čísla jsou stejná.")

# NEBO!
if 0 < cislo <10: 
    print("Patřím mezi prvních deset.")
elif 0 < cislo < 20:
    print("Patřím mezi druhých deset.")
else: 
    print("První číslo je větší než druhé.")


# TERNÁRNÍ OPERÁTOR
#<proveď_toto> if <pokud_platí_toto> else <jinak_proveď_toto>

vek = 18

if vek >= 18:
    print("Dospělý")
else:
    print("Mladiství")

print("Dospělý") if vek >= 18 else print("Mladiství") # Dodělat


