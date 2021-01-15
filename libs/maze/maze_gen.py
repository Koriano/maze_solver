"""
Projet - Résolution d'un labyrinthe 2D/3D

Alexandre HAMON
Margaux SCHNELZAUER-HENRY

Bibliothèque servant à générer des labyrinthes
"""
# Built-in modules
import random
# Personnal modules
from libs.maze.maze_utils import *
from libs.maze.dijkstra import *
from libs.maze.maze_solve import *


def cheminAleatoire(carte, i, j, chemin, longueur):
    """
    Fonction permettant de déterminer un chemin aléatoire d'une certaine longueur.
    Utilisé pour la génération d'une carte aléatoire.
    Fonctionne en récursivité (longueur <= 500 par problème de récurisivité depth)

    :param carte: La carte du labyrinthe                                (numpy.ndarray)
    :param i: Première coordonnée du point de départ                    (int)
    :param j: Deuxième coorodnnée du point de départ                    (int)
    :param chemin: Chemin déjà parcouru par l'algorithme                (list)
    :param longueur: Longueur du chemin                                 (int)
    :return: True si le chemin fait la bonne longueur, False sinon      (boolean)
    """

    # Condition d'arrêt
    if longueur == 0:
        return True

    # Initialisation
    check = False
    voisins = listeVoisins(carte, i, j)

    # Pour chaque voisin pas dans le chemin, on ajoute au chemin et on rappelle la fonction
    for v in voisins:
        if v not in chemin:
            chemin.append(v)
            check = cheminAleatoire(carte, v[0], v[1], chemin, longueur-1)

            if check:
                break

    if check:
        return True

    # Si aucun chemin à partir de ce point n'est concluant, on supprime les cases parcourues jusque là
    else:
        chemin.remove(chemin[-1])
        return False


def initMapAleatoire(h, l):
    """
    Fonction qui permet de générer une carte générée avec l'algorithme de chemin aléatoire.

    :param h: Hauteur de la carte                   (int)
    :param l: Largeur de la carte                   (int)
    :return: La carte initialisée avec les murs     (numpy.ndarray)
    """

    # On initialise la carte vide
    carte = np.full((h, l), -2)
    nb_cases = h*l

    # On détermine une case de départ aléatoire
    i_fin, j_fin = random.randint(0, h-1), random.randint(0, l-1)

    # Déterminer un chemin aléatoire valable
    longueur = max(h, l)//2
    chemin = [(i_fin, j_fin)]

    cheminAleatoire(carte, i_fin, j_fin, chemin, longueur)

    # Calcul le nombre de murs sur la map
    pourcentage_mur = 0.6
    nb_murs = int(nb_cases * pourcentage_mur)

    fin = (i_fin, j_fin)

    # Déterminer l'emplacement des murs
    for i in range(nb_murs):
        mur = random.randint(0, h-1), random.randint(0, l-1)

        while mur in chemin:
            mur = random.randint(0, h-1), random.randint(0, l-1)

        carte[mur] = -1

    return carte, fin


def DFS(carte, i, j):
    """
    Fonction qui permet de construire un labyrinthe grâce à l'algorithme DFS

    :param carte: Carte du labyrinthe                     (numpy.ndarray)
    :param i: Première coordonnée de la case de départ  (int)
    :param j: Deuxième coordonnée de la case de départ  (int)
    :return: La carte initialisée                       (numpy.ndarray)
    """
    # Initialisation
    carte[i, j] = -2
    intersections = [(i, j)]    # Liste des intersections pour revenir plus vite en arrière

    # Tant qu'il reste des intersections
    while len(intersections) > 0:

        # On prend la dernière intersection et on regarde ses voisins eligibles
        case = intersections[-1]
        intersections.pop()
        voisins = listeVoisinsEligibles(carte, case[0], case[1])

        while len(voisins) > 0:
            case = random.choice(voisins)
            if len(voisins) >= 2:
                intersections.append(case)
            carte[case] = -2
            voisins = listeVoisinsEligibles(carte, case[0], case[1])

    return carte


def initMapDFS(h, l):
    """
    Fonction qui permet de générer une carte (labyrinthe) avec la méthode du DFS

    :param h: Hauteur de la carte   (int)
    :param l: Largeur de la carte   (int)
    :return: La carte initialisée   (numpy.ndarray)
    """

    # On génère une matrice h*l rempplie de -1
    carte = np.full((h, l), -1)

    # On détermine la fin du labyrinthe aléatoirement
    i_fin, j_fin = random.randint(0, h-1), random.randint(0, l-1)

    # On execute l'algorithme de DFS pour initialiser la carte
    carte = DFS(carte, i_fin, j_fin)

    return carte, (i_fin, j_fin)


def genereMapDij(h, l):
    """
    Fonction qui reprend les fonctions des parties précédentes afin de générer une carte, appliquer dijkstra,
    et trouver un point de départ.

    :param h: Hauteur du labyrinthe                 (int)
    :param l: Largeur du labyrinthe                 (int)
    :return: La carte                               (numpy.ndarray)
             Le point de départ                     (int, int)
             Le point d'arrivée                     (int, int)
             La distance max trouvée pour Dijkstra  (int)
    """

    # Génération de map + Dijkstra
    carte, arrivee = initMapDFS(h, l)
    carte = dijkstra(carte, arrivee)

    # On trouve un début dont la solution possède une longueur de chemin l
    deb = debut(carte)

    # On cherche le maximum de Dijkstra sur la carte
    maxi = 0
    for i in range(h):
        for j in range(l):
            if carte[i, j] > maxi:
                maxi = carte[i, j]

    return carte, deb, arrivee, maxi
