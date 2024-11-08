#1. CÍL - INDEXOVÁNÍ
#prvnívh 5 písmen slova indexování
print("indexování"[0:5]) #index
print("indexování"[:5])

#posledních 5 písmen
print("indexování"[4:9]) #xován - ŠPATNĚ
print("indexování"[5:10]) #ování - SPRÁVNĚ
print("indexování"[-5:]) #ování - SPRÁVNĚ

#každé 3. písmeno počínaje 1. (i)
print("indexování"[0:10:3]) #ieví
print("indexování"[::3]) #ieví


#2. CÍL - PŘEVOD JEDNOTEK
# z kg na libry
# z km na míle
# z litrů na galony

#převody mezi jednotkami
kg_libra = 2.20
km_mile = 0.62
litr_galon = 0.26

#proměnné s následujícím počtem 
kg_pocet = 80
km_pocet = 54
litr_pocet = 5

#proměnné s výpočtem - tj. kolik liber je 80 kg
kg_vysledek = (kg_pocet * kg_libra)
#print(kg_vysledek)
km_vysledek = (km_pocet * km_mile)
litr_vysledek = (litr_pocet * litr_galon)

print(kg_pocet, "kg je ", kg_vysledek, "liber")
print(km_pocet, "km je ", km_vysledek, "mil")
print(litr_pocet, "kg je ", litr_vysledek, "galonů") #SPRÁVNĚ 


#3. CÍL - OPERACE S STR A INT
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000

sleva_merc = 5000
cena_2_merc = mercedes * 2
cena_merc_a_rolls = mercedes + rolls_royce 
cena_2_rolls_s_vybavou = (2 * rolls_royce) + (2 * vybava)
cena_merc_s_vybavu = mercedes + vybava
merc_se_slevou = mercedes - sleva_merc

print("Sleva na Mercedes: ",sleva_merc)
print("Cena za dva mercedesy je: ", cena_2_merc)
print("Cena za Mercedes a Rolls-Royce: ", cena_merc_a_rolls)
print("Cena za dva Rolls-Royce s příplatkovou výbavu", cena_2_rolls_s_vybavou)
print("Cena za Mercedes s příplatkovou výbavou", cena_merc_s_vybavu)
print("Cena za Mercedes po slevě: ",merc_se_slevou)


jmeno = "Lukáš"
prijmeni = "Dvořák"
cele_jmeno = jmeno + " " + prijmeni
delka_jmena = len(cele_jmeno)
cara = "=" * delka_jmena

print("celé jméno: ", cele_jmeno)
print("Délka jména je: ", delka_jmena)
print(cara)
print(cele_jmeno)
print(cara)


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
print(bool(5 != 1)) #true

