"""
Auteur : Jawad Cherkaoui
Date : 18/09/22
But du programme :
Le programme suivant calcule la quantité nécessaire pour la réalisation d'une mousse au chocolat et
il calcule également la circonférence et l'air d'un cercle.
Entrée : le nombre d'o, la quantité de sachet de sucre, la quantité de chocolat et le rayon d'un cercle.
Sorties : les nouvelles quantités pour la mousse au chocolat et l'air ainsi que la circonférence du cercle.
"""

# exercices 2.4 - Code avec Variable
n = int(input("entrez le nombre de personnes : "))
oeufs = 3 * n // 4
chocolat = 100 * n // 4
sucre_vanille = n // 4
print("nombres d'oeufs : ", oeufs)
print("grammes de chocolat : ", chocolat)
print("sachet de sucre vanille : ", sucre_vanille)


# --------------AUTRE_EXEMPLE---------------------

# import math   ----->  math.pi
# ou
# from math import pi -----> pi

rayon = float(input("entrez en valeur decimal le rayon du cercle : "))
pi = 3.14159
air = pi * rayon ** 2
peri = pi * 2 * rayon
print("\nl'air du cercle : ", air, "mètres carré.\n")
print("\nla superficie du cercle : ", peri, "mètres.\n")

# ---------------2.5.5--------------
x = 36
produit = 36*36
div_entiere = 36//5
expo = 15**15
pi = 3.14159
mon_texte = "Bonjour"

# ---------------2.5.6--------------

a = float(input())
b = float(input())
moyenne_arithmetique = (a+b)/2
print(moyenne_arithmetique)

# ---------------2.5.7--------------

a = float(input())
b = float(input())
c = float(input())
d = (c/a)*b
print(d)

# ---------------2.6.3---------------
import turtle

turtle.begin_fill()
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.right(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)
turtle.end_fill()
turtle.color("red")
turtle.begin_fill()
turtle.right(60)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.end_fill()
turtle.color("blue")
turtle.begin_fill()
turtle.right(120)
turtle.left(60)
turtle.forward(100)
turtle.right(120)
turtle.forward(100)

# ---------------2.4-----------

from math import sin, cos, pi
long = float(input())
print(long * cos(0), long * sin(0))
print(long * cos(pi / 3), long * sin(pi / 3))
print(long * cos(pi * 2 / 3), long * sin(pi * 2 / 3))
print(long * cos(pi), sin(pi))
print(long * cos(pi*4/ 3), long * sin(pi*4/ 3))
print(long * cos(pi*5/3), long * sin(pi*5/3))

# ---------------------------------------

print('\n\nBonjour\n\n')
# retour à la ligne avec /n

# ---------------2.7.4-------------------

b = int(input())
y = int(input())
z = float(input())
t = float(input())

print(b-y)
print(b+z)
print(b+t)
print(b*z)
print(b/2)
print(b/(y+1))
print(((b+y)*z)/(4*b))
print(b**(-1/2))

# ------------------2.7.5-----------------

print("Hello World")
print("Aujourd'hui")
print("C'est \"Dommage !\"")
print("Hum \\o/")

# ------------2.7.6-------------------
from math import pi
r = float(input())
volume = (4/3)*pi*r**3
print(volume)
