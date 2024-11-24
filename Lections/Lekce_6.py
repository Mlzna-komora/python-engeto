# Knihovny - kód, který můžu použt - lze nahrát
# Dělíme:
#   Moduly - soubor s příponou.py
#   Balíčky - celý adresář, který může obsahovat několik modulů
# Nahrávání knihoven: 
#           import<knihovna>
#           from<knihovna> import * - moc často napoužívané
#           from <knihovna> import <objekt>
#               např.: from matf import e,pi
#           from <knihovna> import <objekt> as <alias>
#               from <knihovna> import <EXTRA_DLOUHE_JMENO_KONSTANTY> as <alias>
#           import <knihonva> as <alias>

import math
# fce floor zaokrouhluje na celé nižší číslo
print(math.floor(1.456)) # 1
print(math.pi)

# Importované knihovny vždy dáváme na první řádky kódu!
# Nejprve se dávají importované standardní knihovna, potom oddělení volným řádkem a potom import vlastních knihoven
# Když chci spustit vlastní modul, je důležité nacházet se ve stejné složce jako je soubor, který spouštíme


# PRÁCE S MOJÍ VYTVOŘENOU KNIHOVNOU pomocne.py
# nechci spustit celou knihovnu, ale jen část
import pomocne
# po RUN: Proměnné:
# 11 Matous ['a', 'b', 'c']
# Nultý index:
# a


# MODULY - soubory s příponou .py
# modul pro práci s operačním systémem
import os  
  
# modul pro přístup k některým systémovým proměnným 
import sys

# modul pro práci s pseudo-náhodnými procesy    
import random  

print(
    "os" in dir() \
    and "sys" in dir() \
    and "random" in dir()
) # True - dir() ověření, že je import v aktuálním pracovním rámci a nahrané moduly jsou k dispozici
print("muj_modul" in dir()) # False - nějaký fiktivní muj_modul


# FCE dir() a help()
print(help(math))

import os
print(help(os.path))



# VÝPIS OBJEKTŮ - dir()
print(dir(math))
# ["__bases__", "__class__", "__delattr__", "__dir__", "__doc__", "__eq__", "__file__", "__format__", "__ge__", "__getattr__", "__getattribute__", "__gt__", "__hash__", "__init__", "__init_subclass__", "__le__", "__loader__", "__lt__", "__module__", "__name__", "__ne__", "__new__", "__package__", "__reduce__", "__reduce_ex__", "__repr__", "__setattr__", "__spec__", "__str__", "__subclasshook__", "acos", "acosh", "asin", "asinh", "atan", "atan2", "atanh", "ceil", "comb", "copysign", "cos", "cosh", "degrees", "dist", "e", "erf", "erfc", "exp", "expm1", "fabs", "factorial", "floor", "fmod", "frexp", "fsum", "gamma", "gcd", "hypot", "inf", "isclose", "isfinite", "isinf", "isnan", "isqrt", "ldexp", "lgamma", "log", "log10", "log1p", "log2", "modf", "nan", "perm", "pi", "pow", "prod", "radians", "sin", "sinh", "sqrt", "tan", "tanh", "trunc"]
# = list se všemi objekty, které jsou v rámci knihvny math


# BALÍČEK - sbírka několika modulů (souborů s příponou .py)

