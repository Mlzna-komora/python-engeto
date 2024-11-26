film_1 = {
    "JMENO": "Shawshank Redemption",
    "REZISER": "Frank Darabont",
    # Další detaily filmu
}
film_2 = {
    "JMENO": "The Godfather",
    "REZISER": "Francis Ford Coppola",
    # Další detaily filmu
}
film_3 = {
    "JMENO": "The Dark Knight",
    "REZISER": "Christopher Nolan",
    # Další detaily filmu
}
film_4 = {
    "JMENO": "The Prestige",
    "REZISER": "Christopher Nolan",
    # Další detaily filmu
}

# Slovníky filmů
filmy_reziseri = {
    film_1["REZISER"]: film_1,
    film_2["REZISER"]: film_2,
    film_3["REZISER"]: film_3,
    film_4["REZISER"]: film_4
}

filmy = {
    film_1['JMENO']: film_1,
    film_2['JMENO']: film_2,
    film_3['JMENO']: film_3,
    film_4['JMENO']: film_4
}

# Výběr služby
dostupne_filmy = input('Výběr služby dostupné filmy? ano/ne').strip().lower()
detaily_filmu = input('Výběr služby detaily filmu? ano/ne').strip().lower()
reziseri = input('Výběr služby režiséři? ano/ne').strip().lower()
doporuc_film = input('Výběr služby doporuč film? ano/ne').strip().lower()

# Podmínky na základě volby
if dostupne_filmy == 'ano':
    print("Dostupné filmy:")
    for film in filmy.keys():
        print(f"- {film}")
elif dostupne_filmy == 'ne' and detaily_filmu == 'ano':
    print("Detaily všech filmů:")
    for film, details in filmy.items():
        print(f"{film}: {details}")
elif dostupne_filmy == 'ne' and detaily_filmu == 'ne' and reziseri == 'ano':
    print("Filmy podle režiséra:")
    for reziser, details in filmy_reziseri.items():
        print(f"{reziser}: {details}")
elif dostupne_filmy == 'ne' and detaily_filmu == 'ne' and reziseri == 'ne' and doporuc_film == 'ano':
    print('Ještě nevím, jak doporučit film.')
else:
    print("Nebyla vybrána žádná služba.")
