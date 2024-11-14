oddelovac = "=" * 62

sluzby = ("dostupne filmy", "detaily filmu", 'reziseri', "doporuc film") # tuple

uzivatele = {
    "tomas": {"Shawshank Redemption", "The Godfather", "The Dark Knight"},
    "petr": {"The Godfather", "The Dark Knight"},
    "marek": {"The Dark Knight", "The Prestige"}
}

film_1 = {
    "JMENO": "Shawshank Redemption",
    "HODNOCENI": "93/100",
    "ROK": 1994,
    "REZISER": "Frank Darabont",
    "STOPAZ": 144,
    "HRAJI": ("Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler",
      "Clancy Brown", "Gil Bellows", "Mark Rolston", "James Whitmore",
      "Jeffrey DeMunn", "Larry Brandenburg"
     )
}

film_2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": ("Marlon Brando", "Al Pacino", "James Caan",
      "Richard S. Castellano", "Robert Duvall", "Sterling Hayden",
      "John Marley", "Richard Conte"
    )
}

film_3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": ("Christian Bale", "Heath Ledger", "Aaron Eckhart",
      "Michael Caine", "Maggie Gyllenhaal", "Gary Oldman", "Morgan Freeman",
      "Monique Gabriela", "Ron Dean", "Cillian Murphy"
    )
}

film_4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": ("Hugh Jackman", "Christian Bale", "Michael Caine",
      "Piper Perabo", "Rebecca Hall", "Scarlett Johansson", "Samantha Mahurin",
      "David Bowie"
    )
}

#-------------------------------------------------------------------------------------------------------------------------------------


# cílem je SPOJENÍ VŠECH SLOVNÍKŮ DO JEDNOHO SE JMÉNEM FILMY
# Spojíme všechny slovníky filmů do jednoho slovníku jménem filmy

filmy = {
    film_1['JMENO']: film_1,
    film_2['JMENO']: film_2,
    film_3['JMENO']: film_3,
    film_4['JMENO']: film_4
}
print(filmy)
print(filmy.keys()) #dict_keys(['Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'The Prestige']) - tisk pouze klíčů (všech)
#{
#    "Shawshank Redemption": film_1,
#    "The Godfather": film_2,
#    "The Dark Knight": film_3,
#    "The Prestige": film_4
#}


filmy_reziseri = {
    film_1["REZISER"]: film_1,
    film_2["REZISER"]: film_2,
    film_3["REZISER"]: film_3,
    film_4["REZISER"]: film_4
}




#-------------------------------------------------------------------------------------------------------------------------------------


# Uvítání a výpis nabídky
uzivatel = input('ZADEJ JMÉNO: ')


#sluzby = ("dostupne filmy", "detaily filmu", 'reziseri', "doporuc film") # tuple
# tomas, petr, marek
if uzivatel in uzivatele:
    print('V POŘÁDKU!')
else:
    print('NEPLATNÉ UŽIVATELSKÉ JMÉNO!')
    quit()

print(oddelovac)
print('VÍTEJTE V NAŠEM FILMOVÉM SLOVNÍKU'.center(62))
print(oddelovac)
print(("| " + " | ".join(sluzby) + " |").center(62), oddelovac, sep="\n") #
#==============================================================
#              VÍTEJTE V NAŠEM FILMOVÉM SLOVNÍKU               
#==============================================================
# | dostupne filmy | detaily filmu | reziseri | doporuc film | 
#==============================================================


#-------------------------------------------------------------------------------------------------------------------------------------


# CÍL: Výběr služby a výpis všech dostupných filmů

# OČEKÁVÁME:
#VYBER SLUZBU: dostupne filmy
#NASE FILMY: Shawshank Redemption, The Godfather, The Dark Knight, The Prestige


print(sluzby)
vyber_sluzby = input('Vyber službu: ')

if vyber_sluzby in sluzby == 'dostupne_filmy':
    print('DOSTUPNÉ FILMY: ', ','.join(tuple(filmy.keys())), oddelovac, sep='\n')
else:
    print('Vybraná služba není v nabídce, ukončuji...')







# ASI JE POTŘEBA NEJPRVE PŘIŘADIT DO VŠECH NÁSLEDUJÍCÍCH PROMĚNNÝCH TO, CO MAJÍ VYPSAT 

#vypis_dostupne_filmy: print(filmy.keys())

dostupne_filmy = input('Výběr služby dostupné filmy? ano/ne').strip().lower() # když uživatel napíše Ano/ANo/ano,..
detaily_filmu = input('Výběr služby detaily filmu? ano/ne').strip().lower()
reziseri = input('Výběr služby režiséři? ano/ne').strip().lower()
doporuc_film = input('Výběr služby doporuč film? ano/ne').strip().lower()

if dostupne_filmy == 'ano':
    print(filmy.keys())
    quit()
elif dostupne_filmy == 'ne' and detaily_filmu == 'ano':
    print(filmy)
    quit()
elif dostupne_filmy == 'ne' and detaily_filmu == 'ne' and reziseri == 'ano':
    print(filmy_reziseri) 
    quit()
elif dostupne_filmy == 'ne' and detaily_filmu == 'ne' and reziseri == 'ne' and doporuc_film == 'ano':
    print('Ještě nevím, jak doporučit film.')
    quit()


