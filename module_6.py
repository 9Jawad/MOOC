# ---------------6.1--------------


def inventaire(offres, objets):
    res = set()
    for i in objets:
        if i in offres:
            res.add(offres[i])
    return res

# ---------------6.2--------------


def calcul_prix(produits, catalogue):
    res = 0
    for i in produits:
        if i in catalogue:
            res += produits[i] * catalogue[i]
    return res

# ---------------6.3--------------


def top_3_candidats(moyennes):
    res = []
    n = len(moyennes)
    lst = sorted(moyennes.values())
    lst = lst[n-3:]
    lst.reverse()
    for i in range(3):
        for keys in moyennes:
            if moyennes[keys] == lst[i]:
                res.append(keys)
    return tuple(res)

# ---------------6.4--------------


def substitue(message, abreviation):
    n = message.split()
    res = " "
    for keys in n:
        if keys in abreviation:
            res += abreviation[keys] + " "
        else:
            res += keys + " "
    return res.strip()

# ---------------6.5--------------


def construction_dict_amis(liste_couple):
    relation = {}
    for prenom1, prenom2 in liste_couple:
        if prenom1 not in relation:
            relation[prenom1] = {prenom2}
        elif prenom1 in relation:
            relation[prenom1].add(prenom2)

        if prenom2 not in relation:
            relation[prenom2] = set()
    return relation

# ---------------6.6-------------- FONCTIONNE MAIS CE FDP A DIT DE MODIF LE MEME DICO


def symetrise_amis_ESSAI(d, englobe):
    amis = {}
    if englobe:
        for i in d:
            n = list(d[i])
            for j in n:
                if j not in amis:
                    amis[j] = {i}
                if i not in amis:
                    amis[i] = {j}
                else:
                    amis[j].add(i)
                    amis[i].add(j)
    else:
        for i in d:
            n = list(d[i])
            for j in n:
                if j not in amis:
                    if d[j] == {i}:
                        amis[i] = {j}
                        amis[j] = {i}
                    else:
                        amis[j] = set()
                else:
                    if d[j] == {i}:
                        amis[i].add(j)
                        amis[j].add(i)
    return amis


# ---------------6.6-------------- """""""""VERSION CORRECT""""""""


def symetrise_amis(d, englobe):
    for prenom in d:
        for ami in d[prenom].copy():
            if englobe:
                d[ami].add(prenom)
            else:
                if prenom not in d[ami]:
                    d[prenom].discard(ami)

# ---------------6.7--------------


def prime_odd_numbers(numbers):
    res_1 = set()
    res_2 = set()
    for i in numbers:
        if i not in even(i):
            res_1.add(i)
        if i in prime_numbers(i):
            res_2.add(i)
    return res_2, res_1


def even(n):
    set_even = set()
    for i in range(0, n+1):
        if i % 2 == 0:
            set_even.add(i)
    return set_even


def prime_numbers(n):
    res = None
    prime_set = set()
    for i in range(n + 1):
        if i == 2:
            res = True
        elif i > 2:
            for j in range(2, i):
                if i % j == 0:
                    res = False
                    break
                else:
                    res = True
        if res:
            prime_set.add(i)
    return prime_set

# ---------------6.8--------------


def store_email(liste_mails):
    d = {}
    lst = liste_mails
    for i in range(len(lst)):
        n = lst[i].index("@")
        if lst[i][n+1:] not in d:
            d[lst[i][n+1:]] = [lst[i][:n]]
        else:
            d[lst[i][n + 1:]].append(lst[i][:n])
    a = list(d.keys())
    b = list(d.values())
    for x in range(len(b)):
        b[x] = sorted(b[x])
    t = []
    for i in range(len(b)):
        t.append((a[i], b[i]))
    return dict(t)

# ---------------6.9-------------


def compteur_lettres(texte):
    dico = {}.fromkeys("abcdefghijklmnopqrstuvwxyz", 0)  # création d'un dico avec l'alphabet

    text = texte  # nettoyage du texte (seulement alphabet)
    for i in text:
        if not i.isalpha():
            text = text.replace(i, "").lower().strip()

    for j in text:
        dico[j] = dico.get(j) + 1

    return dico

# ---------------6.10-------------


def valeurs(dico):
    res = []
    a = sorted(list(dico.keys()))
    for i in range(len(a)):
        res.append(dico[a[i]])
    return res

# ---------------6.11-------------


def bonne_planete(diametre):
    res = False
    r = 4 * 3.1415 * (diametre/2)**2
    if r > 50000:
        res = True
    return res


n = int(input())
if bonne_planete(n):
    print("Bonne planète")
else:
    print("Trop petite")


# ---------------6.12-------------


def belongs_to_file(word, filename):
    res = False
    if word in open(filename, encoding='utf-8').read().split():
        res = True
    return res

# ---------------6.13-------------


# ---------------6.14-------------


def placer_pion(couleur, colonne, grille):
    res = False
    for i in range(len(grille)):
        if grille[i][colonne] == 'V':
            res = True
            grille[i][colonne] = couleur
            break

    return res, grille

# --------------6.15-------------------


def gagnant(grille):
    # PAS OPTI MAIS FRANGIN CA ME CLC
    # GAGNE SUR LA LIGNE
    res = None
    for i in range(6):
        for j in range(4):
            if grille[i][j] == grille[i][j+1] == grille[i][j+2] == grille[i][j+3]:
                if grille[i][j] != 'V':
                    res = grille[i][j]
                    return res

    # GAGNE SUR LA COLOGNE
    for i in range(3):
        for j in range(7):
            if grille[i][j] == grille[i+1][j] == grille[i+2][j] == grille[i+3][j]:
                if grille[i][j] != 'V':
                    res = grille[i][j]
                    return res

    # GAGNE SUR LA DIAGONALE
    for i in range(3):
        for j in range(4):
            if grille[i][j] == grille[i+1][j+1] == grille[i+2][j+2] == grille[i+3][j+3]:
                if grille[i][j] != 'V':
                    res = grille[i][j]
                    return res

    # GAGNE SUR LA DIAGONALE DE L'AUTRE SENS
    for i in range(3):
        for j in range(6, 2, -1):
            if grille[i][j] == grille[i+1][j-1] == grille[i+2][j-2] == grille[i+3][j-3]:
                if grille[i][j] != 'V':
                    res = grille[i][j]
                    return res
    return res

# ---------------6.16------------------


