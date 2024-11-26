# HANGMAN

zivoty = 7
hra_bezí = True
slovo = "obesenec"
tajenka = len(slovo) * ["_"]

def nahrad_v_tajence(tajenka, stare, nove):
    return [nove if x == stare else x for x in tajenka]


# Connect this Colab to your Drive - NĚJAK DODĚLAT

print(tajenka)
tip = input("Hadej pismeno/slovo:")
if tip == slovo:
    print("super!")
    quit()

for index, pismeno in enumerate(slovo):
    if pismeno in slovo:
        print("Uhodl jsi písmeno.")
        # print tajenky s uhádnutým písmenem
        # tajenka = [tip if x == pismeno else x for x in tajenka]
        tajenka[index] = pismeno
        print(tajenka)

        #upravene_slovo = slovo.replace(tip, "-")
        #print(upravene_slovo)
        
        #tajenka_str = " ".join(tajenka)
        #print(tajenka_str)

        #upravena_tajenka_str = tajenka_str.replace("_", tip)
        #print(upravena_tajenka_str)

        #index = tajenka.index("_")
        #tajenka[index] = tip
        
        #nova_tajenka = nahrad_v_tajence(tajenka, "-", tip)
        #print(nova_tajenka)
    else:
        print("chyba")



