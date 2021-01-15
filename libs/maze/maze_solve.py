"""
Projet - Résolution d'un labyrinthe 2D/3D

Alexandre HAMON
Margaux SCHNELZAUER-HENRY

Bibliothèque servant à résoudre des labyrinthes
"""
# Built-in modules
import numpy as np


def carteDirectionnelle(carte):
    """
    Fonction qui génère la carte directionnelle à partir d'une carte initialisée avec Dijkstra.

    :param carte: Carte initialisée et remplie par Dijkstra (numpy.ndarray)
    :return: Carte directionnelle correspondante            (numpy.ndarray)
    """

    # Initialisation
    h = carte.shape[0]  # Hauteur de la carte
    l = carte.shape[1]  # Largeur de la carte
    carte_dir = np.full((h, l), None)   # On initialise le retour avec une carte remplie de None

    # On parcourt la carte
    for i in range(h):
        for j in range(l):

            # Si la case ne correspond pas à un mur, ni à la fin
            if carte[i, j] > 0:

                # Voisin Est
                if j+1 < l and carte[i, j+1] != -1 and carte[i, j+1] < carte[i, j]:
                    carte_dir[i, j] = 0

                # Voisin Nord-Est
                elif 0 <= i-1 and j+1 < l and carte[i-1, j+1] != -1 and carte[i-1, j+1] < carte[i, j]:
                    carte_dir[i, j] = 1

                # Voisin Nord
                elif 0 <= i-1 and carte[i-1, j] != -1 and carte[i-1, j] < carte[i, j]:
                    carte_dir[i, j] = 2

                # Voisin Nord-Ouest
                elif 0 <= i-1 and 0 <= j-1 and carte[i-1, j-1] != -1 and carte[i-1, j-1] < carte[i, j]:
                    carte_dir[i, j] = 3

                # Voisin Ouest
                elif 0 <= j-1 and carte[i, j-1] != -1 and carte[i, j-1] < carte[i, j]:
                    carte_dir[i, j] = 4

                # Voisin Sud-Ouest
                elif 0 <= j-1 and i+1 < h and carte[i+1, j-1] != -1 and carte[i+1, j-1] < carte[i, j]:
                    carte_dir[i, j] = 5

                # Voisin Sud
                elif i+1 < h and carte[i+1, j] != -1 and carte[i+1, j] < carte[i, j]:
                    carte_dir[i, j] = 6

                # Voisin Sud-Est
                elif i+1 < h and j+1 < l and carte[i+1, j+1] != -1 and carte[i+1, j+1] < carte[i, j]:
                    carte_dir[i, j] = 7

            # On marque la fin à 8 pour la reconnaitre
            elif carte[i, j] == 0:
                carte_dir[i, j] = 8

    return carte_dir


def debut(carte):
    """
    Cette fonction permet de selectionner le point le plus éloigné de la sortie du labyrinthe

    :param carte: Carte renvoyée par Dijkstra (numpy.ndarray)
    :return: Coordonnées du point de départ     (int,int)
    """

    # Initialisation
    maxi = 0    # Stocke la valeur maximum trouvée
    i_max, j_max = 0, 0     # Stocke les coordonnées de la case de plus grande valeur

    # On parcourt la carte
    for i in range(carte.shape[0]):
        for j in range(carte.shape[1]):

            # Si la valeur de la case actuelle est supérieure au maximum précédent
            if carte[i][j] > maxi:
                # On actualise la valeur max et ses coordonnées
                maxi = carte[i][j]
                i_max, j_max = i, j

    return i_max, j_max


def resolve(carte_dir, debut):
    """
    Fonction qui permet de résoudre un labyrinthe grâce à sa carte directionnelle, en partant du
    point le plus éloigné de la sortie.

    :param carte_dir: La carte directionnelle à résoudre    (numpy.ndarray)
    :param debut: Coordonnées du point de départ            (int, int)
    :return: Le chemin qui constitue la solution            (list)
    """

    # Initialisation
    chemin = [debut]    # Variable de retour
    direction = carte_dir[debut] # Première direction à suivre

    # Tableau qui sera utilisé comme un switch/case en fonction de la direction
    switch = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

    # Tant qu'on est pas arrivé à la fin
    while direction != 8:

        # On ajoute la case suivante au chemin
        i = chemin[-1][0] + switch[direction][0]
        j = chemin[-1][1] + switch[direction][1]
        chemin.append((i, j))

        # Et on regarde la prochaine direction
        direction = carte_dir[i, j]

    return chemin
