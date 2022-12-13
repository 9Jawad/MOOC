from math import sqrt
from random import randint
import turtle

maximum = 100
releve = int(input("la pluie relevé était de : "))
if releve > maximum:
    maximum = releve
    print("Nouveau record de pluie atteint aujourd'hui !", maximum, "ml")
else:
    print("le maximum reste inchangé")

# -------------------------

x = int(input())
if x > 0:
    print("la valeur de x est positive")
elif x == 0:
    print("la valeur de x n'est ni positif, ni négatif !")
else:
    print("la valeur de x est négative")

# -----------------------

type(False)
type(True)  # réponse -------> <class 'bool'>

# ---------------bonus-------------

ans = int(input("Donnez l'année que vous voulez tester : "))
if ans % 4 == 0:
    print("l'année", ans, "est bissextile")
else:
    print("l'année", ans, " n'est pas bissextile")

# --------------bonus----------------

"""
Auteur : Jawad Cherkaoui
Date : 22/09/22
But : réaliser un programme qui résout les équation du second degré
Entrée : a,b,c
Sortie : Les valeurs de x 
"""

# from math import sqrt
a = float(input("\n Veuillez entrer la valeur de a : "))
b = float(input("\n Veuillez entrer la valeur de b :"))
c = float(input("\n Veuillez entrer la valeur de c : "))

delta = b**2 - (4*a*c)


if delta < 0:
    print("Il n'existe aucune racine dans les réels pour cette équation du second degré ")

elif delta == 0:
    print("la racine est, x = ", -b/2*a)

else:
    racine = sqrt(delta)
    print("la première racine est, x1 = ", (-b+racine) / 2*a)
    print("la deuxième racine est, x2 = ", (-b-racine) / 2*a)
    print("Il n'existe aucune racine dans les réels pour cette équation du second degré ")
# -----> J'ai déplacé ma variable "racine" dans "else" car plus haut elle pourrait probablement
#       causer des problèmes, vu qu'elle est potentiellement négative


# from random import randint
secret = randint(0, 5)

devine = int(input("Entrez une valeur situé entre 0 et 5 : "))

if devine == secret:
    print("\ngagné !")
else:
    print("\nperdu ! La valeur était : ", secret)


# ---------------3.1----------------

a = int(input())
b = int(input())
c = int(input())

if a == b:
    print(a)

elif b == c:
    print(b)

elif c == a:
    print(c)

# ---------------3.2----------------

temperature = int(input())

if temperature > 0:
    if temperature <= 10:
        print("Il va faire frais.")

else:
    print("Il va faire froid.")

# ---------------3.3----------------

a = int(input())
b = int(input())
c = int(input())

if c == 1:
    print(a+b)
elif c == 2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4:
    print(a**2 + a*b)
else:
    print("Erreur")

# ---------------3.4----------------

x = int(input())

if x % 2 == 0:
    print("True")
elif x % 2 != 0:
    print("False")

# --------------3.5-----------------

a = int(input())
b = int(input())

if a > 0 and b > 0:
    if a % b == 0:
        print("False")
    elif b % a == 0:
        print("False")
    else:
        print("True")

# --------------3.6-----------------
# from math import sqrt
a = float(input())
b = float(input())

if a >= 0 and b >= 0:
    moy_geo = sqrt(a*b)
    print(moy_geo)
elif a < 0 or b < 0:
    print("Erreur")


# --------------3.7 MA VERSION-----------------

# from random import randint

print("Pour rappel,parier sur un nombre entre 0 et 12 signifie que vous pariez sur le numéro correspondant.")
print("13 : Vous pariez sur pair.")
print("14 : Vous pariez sur impair.")
print("15 : Vous pariez sur la couleur rouge.")
print("16 : Vous pariez sur la couleur noire.\n")

a = int(input("Vous pariez sur : "))
b = randint(0, 12)
c = randint(0, 1)
# 0=rouge, 1=noir

mise = 10

if 0 <= a <= 12:
    if a == b:
        print("BINGO !, votre mise actuelle : ", mise*12, "euros.")
    elif a != b:
        print("Dommage !, votre mise actuelle : ", mise-10, "euros.")
        print("le chiffre était : ", b)

elif 12 < a <= 16:
    if a == 13:
        if b % 2 == 0:
            print("Félicitation !, votre mise actuelle : ", mise*2, "euros.")
            print("Le nombre était bien pair.")
        elif b % 2 != 0:
            print("Dommage !, votre mise actuelle : ", mise-10, "euros.")
            print("Le nombre était impair.")
            print("le chiffre était : ", b)
    elif a == 14:
        if b % 2 == 0:
            print("Dommage !, votre mise actuelle : ", mise-10, "euros.")
            print("Le nombre était pair.")
            print("le chiffre était : ", b)
        elif b % 2 != 0:
            print("Félicitation !, votre mise actuelle : ", mise*2, "euros.")
            print("Le nombre était bien impair.")
    elif a == 15:
        if c == 0:
            print("Félicitation !, votre mise actuelle : ", mise*2, "euros.")
            print("La couleur était bien rouge.")
        elif c == 1:
            print("Dommage !, votre mise actuelle : ", mise-10, "euros.")
            print("La couleur était rouge.")
            print("le chiffre était : ", b)
    elif a == 16:
        if c == 0:
            print("Dommage !, votre mise actuelle : ", mise-10, "euros.")
            print("La couleur était noir.")
            print("le chiffre était : ", b)
        elif c == 1:
            print("Félicitation !, votre mise actuelle : ", mise*2, "euros.")
            print("La couleur était bien noir.")

else:
    print("Erreur - Veuillez entrer une valeur entre 0 et 16")

# --------------3.7-----------------

a = int(input())
b = int(input())

mise = 10

if 0 <= a <= 12:
    if a == b:
        print(mise*12)
    elif a != b:
        print(mise-10)

elif 12 < a <= 16:
    if a == 13:
        if b % 2 == 0:
            print(mise*2)
        elif b == 0:
            print(mise*2)
        elif b % 2 != 0:
            print(mise - 10)
    elif a == 14:
        if b % 2 == 0:
            print(mise - 10)
        elif b == 0:
            print(mise - 10)
        elif b % 2 != 0:
            print(mise*2)
    elif a == 15:
        if b == 1 or b == 3 or b == 5 or b == 7 or b == 9 or b == 12:
            print(mise*2)
        else:
            print(mise - 10)
    elif a == 16:
        if b == 2 or b == 6 or b == 4 or b == 8 or b == 10 or b == 11:
            print(mise*2)
        else:
            print(mise - 10)

# --------------3.8------------------------

# from math import sqrt
lettre = input()
a = float(input())  # la longueur de l’arête du polyèdre

if lettre == "T":
    print((sqrt(2)/12)*a**3)
elif lettre == "C":
    print(a**3)
elif lettre == "O":
    print((sqrt(2)/3)*a**3)
elif lettre == "D":
    print((15 + 7*sqrt(5)/4)*a**3)
elif lettre == "I":
    print(((5*(3+sqrt(5)))/12)*a**3)
else:
    print("Polyèdre non connu")

# ------------------3.9-------------

nbr = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
while nbr != 42:
    print("Mauvaise réponse.")
    nbr = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
print("Bravo !")

# ------------------3.10-------------

a = int(input())
b = 0
tentative = 0
while a != -1:
    tentative = tentative + 1
    b += a
    a = int(input())

print(b/tentative)

# ----------------3.11 + 3.12------------

n = int(input())
tentative = 0
for val in range(n):
    print(tentative * " " + ((n-tentative)*"X"))
    tentative = tentative + 1

# ---------------3.13------------

a = int(input())

if a >= 0:
    res = 0
    for i in range(a):
        b = int(input())
        res += b
    print(res)

elif a == -1:
    res = 0
    b = input()
    while b != "F":
        res += int(b)
        b = input()

    print(res)

else:
    print()


# -------------3.14-----------

# from random import randint

vie = 6
nbr_secret = randint(0, 100)

n = int(input())

if 0 <= n <= 100:
    for boucle in range(vie):

        vie = vie - 1

        if vie == 0:
            if n != nbr_secret:
                print("Perdu ! Le secret était", nbr_secret)

            elif n == nbr_secret:
                print("Gagné en", (6 - vie) * '❤️', "essai(s) !")

        elif vie > 0:
            if n > nbr_secret:
                print("Trop grand")
                n = int(input())

            elif n < nbr_secret:
                print("Trop petit")
                n = int(input())

            else:
                print("Gagné en", (6 - vie) * '❤️', "essai(s) !")
                vie = 0

        else:
            print()
else:
    print()


# -------------------3.15----------------

saut = int(input())
position_cible = int(input())

if 1 < saut < 100 and 1 < position_cible < 100:

    position_courante = 0

    while position_courante != position_cible:
        position_courante += saut

        if position_courante == position_cible:
            print("Cible atteinte")

        elif position_courante >= 100:
            position_courante = position_courante % 100

            if position_courante == 0:
                print(position_courante)
                print("Pas trouvée")
                position_courante = position_cible

            elif position_courante == position_cible:
                print("Cible atteinte")

            else:
                print(position_courante)
        else:
            print(position_courante)


else:
    print()

# ----------------3.16---------------

n = int(input())

if n > 0:
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i*j, end=" ")
        print(" ")

# ------------------3.17-----------------

x = float(input())

n = 3
val = 1
val2 = 1
termes = 0
termes2 = 0
while abs(val) > 1e-6 and abs(val2) > 1e-6:
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    val = (-(x ** n) / fact)
    termes += val
    n = n + 2

    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    val2 = (x ** n) / fact
    termes2 += val2
    n = n + 2

print(x + termes + termes2)


# --------------------3.17--------------

nr = int(input())
for i in range(1, nr + 1):
    for a in range(nr - i):
        print(' ', end='')
    for b in range(i):
        print((i + b) % 10, end='')
    for c in range(i - 1, 0, -1):
        print(((i + c) - 1) % 10, end='')
    print()


# ----------------Turtle BONUS-------------

# import turtle

x = int(input("nombre de cotés du polygone : ", ))
for i in range(x):
    turtle.forward(100)
    turtle.left((x - 1) * 360/x)
turtle.done()

# -------------

# import turtle

x = int(input("nombre de cotés de l'étoile : ", ))
for i in range(x):
    turtle.forward(100)
    turtle.left((x - 1) * 180/x)
turtle.done()
