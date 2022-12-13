# ----------4.1-------------

def deux_egaux(a, b, c):
    return a == b or b == c or a == c


x = int(input())
y = int(input())
z = int(input())
egaux = deux_egaux(x, y, z)

if egaux:
    print("True")
else:
    print("False")


# ----------4.2A------------


def leve_soleil(a, b, c):
    if a > b:
        return a == c or not (b <= c <= a)
    else:
        return a <= c < b or a == b == 0


# ----------4.2B------------


def soleil_leve(a, b, c):
    if a > b:
        return a == c or not (b <= c <= a)
    else:
        return a <= c < b or a == b == 0


x = int(input())
y = int(input())
z = int(input())
w = int(input())

for i in range(24):
    if soleil_leve(x, y, i) or soleil_leve(z, w, i):
        print(i)
    else:
        print(i, "*")


# ------------------4.3------------------


def premier(n):
    res = 0

    if n == 2:
        res = True

    for i in range(2, n):
        if n % i == 0:
            res = False
            break
        else:
            res = True

    return res


y = int(input())
for i in range(2, y):
    if premier(i):
        print(i)


# --------------4.4--------------------


from random import randint, seed


def alea_dice(s):
    res = 0
    seed(s)
    a = randint(1, 6)
    b = randint(1, 6)
    c = randint(1, 6)

    if a == b or a == c or b == c:
        return False

    if a == 1 or a == 2 or a == 4:
        res = True
        if b == 1 or b == 2 or b == 4:
            res = True
            if c == 1 or c == 2 or c == 4:
                res = True
            else:
                res = False
        else:
            res = False
    else:
        res = False

    return res


x = int(input())
print(alea_dice(x))


# --------------4.5----------------

def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    argent = (x20 * 20) + (x10 * 10) + (x5 * 5) + (x2 * 2) + (x1 * 1)

    if prix == argent:
        return 0, 0, 0, 0, 0
    elif prix > argent:
        return None, None, None, None, None
    else:
        rendu = argent - prix
        res20 = 0
        while rendu // 20 > 0:
            rendu -= 20
            res20 += 1
        res10 = 0
        while rendu // 10 > 0:
            rendu -= 10
            res10 += 1
        res5 = 0
        while rendu // 5 > 0:
            rendu -= 5
            res5 += 1
        res2 = 0
        while rendu // 2 > 0:
            rendu -= 2
            res2 += 1
        res1 = 0
        while rendu // 1 > 0:
            rendu -= 1
            res1 += 1
        return res20, res10, res5, res2, res1

# -------------4.6---------------------


def somme(a='1', b='1'):
    return int(a) + int(b)


# -----------------4.7------------------

from math import sqrt


def rac_eq_2nd_deg(a, b, c):

    delta = b ** 2 - (4 * a * c)

    if delta < 0:
        return ()

    elif delta == 0:
        return -b / 2 * a,

    else:
        racine = sqrt(delta)
        r = ((-b + racine) / (2 * a))
        t = ((-b - racine) / (2 * a))
        if r > t:
            return t, r

        else:
            return r, t


# -----------------4.8----------------
from math import factorial


def catalan(x):
    res = (factorial(2 * x))/(factorial((x + 1)) * factorial(x))
    return res


# ------------------4.9--------------------

def bat(joueur_1, joueur_2):
    a = joueur_1
    b = joueur_2

    if a > b:
        if a == 2 and b == 1:
            return True
        elif a == 1 and b == 0:
            return True
        else:
            return False
    elif a == 0 and b == 2:
        return True
    else:
        return False

# ---------------4.10-------------------

import random  # module les tirages aléatoires

PIERRE = 0
FEUILLE = 1
CISEAUX = 2
MANCHE = 5
KEYWORDS = ("Pierre", "Feuille", "Ciseaux")


def bats(joueur1, joueur2):
    """Retourne vrai si j1 bat j2, sinon retourne faux"""
    return joueur1 % 3 == (joueur2 + 1) % 3


def manche(points):
    """Réalise une manche de pierre feuille ciseaux, et retourne les points nouveaux."""

    coup_j, coup_o = int(input()), random.randint(0, 2)

    if bats(coup_j, coup_o):  # vérifie dans quel cas on est
        points, message = points + 1, "est battu par"
    elif coup_j == coup_o:
        message = "annule"
    else:
        points, message = points - 1, "bat"

    print(KEYWORDS[coup_o], message, KEYWORDS[coup_j], ":", points)  # imprime le cas au joueur
    return points


def jeu():
    """fonction appellant un joueur a jouer x MANCHES de pierre feuille ciseaux
    contre un ordinateur, et affiche selon que le joueur a gagné ou non. """
    points = 0
    for i in range(MANCHE):  # on appelle la fonction manche x fois
        points = manche(points)

    if points > 0:  # vérifie si le joueur a gagné ou non
        message_final = "Gagné"
    elif points == 0:
        message_final = "Nul"
    else:
        message_final = "Perdu"
    print(message_final)


# programme principal
s = int(input())
random.seed(s)
jeu()


