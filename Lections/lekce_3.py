True and True or False and not True

# SLOVNÍK (~dictionary)

muj_slovnik_1 = {'jmeno': 'Radim', 'prijmeni': 'Jedlicka'} # standardní datový typ 
# klíč: hodnota - podle klíče dohledávám hodontu
# klíče jsou stringy ('jmeno', 'vek',...)
# hodnoty jsou různého datového typu (str, int, bool)
# slovník je ZMĚNITELNÝ (~mutable)

# se slovníkem pracuji tak, že PODLE KLÍČE HLEDÁM HODNOTU = MAPOVÁNÍ

muj_slovnik_01 = {
    'jmeno': 'Matous',
    'vek': 100,
    'ridicske_opravneni': True,
    'volny_cas':['klavir', 'basa']
}
print(muj_slovnik_01['jmeno'])


muj_novy_slovnik = dict() # 1. možnost tvorby slovníku
id(muj_novy_slovnik)
type(muj_novy_slovnik) # dict - OK

muj_novy_slovnik_2 = {} # tvorba slovniku pomocí složených závorek
id(muj_novy_slovnik_2)
type(muj_novy_slovnik_2) # dict - OK

muj_novy_slovnik['jmeno'] = 'Radim'
print(muj_novy_slovnik) # {'jmeno': 'Radim'}

muj_novy_slovnik['rid_opravneni'] = True
muj_novy_slovnik['hobby'] = ('fotbal', 'hry', 'pratele')
muj_novy_slovnik['vek'] = 22
muj_novy_slovnik['jmeno'] = 'Karin'

print(muj_novy_slovnik) # {'jmeno': 'Karin', 'rid_opravneni': True, 'hobby': ('fotbal', 'hry', 'pratele'), 'vek': 22} - ÚPLNĚ JINÉ POŘADÍ, TO JE NORMÁLNÍ
# jednotlivé hodnoty získávám pomocí klíčů
print(muj_novy_slovnik['jmeno']) # Karin
print(muj_novy_slovnik['hobby']) # ('fotbal', 'hry', 'pratele')
print(muj_novy_slovnik['hobby'][2]) # pratele
print(muj_novy_slovnik['hobby'][2][2]) # a - jdeme do mého slovínu, hodnota pod jménem hobby -> pratele -> a
print(muj_novy_slovnik['hobby'][2], muj_novy_slovnik['hobby'][2]) # pratele pratele
print(muj_novy_slovnik['hobby'][2] * 2) #pratelepratele


# SLOVÍK VE SLOVNÍKU (~nesting)
kontakt = {
    'telefon': '000 123 456 789',
    'email': 'lukas@gmail.com',
    'web': 'www.lukas.cz'
}
muj_novy_slovnik['kontakt'] = kontakt
print(muj_novy_slovnik) # {'jmeno': 'Karin', 'rid_opravneni': True, 'hobby': ('fotbal', 'hry', 'pratele'), 'vek': 22, 'kontakt': {'telefon': '000 123 456 789', 'email': 'lukas@gmail.com', 'web': 'www.lukas.cz'}}
#pprint(muj_novy_slovnik)
print(muj_novy_slovnik['kontakt']) # {'telefon': '000 123 456 789', 'email': 'lukas@gmail.com', 'web': 'www.lukas.cz'}
print(muj_novy_slovnik['kontakt']['email']) # lukas@gmail.com - přesně jako případ s dvojkama - řádek 36


# METODY SLOVNÍKU
# pop - odstraní jeden klíč (který jsme nadefinovali)
opravneni = muj_novy_slovnik.pop('rid_opravneni') # pop vrátí hodnotu zadefinovaného klíče a zároveň hodnotu klíče odstraní
print(opravneni) # true

# keys - vylistování klíčů
muj_novy_slovnik.keys()

# values - nějak vrací všechny hodnoty


pismena = ["a", "b", "c", "d"] # list
vyskyt = [1, 10, 5, 0] # list
muj_slovnik_3 = {}.fromkeys(pismena, 0) # {"a": 0, "b": 0, "c": 0, "d": 0}
print(muj_slovnik_3)
muj_slovnik_x = {}.fromkeys(pismena, vyskyt)
print(muj_slovnik_x) # {'a': [1, 10, 5, 0], 'b': [1, 10, 5, 0], 'c': [1, 10, 5, 0], 'd': [1, 10, 5, 0]}
muj_zip = zip(pismena, vyskyt)
muj_slovnik_4 = dict(zip(pismena, vyskyt))
print(muj_slovnik_4) # {'a': 1, 'b': 10, 'c': 5, 'd': 0}

