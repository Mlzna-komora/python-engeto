# Pomocí modulu os napiš takový kód, který v aktuálním umístění vytvoří tyto tři prázdné adresáře:
# 1. obrázky
# 2. texty
# 3. gify


import os # knihovna na info o systému, mylsím
jmena_slozek = ["obrazky", "texty", "gify"]
for promenna in jmena_slozek:
    if promenna is str:
        print("Složka již existuje!")
    else:
        print(f"Tvořím novou složku: {promenna}")
