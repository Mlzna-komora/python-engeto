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
filmy = {           # nový slovník
    film_1['JMENO']: film_1, # jako jejich hodnoty jsme uložili celý slovník
    film_2['JMENO']: film_2,
    film_3['JMENO']: film_3,
    film_4['JMENO']: film_4
}
print(filmy.keys()) #dict_keys(['Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'The Prestige'])

#-------------------------------------------------------------------------------------------------------------------------------------

# UVÍTÁNÍ A VÝPIS NABÍDKY
uzivatel = input("Zadej jmeno: ")

if not uzivatel in uzivatele:
    print("neregistrovany uzivatel!")
    quit() # ukončení programu
else:
    print("V pořádku", oddelovac, sep="\n")
    print("Vitejte v nasem filmovem slovniku!".upper().center(62), # center - vycentruje str na určitý počet znaků (čára dlouhá 62 znaků a tu moji větu hodí doprostřed)
          oddelovac, sep="\n")
    print(("| " + " | ".join(sluzby) + " |").center(62), oddelovac, sep="\n") # metoda join = spojuje stringy/tuple/list.
#V tomto případě metoda join definuje, jakým znakem spojuji prvky v mém tuplu služby. Nejprve definuji znak '|'.join(sluzby), potom teprve píšu metodu join
# sep='\n' - začíná se na novém řádku 
# + spojuje stringy

#-------------------------------------------------------------------------------------------------------------------------------------

# VÝBĚR SLUŽBY A VÝPIS VŠECH DOSTUPNÝCH FILMŮ
vyber = input("Vyber sluzbu: ")

if vyber in sluzby and vyber == "dostupne filmy":
    print("DOSTUPNE FILMY:", ', '.join(tuple(filmy.keys())), oddelovac, sep="\n") # metoda keys vytáhne názvy filmů
else:
    print("vybrana sluzba neni v nabidce, ukoncuji..")


#-------------------------------------------------------------------------------------------------------------------------------------

# VYBER FILM A ZOBRAZ DETAILY O NĚM
vyber = input("Vyber sluzbu:")

if vyber in sluzby and vyber == "dostupne filmy":
    print("DOSTUPNE FILMY:", ', '.join(tuple(filmy.keys())), oddelovac, sep="\n") # TISK DOSTUPNÝCH FILMŮ

elif vyber in sluzby and vyber == "detaily filmu":
    print("DOSTUPNE FILMY:", ', '.join(tuple(filmy.keys())), sep="\n")
    film = input("Vyber film:") # 
    print(oddelovac, "FILM: " + film, filmy.get(film), oddelovac, sep="\n") # výbeř bude ve službávh a zároveň ten výběr bude detaily filmů
    # metoda get - abych nedostala error, když napíšu film, který není v databázi, ale dostanu výsledek none - nebo? takový film neznám
else:
    print("vybrana sluzba neni v nabidce, ukoncuji..")


#-------------------------------------------------------------------------------------------------------------------------------------


# VYBER VŠECHNY REŽISÉRY
vyber = input("Vyber sluzbu: ")

if vyber in sluzby and vyber == "dostupne filmy":
    print("DOSTUPNE FILMY:", ', '.join(tuple(filmy.keys())), oddelovac, sep="\n")

elif vyber in sluzby and vyber == "detaily filmu":
    print("DOSTUPNE FILMY:", ', '.join(tuple(filmy.keys())), sep="\n")
    film = input("Vyber film:")
    print(oddelovac, f"FILM: {film}", filmy.get(film), oddelovac, sep="\n")

elif vyber in sluzby and vyber == 'reziseri':
    reziseri = {filmy["Shawshank Redemption"]["REZISER"],
                filmy["The Godfather"]["REZISER"],
                filmy["The Dark Knight"]["REZISER"],
                filmy["The Prestige"]["REZISER"]}
    print(', ' .join(reziseri), oddelovac, sep="\n") # nový elif - nová proměnná reziseri a udělám set  (začátek a konec složené závorky)
    # join(reziseri) - oddělené čárkou
    # v setu může být pouze jeden unikátní režisér, proto mi to vytiskne 3 režiséry a ne 4, kde by jeden byl napsaný 2x
else:
    print("Vybrana sluzba neni v nabidce, ukoncuji..", oddelovac, sep="\n")