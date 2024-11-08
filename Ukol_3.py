user_1 = {}
print(type(user_1)) # <class 'dict'> - OK

user_email = {'email': 'marek.parek@gmail.com'}

user_1['name'] = 'Marek'
user_1['surname'] = 'Parek'

user_1.update(user_email) # rozšíření user_1 o další slovním user_email
print(user_1)
print('User #01:', user_1) # User #01: {'name': 'Marek', 'surname': 'Parek', 'email': 'marek.parek@gmail.com'}


# OVĚŘENÍ, ŽE HESLO VLOŽENÉ UŽIVATELEM PATŘÍ K JEHO ÚČTU
jmeno = 'Marek' # = keys
heslo = '1234' # = values
uzivatel = {'Marek' : '1234'}

# if uzivatel.get(jmeno) == heslo: - ALTERNATIVA, metoda get vrátí hodnotu, pokud existuje zadaný klíč
if jmeno and heslo in uzivatel.values():
    print('Ahoj,', jmeno, ' vítej v aplikaci! Pokračuj...')
else:
    print('Uživatelské jméno nebo heslo nejsou v pořádku!')


cisla_1 = (1, 1, 2, 3, 4)
cisla_2 = (5, 6, 7, 7, 8)
set_cisla_1 = set(cisla_1)
set_cisla_2 = set(cisla_2)

print(type(set)) # <class 'set>
print(set)

sjednocene_hodnoty = set_cisla_1.union(set_cisla_2)
#print(cisla_1.union(cisla_2))
print(sjednocene_hodnoty)



cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}

set_cisla_1 = set(cisla_1)
set_cisla_2 = set(cisla_2)

rozdil_cisel = (set_cisla_1.difference(set_cisla_2))
print("rozdilné hodnoty prvního setu oproti druhemu:", rozdil_cisel)





