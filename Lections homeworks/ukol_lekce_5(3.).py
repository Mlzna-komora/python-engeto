# Program, který vyžádá aritmetický operátor a následně čísla, se kterými celý zápis vypočítá
# Po každé operaci se program uživatele zeptá, zda chce provést další operaci nebo program ukončit


plus = "+"
minus = "-"
print(f"Sčítání:, {plus}")
print(f"Odečítání:, {minus}")
operation = input(f"Vyber operaci:")

# Nekonečná smyčka
while True:
    if operation not in (plus, minus):
        print("Nezadali jste platný operátor, zkuste to znovu")
        continue
    number_1 = int(input("Zadej 1. číslo:"))
    number_2 = int(input("Zadej 2. číslo:"))
    if operation == plus:
        print(f"{number_1} + {number_2} = {number_1 + number_2}")
    elif operation == minus:
        print(f"{number_1} + {number_2} = {number_1 - number_2}")
        again = input("Chcete provést další operaci? (a pro ano, jakoukoliv jinou klávesu pro ne)")
        if again == "a":
            continue
        else:
            print("Ukončuji...")
            break
