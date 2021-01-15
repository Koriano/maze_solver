"""
Projet - Résolution d'un labyrinthe 2D/3D

Alexandre HAMON
Margaux SCHNELZAUER-HENRY

Bibliothèque contenant des fonctions utilitaires pour les bibliothèque de labyrinthe
"""


def listeVoisins(carte, i, j):
    """
    Fonction qui retourne la liste des voisins non-murs d'une case sépcifiée

    :param carte: Carte du labyrinthe             (numpy.ndarray)
    :param i: Première coordonnée de la case    (int)
    :param j: Deuxième coordonnée de la case    (int)
    :return: Liste des voisins non-murs         (list)
    """

    h = carte.shape[0]    # Hauteur de la matrice
    l = carte.shape[1]    # Largeur de la matrice
    voisins=[]       # Variable de retour

    # Voisin Sud
    if i+1 < h and carte[i + 1][j] != -1:
        voisins.append((i+1, j))

    # Voisin Est
    if j+1 < l and carte[i][j + 1] != -1:
        voisins.append((i, j+1))

    # Voisin Nord
    if 0 <= i-1 and carte[i - 1][j] != -1:
        voisins.append((i-1, j))

    # Voisin Ouest
    if 0 <= j-1 and carte[i][j - 1] != -1:
        voisins.append((i, j-1))

    # Voisin Sud-Est
    if i+1 < h and j+1 < l and carte[i + 1][j + 1] != -1:
        voisins.append((i+1, j+1))

    # Voisin Nord-Ouest
    if 0 <= i-1 and 0 <= j-1 and carte[i - 1][j - 1] != -1:
        voisins.append((i-1, j-1))

    # Voisin Sud-Ouest
    if i+1 < h and 0 <= j-1 and carte[i + 1][j - 1] != -1:
        voisins.append((i+1, j-1))

    # Voisin Nord-Est
    if j+1 < l and 0 <= i-1 and carte[i - 1][j + 1] != -1:
        voisins.append((i-1, j+1))

    return voisins


def listeVoisinsEligibles(carte, i, j):
    """
    Fonction qui permet de lister les voisin éligibles d'une case.
    Une case est éligible lorsqu'un seul de ses voisins est déjà marqué (-2).
    Utilisé pour la génération en DFS.

    :param carte: Carte du labyrinthe             (numpy.ndarray)
    :param i: Première coordonnée de la case    (int)
    :param j: Deuxième coordonnée de la case    (int)
    :return: Liste des voisins eligibles        (list)
    """

    h = carte.shape[0]  # Hauteur de la matrice
    l = carte.shape[1]  # Largeur de la matrice
    eligibles = []   # Variable de retour

    # Voisin Sud
    if i+1 < h:

        new_i, new_j = i+1, j   # Coordonnées du voisin sud
        compteur = 1            # Compteur de voisins marqués

        # Voisin sud du voisin sud
        if new_i+1 < h and carte[new_i + 1][new_j] == -2:
            compteur += 1

        # Voisin Est du voisin sud
        if compteur < 2 and new_j+1 < l and carte[new_i][new_j + 1] == -2:
            compteur += 1

        if compteur < 2 and 0 <= new_j-1 and carte[new_i][new_j - 1] == -2:
            compteur += 1

        if compteur == 1:
            eligibles.append((new_i, new_j))

    # Voisin Est
    if j+1 < l:

        new_i, new_j = i, j+1   # Coordonnées du voisin Est
        compteur = 1            # Compteur de voisins marqués

        # Voisin Sud du voisin Est
        if new_i+1 < h and carte[new_i + 1][new_j] == -2:
            compteur += 1

        # Voisin Est du voisin Est
        if compteur < 2 and new_j+1 < l and carte[new_i][new_j + 1] == -2:
            compteur += 1

        # Voisin Nord du voisin Est
        if compteur < 2 and 0 <= new_i-1 and carte[new_i - 1][new_j] == -2:
            compteur += 1

        if compteur == 1:
            eligibles.append((new_i, new_j))

    # Voisin Nord
    if i-1 >= 0:

        new_i, new_j = i-1, j   # Coordonnées du voisin Nord
        compteur = 1            # Compteur de voisins marqués

        # Voisin Est du voisin Nord
        if new_j+1 < l and carte[new_i][new_j + 1] == -2:
            compteur += 1

        # Voisin Nord du voisin Nord
        if compteur < 2 and 0 <= new_i-1 and carte[new_i - 1][new_j] == -2:
            compteur += 1

        # Voisin Ouest du voisin Nord
        if compteur < 2 and 0 <= new_j-1 and carte[new_i][new_j - 1] == -2:
            compteur += 1

        if compteur == 1:
            eligibles.append((new_i, new_j))

    # Voisin Ouest
    if j-1 >= 0:

        new_i, new_j = i, j-1   # Coordonnées du voisin Ouest
        compteur = 1            # Compteur de voisins marqués

        # Voisin Sud du voisin Ouest
        if new_i+1 < h and carte[new_i + 1][new_j] == -2:
            compteur += 1

        # Voisin Nord du voisin Ouest
        if compteur < 2 and 0 <= new_i-1 and carte[new_i - 1][new_j] == -2:
            compteur += 1

        # Voisin Ouest du voisin Ouest
        if compteur < 2 and 0 <= new_j-1 and carte[new_i][new_j - 1] == -2:
            compteur += 1

        if compteur == 1:
            eligibles.append((new_i, new_j))

    return eligibles


def listeMurs(carte):
    """
    Cette fonction renvoie la liste des positions des murs dans une carte

    :param carte: Carte où se trouve les murs     (numpy.ndarray)
    :return: liste contenant la position des murs   (list)
    """

    murs = []

    # Parcours de la matrice
    for i in range(carte.shape[0]):
        for j in range(carte.shape[1]):

            # Repérage des murs
            if carte[i][j] == -1:
                murs.append((i, j))

    return murs
