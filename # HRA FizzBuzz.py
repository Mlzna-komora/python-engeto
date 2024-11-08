# HRA FizzBuzz
cislo = int(input("Zadej číslo: "))
if cislo % 3 == 0 and cislo % 5 == 0:
    print("FizzBuzz")
elif cislo % 3 == 0: #zbytek po dělení 3 je nula, MODULO
    print("Fizz")
elif cislo % 5 == 0:
    print("Buzz")
elif cislo % 3 == 0 and cislo % 5 == 0:
    print("FizzBuzz")
else:
    print(cislo)