"""
Projet - Résolution d'un labyrinthe 2D/3D

Alexandre HAMON
Margaux SCHNELZAUER-HENRY

Bibliothèque permettant d'utiliser dijkstra
"""
import numpy as np


def dijkstra(carte, fin):
    """
    Fonction qui utilise l'algorithme de Dijkstra afin de remplir une carte de labyrinthe avec des valeurs.
    Ces valeurs correspondent à la distance de la case par rapport à la sortie.
    La fonction utilise le mécanisme de propagation.

    :param carte: La carte du labyrinthe à remplir          (numpy.ndarray)
    :param fin: Les coordonnées de la sortie du labyrinthe  (int, int)
    :return: La carte remplie grâce à Dijkstra              (numpy.ndarray)
    """

    # Initialisation
    h = carte.shape[0]  # Hauteur de la carte
    l = carte.shape[1]  # Largeur de la carte
    carte_dij = np.copy(carte)
    voisins = []        # Liste des voisins à marquer prochainement
    marques = [fin]     # Liste des cases déjà marquées
    carte_dij[fin] = 0      # On marque le départ à la valeur 0
    compteur = 1        # Les prochaines valeurs des cases seront 1


    # Tant que marques n'est pas vide
    while len(marques) > 0:

        # Pour chaque marque, on va ajouter ses voisins à la liste des voisins
        for i, j in marques:

            # Voisin Sud
            if i+1 < h and carte_dij[i+1][j] == -2:
                voisins.append((i+1, j))
                carte_dij[i+1][j] = compteur

            # Voisin Est
            if j+1 < l and carte_dij[i][j+1] == -2:
                voisins.append((i, j+1))
                carte_dij[i][j+1] = compteur

            # Voisin Nord
            if 0 <= i-1 and carte_dij[i-1][j] == -2:
                voisins.append((i-1, j))
                carte_dij[i-1][j] = compteur

            # Voisin Ouest
            if 0 <= j-1 and carte_dij[i][j-1] == -2:
                voisins.append((i, j-1))
                carte_dij[i][j-1] = compteur

            # Voisin Sud-Est
            if i+1 < h and j+1 < l and carte_dij[i+1][j+1] == -2:
                voisins.append((i+1, j+1))
                carte_dij[i+1][j+1] = compteur

            # Voisin Nord-Ouest
            if 0 <= i-1 and 0 <= j-1 and carte_dij[i-1][j-1] == -2:
                voisins.append((i-1, j-1))
                carte_dij[i-1][j-1] = compteur

            # Voisin Sud-Ouest
            if i+1 < h and 0 <= j-1 and carte_dij[i+1][j-1] == -2:
                voisins.append((i+1, j-1))
                carte_dij[i+1][j-1] = compteur

            # Voisin Nord-Est
            if j+1 < l and 0 <= i-1 and carte_dij[i-1][j+1] == -2:
                voisins.append((i-1, j+1))
                carte_dij[i-1][j+1] = compteur

        marques, voisins = voisins, []
        compteur += 1

    return carte_dij