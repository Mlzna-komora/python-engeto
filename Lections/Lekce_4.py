# v každém kroku vytiskneme jedno písmenko po druhém, iterovatelný datový typ je probraný celý --> program skončí
for pismeno in "Python Akademie": # 4 iterovatelné datové typy lze dávat do for cyklu, HLAVIČKA SMYČKY
    print(pismeno)

muj_seznam = [1, 2, 3, 4, 5] # list, chci vypsat každou jeho hodnotu

print(muj_seznam[0]) # 1 vypíše pod sebe
print(muj_seznam[1]) # 2
print(muj_seznam[2]) # 3
print(muj_seznam[3]) # 4
print(muj_seznam[4]) # 5

# můžeme nahradit for cyklem:
for cislo in muj_seznam: # muj_seznam je iterovatelný (a hlavně iterovaný) zdroj hodnot
    print(cislo) # vytiskne to stejné jako nahoře


# lze iterovat pomocí cyklu for i SLOVNÍK
for klic in {"jméno": "Metoděj", "vek": 1, "přezdívka": "Lasička"}: 
    print(klic) 

for hodnota in {"jméno": "Metoděj", "vek": 1, "přezdívka": "Lasička"}: 
    print(hodnota) 


#pismena = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
#for pismeno in pismena: # fce pismeno se automaticky vytvoří, když vytvořím for cyklus
#    if pismeno == "c":
#        print(f"Mam hodnotu -> "{pismeno}"<--------")
#    else:
#        print(f"Nemám "c", ale "{pismeno}"")
#else:
#    print("-" * 33, "Dokoncil jsem hledani pismena "c"", "-" * 33, sep"\n") 
# NEFUNGUJE


for pismeno in "Python Akademie":
    print(pismeno) # P, break přerušil cyklus po první iteraci
    break

for pismeno in "Python Akademie":
    print(pismeno)
else:
    print("-" * 29, "Konec smyčky!", "-" * 29, sep="\n")
    


# RANGE - interval/rozsah - NOVÝ DATOVÝ TYP PRACUJÍCÍ POUZE S CELÝMI ČÍSLY (int)
print(range(11)) # range(0, 11)
print(list(range(11))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(type(range(11))) # <class 'range'>


# ITEROVATELNÉ DATOVÉ TYPY:
# str, list, tuple, dice, set

suda_cisla = list()
cela_cisla = (1, 2, 3, 4, 5)
for cislo in cela_cisla:
    if cislo % 2 == 0:
        suda_cisla.append(cislo)
print(suda_cisla) # [2, 4]

suda_cisla = list()
cela_cisla = (1, 2, 3, 4, 5)
for cislo in cela_cisla:
    if cislo % 2 == 0:
        print("Sudé číslo")
    elif cislo % 2 != 0:
        print("Liché číslo")


# BREAK:
for pismeno in ("a", "b", "c", "d"):
    if pismeno == "c":
        print("Našel jsem 'c', přeskakuji cyklus.")
        break
    print(pismeno)

# CONTINUE:
for pismeno in ("a", "b", "c", "d"):
    if pismeno in {"a", "b"}:
        continue
    print("Hodnota", pismeno, "je dulezita")


# DATOVÝ TYP RANGE:
rozsah = range(1,20)
print(rozsah) # range(1, 20)

#lze použít range jako jeden arg (stop), dva arg (start, stop), 3 argumenty (start, stop, step)
rozsah_2 = tuple(range(1,20,3)) # (1, 4, 7, 10, 13, 16, 19)
print(rozsah_2)


#  ENUMERATE 
jmena = ("Java", "C", "Rust", "Python")
print(tuple(enumerate(jmena))) # ((0, 'Java'), (1, 'C'), (2, 'Rust'), (3, 'Python'))

for index, symbol in enumerate("Ahoj, vsem"):
    print(f"INDEX: {index}, SYMBOL: {symbol}") # INDEX: 0, SYMBOL: A, atd...


# COMPREHENSIONS
# původní slovník se všemi městy
mesta = {
    "Praha": 1_335_084, 
    "Brno": 382_405, 
    "Ostrava": 284_982,
    "Plzen": 175_219, 
    "Liberec": 104_261
}

# klasická smyčka 'for'
nad_sto_tisic_obyv = dict()
for mesto in mesta:
    if mesta[mesto] > 200_000:
        print(nad_sto_tisic_obyv)
else:
    print(f"Klasická smyčka: '{mesta}'")

for mesto in mesta:
    if mesta[mesto] > 200_000:
        nad_sto_tisic_obyv[mesto] = mesta[mesto]
else:
    print(f"Klasicka smycka: {nad_sto_tisic_obyv}")