# v každém kroku vytiskneme jedno písmenko po druhém, iterovatelný datový typ je probraný celý --> program skončí
for pismeno in "Python Akademie": # 4 iterovatelné datové typy lze dávat do for cyklu, HLAVIČKA SMYČKY
    print(pismeno)

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
