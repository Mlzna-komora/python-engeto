# METODY
# Metody stringu
print(dir(str))

print(dir(str))
text = "A"
print(dir(text))

print("matous".upper()) # MATOUS
print("MATOUS".lower()) # matous

# CVIČENÍ 1:
mail = "matous.holinka@gmail.com" # chci zo toho dostat jen "matous.holinka"
print(mail)

rozdeleny_mail = mail.split("@") # split - rozsekne zadaný string nebo textový řetězec - v tomto případě rozsekne na @
print(rozdeleny_mail) # ['matous.holinka', 'gmail.com'] dostávám, ale já chci jen první věc
jmeno = rozdeleny_mail[0]
print(jmeno) # matous.holinka

# mám nahradit v "matous.holinka" znakem "." pomocí mezery " "
jmeno_upravene = jmeno.replace(".", " ")
print(jmeno_upravene) # matous holinka

# nakonec to vypsat pomocí metody title
print(jmeno_upravene.title()) # Matous Holinka

print("matous.holinka@gmail.com".split("@")[0].replace(".", " ").title()) # alternativně vše nahoře zapsat do jednoho řádku


# CVIČENÍ 2:
zaznam = "Ota; Petr; Pavel"
print(zaznam)
seznam_jmen = (zaznam.split(";"))
print(seznam_jmen)
seznam_jmen.insert(0, 'Johny')
print(seznam_jmen)
seznam_jmen.append('Jane')
print(seznam_jmen)