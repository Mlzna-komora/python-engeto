# Pro tuto úlohu budeš potřebovat nahrát knihovnu random. Tvým úkolem bude simulovat hod kostkou.

import random
min_hodnota = 1
max_hodnota = 6

# TODO: Vytvoření řízené nekonečné smyčky
while True:
    print("Házím kostkou...")
    kostka_hodnota = random.randint(min_hodnota, max_hodnota)
    print(f"Na kostce je: {kostka_hodnota}")
    if kostka_hodnota == 6:
        continue
    else:
        print("Konec")
        break