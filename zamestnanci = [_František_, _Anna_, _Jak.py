zamestnanci = ['František', 'Anna', 'Jakub', 'Klára']

# 2.: Vypiš obsah zaměstnanci
print('Zaměstnanci na začátku: ', zamestnanci)

# 3.: Vytvořit kopii listu a pojmenovat ji zamestnanci_a
zamestnanci_a = zamestnanci.copy()
print(zamestnanci_a)

# 4.: Přidej do listu zamestnanci_a jména:
zamestnanci_a.insert(5, 'Anežka')
zamestnanci_a.insert(4, 'Bruno')
# NEBO: zamestnanci_a.append('Bruno')
print('Nová jména přidána: ', zamestnanci_a)

# 5.: Kopie listu zamestnanci
zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, 'Bruno')
print('Nová jména vložena: ', zamestnanci_b)
