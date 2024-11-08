print("zdarky parky, zmrdecci")

print(100 + 200)
print(type(222)) #pomocí zabudované fce type ověříme, jestli je číselná hodnota skutečně integer - po run kódu vyjde int
print(type(0.3)) #správně po přeložení kódu vyhodí float
print(0.1 + 0.2) #plovoucí řádová čárka - v pythonu nemají některá čísla odpovídající binární tvar - dostávám přibližné hodnoty
print(2 + 3 * 2)
print((2 + 3) * 2)
#print(Python) po runu dostávám errorek (NameError) - známka špatného zápisu
print("Python") #správný zápis slova (stringu - textového řetězce)
print(type("Python"))
print(type("12345")) #uvozovky vždy udělají string (=textový řetězec) ze všeho v uvozovkách
print("It`s \"kind\" of Friday") #\"\"escape characters - používám při potřebě napsat speciální znak, existuje tabulka spec. znaků
print(int("2")) #převod stringu (tj. symbolu v uvozovkách) do integeru (celého čísla) pomocí fce int
print(type(int("2"))) #pouze ověření, že int skutečně přeměnil string do int
print("ICY" + "L") #ICYL
print("ICY " + "L") #ICY L
print("ICY" + " L") #ICY L
print("ICY" + " " + "L")  #ICY L - zle napsat různými způsoby - ovykle existuje více zápisů jedné věci
print("Metisek" * 3) #repetition

#INDEXOVÁNÍ
print("AUTOBUS"[1]) #INDEXOVÁNÍ mi hodí U - začíná od 0 (od začátku, resp. -1 od konce) 
print("AUTOBUS"[0:4]) #dostávám AUTO - zprava otevřený interval, tj. [), proto dostávám pouze AUTO
print("AUTOBUS"[0:7:2]) #dostávám ATBS - přeskakování od 0 do 7 vypíše každý druhý znak

jmeno = "Metisek" #uložení Metiška do proměnné, abych furt nepsala Metišek, po runu není v kódu nic vidět - v paměti pc je uložený string Metišek jako jméno
print(jmeno) #po runu vypíše Metisek, variables může obsahovat písmenné, číselné znaky a podtržítka

jmeno2 = "Martas"
moje_jmeno = "Kata" #snake case - doporučuje se používat, když proměnná má více slov
mojeJmeno = "Volsa" #camel case
MojeJmeno = "Kocicka" #kebab case
PI = 3.141
TIHOVE_ZRYCHLENI = 9.81
print(PI + TIHOVE_ZRYCHLENI) #práce s proměnnými funguje intuitivně

#SEKVENCE
#list (seznam) - lze si uložit více stringů, int,.., MĚNITELNÝ - lze do něj přidávat/ubírat
#tuple (n-tice) - NELZE MĚNIT

muj_seznam = ["Matous", "Marek", "Lukas", "Jan"] #hranaté závosrky, stringy, oddělené čárkami
#VYTVOŘENÍ LISTU
prvni_seznam = []
druhy_seznam = list()
print(type(prvni_seznam)) 
print(type(druhy_seznam)) #obojí je skutečně type list - OK
treti_seznam = [2, 4, 6, 8]

muj_seznam = ["Matous", "Marek", "Lukas", "Jan"]
print(muj_seznam[0]) #Matous
print(muj_seznam[1]) #Marek
print(muj_seznam[-1]) #Jan
print(muj_seznam[1:3]) #['Marek', 'Lukas']

#VYTVOŘENÍ TUPLE - funguje stejně jako list
muj_tupl = ("Matous", "Marek", "Lukas", "Jan")


#FUNKCE

#type - vrací datový typ zadané hodnoty 
print(type("Metodej")) #<class, "str">

#round - zaokrouhlení na stanovený počet desetinných míst
print(round(0.987, 2)) #0.99

#abs - absolutní hodnota

#int - vrací integer ze zadaného stringu nebo číselného údaje, CELÉ ČÍSLO
print(int("111")) 
print(int(2.123)) #2 (z floatu udělalo celé číslo - int)

#input - ukládání vstupů od uživatele - VZNIKLÁ PROMĚNNÁ FCÍ INPUT JE VŽDY TYPU STRING!!!
#pismeno = input("Vepis pismeno")
#print(pismeno)

#len - vrací délku zadané hodnoty
print(len("hakisak")) #vrací 7 
#print(len(87643)) #error - int has no len()


