# --------5.1 ----------
def signature(identique):
    return identique[1] + " " + identique[0]


# --------5.2 ----------


ADN = ['A', 'C', 'G', 'T']


def est_adn(chaine_cara):
    res = False
    for i in range(len(chaine_cara)):
        if chaine_cara[i] in ADN:
            res = True
        else:
            res = False
            break
    return res


# --------5.3----------


def duree(debut, fin):
    debut_tot = (debut[0] * 60) + debut[1]
    fin_tot = (fin[0] * 60) + fin[1]
    diff = fin_tot - debut_tot
    diff_2 = fin_tot + 1440 - debut_tot

    if debut_tot < fin_tot:
        return diff // 60, diff % 60
    else:
        return diff_2 // 60, diff_2 % 60


# --------- 5.4 -----------

from math import sqrt


def distance_points(point_1, point_2):
    dist = sqrt((((point_1[0]) - (point_2[0])) ** 2) + (((point_1[1]) - (point_2[1])) ** 2))
    return dist


# ----------5.5-----------
# from math import sqrt


def longueur(*points):
    dist = 0
    n = 0
    while n + 1 < len(points):
        a, b = points[n]
        c, d = points[n + 1]
        dist_1 = sqrt(((c - a) ** 2) + ((d - b) ** 2))
        dist += dist_1
        n += 1
    return dist


# --------------5.6---------------


def transcription_clavier(texte):
    n = 0
    for i in texte:
        if i == '%':
            texte = texte[:n] + "M" + texte[n + 1:]
        n += 1
    return texte


# ---------------5.7----------------


def plus_grand_bord(w):
    t = len(w) - 1
    res = 0
    if w[0] == w[t]:
        for i in range(0, len(w) - 1):
            if w[:i + 1] == w[t - i:t + 1]:
                res = w[:i + 1]
    # normalement je dois faire une boucle for mais flemme tu connais
    elif w[0] != w[t]:
        if w[0:2] == w[t - 1:t + 1]:
            res = w[0:2]
        else:
            res = ""
    return res


# ---------------5.8----------------


def prime_numbers(nb):
    liste = []
    if type(nb) != int or nb < 0:
        return None
    else:
        y = 1
        res = 0
        while len(liste) < nb:
            if res:
                liste.append(y)
            y += 1
            if y == 2:
                res = True
            else:
                for i in range(2, y):
                    if y % i == 0:
                        res = False
                        break
                    else:
                        res = True

    return liste


# ---------------5.9---------------

def anagrammes(v, w):
    res = False
    for letter in v:
        if len(w) == len(v) and v.count(letter) == w.count(letter):
            res = True
        else:
            return False

    return res


# -------------5.10-------------


def dupliques(sec):
    res = False
    for i in sec:
        if sec.count(i) == 1:
            res = False
        else:
            return True

    return res


# -------------5.11------------ PROBLEM


def intersection(v, w):
    mot1 = list(v)
    mot2 = list(w)
    res = []
    res_temp =[]

    for lettre in mot1:
        if lettre in mot2:
            res_lst = []
            ordre1 = [i for i in range(len(mot1)) if mot1[i] == lettre]
            ordre2 = [i for i in range(len(mot2)) if mot2[i] == lettre]

            for pos1 in ordre1:
                for pos2 in ordre2:
                    res_lst = []
                    for k in range(min(len(mot1)-pos1, len(mot2)-pos2)):
                        if mot1[pos1+k] == mot2[pos2+k]:
                            res_lst.append(mot1[pos1+k])
                        else:
                            break
                    txt = ''.join(res_lst)
                    res_temp.append(txt)
                res.extend(res_temp)
                res_temp = []

    if res != []:
        final = max(res,key=len)
    else:
        final = ''

    return final


# -----------------5.12------------


def my_insert(lst, n):
    if type(lst) == list and type(n) == int:
        l = lst.copy()
        l.append(n)
        l.sort()
        res = l
    else:
        res = None
    return res


# ------------------5.13----------------

def my_insert_2(lst, n):
    assert isinstance(lst, list) and isinstance(n, int)
    l = lst.copy()
    l.append(n)
    l.sort()
    return l


# ---------------5.14------------------


def distance_mots(mot_1, mot_2):
    x = 0
    if len(mot_1) == len(mot_2):
        for i in range(len(mot_1)):
            if mot_1[i] == mot_2[i]:
                x += 0
            else:
                x += 1
    return x


# ----------------5.15-----------------


def correcteur(mot, liste_mots):
    if mot in liste_mots:
        return mot
    else:
        lst = []
        res = []
        for i in liste_mots:
            if len(mot) == len(i):
                lst.append(i)
        for i in lst:
            x = 0
            for j in range(len(mot)):
                if mot[j] in i:
                    x += 1
            res.append(x)
    return lst[res.index(max(res))]


# ---------------5.16------------------


def my_pow(m, b):
    if type(m) == int and type(b) == float:
        m = [b ** i for i in range(m)]
    else:
        return None
    return m

# ---------------5.17------------------


def decompresse(t):
    n = 0
    solution = []
    while n < len(t):
        for i in range(t[n][0]):
            solution.append(t[n][1])
        n += 1
    return solution

# ---------------5.18---------------------


def my_filter(lst, f):
    return [i for i in lst if f(i)]

# ---------------5.19---------------------


def acrostiche(nom_fichier):
    res = ''
    with open(nom_fichier, encoding='utf-8') as fichier:
        for text in fichier:
            res += text[0]
    return res

# ---------------5.20---------------------


def nouveaux_heros(hist_in, hist_ou):
    with open(hist_in, encoding='utf-8') as histoire:
        modif = histoire.read()
        modif = modif.replace('Paul', 'Tom')
        modif = modif.replace('Pierre', 'Paul')
        modif = modif.replace('Jacqueline', 'Mathilde')
        f = open(hist_ou, 'w', encoding='utf-8')
        f.write(modif)

    return hist_ou


# ---------------5.21---------------------

def liste_des_mots(nom_fichier):
    erreur = set(list('- \' " ? ! : ; . , * = ( ) 1 2 3 4 5 6 7 8 9 0'))
    with open(nom_fichier, encoding='utf-8') as fichier:
        story = fichier.read().lower()
        for n in erreur:
            story = story.replace(n, ' ')
    return sorted(set(story.split()))

# ---------------5.22---------------------


def wc(nomFichier):

    nb_lignes = len(open(nomFichier, 'r').readlines())
    nb_car = len(open(nomFichier, 'r').read())

    with open(nomFichier, encoding='utf-8') as fichier:
        text = fichier.read()

        for i in text:
            if not i.isalnum():
                text = text.replace(i, ' ')
    nb_mots = len(text.split())

    return nb_car, nb_mots, nb_lignes

# ---------------5.23---------------------


def init_mat(m, n):
    return [[0]*n for i in range(m)]

# ---------------5.24---------------------


def print_mat(M):
    if len(M) == 0:
        print("")
    else:
        for i in range(len(M)):
            for j in range(len(M[0])):
                print(M[i][j], end=" ")
            print("")


ma_matrice = eval(input())
print_mat(ma_matrice)

# ---------------5.25---------------------


def trace(M):
    if len(M) == 0:
        return 0
    else:
        res = 0
        for i in range(len(M)):
            res += M[i][i]
        return res

# ---------------5.26---------------------


def antisymetrique(M):
    if len(M) == 0:
        return True
    else:
        res = False
        for i in range(len(M)):
            for j in range(len(M[0])):
                if j % 2 == 0 or i % 2 == 0 and M[j][j] == 0:
                    res += M[j][i]
    return res == 0

# ---------------5.27---------------------


def symetrie_horizontale(A):
    n = len(A)
    return [[A[j][i] for i in range(n)] for j in range(n-1, -1, -1)]
