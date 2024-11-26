# Pomocí modulu os napiš takový kód, který v aktuálním umístění vytvoří tyto tři prázdné adresáře:
# 1. obrázky
# 2. texty
# 3. gify


import os # knihovna na info o systému, mylsím
jmena_slozek = ("obrazky", "texty", "gify")
for promenna in jmena_slozek:
    if promenna is str:
        print("Složka již existuje!")
    else:
        print(f"Tvořím novou složku: {promenna}")
print("Všechny složky existují.") # ŠPATNĚ - nepochopila jsem zadání moc


# vytvoř všechny adresáře v sekvenci `jmeno_slozek`
for promenna in jmena_slozek:
    if os.path.exists(promenna) and os.path.isdir(promenna):
        print("Složka již existuje") # fce os.path.exist() kontroluje, zda cesta existuje, fce os.pat.isdir() ověřuje, zda se jedná o adresář
    else: 
        print("Tvořím novou složku:", promenna)
        os.mkdir(promenna) # Pokud některá složka neexistuje, vytvoří ji pomocí funkce os.mkdir()
    
# jakmile budou všechny složky vytvořené, vypiš oznámení
print("Všechny složky existují")
