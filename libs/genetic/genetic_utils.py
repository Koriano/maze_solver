"""
Projet - Résolution d'un labyrinthe 2D/3D

Alexandre HAMON
Margaux SCHNELZAUER-HENRY

Bibliothèque de fonctions utilitaires pour l'algorithme génétique
"""
# Built-in modules
import matplotlib.pyplot as plt
import random
# Personnal modules
from libs.maze.maze_utils import *
from libs.display import *


def parcoursIndividu(carte, individu, indice, exploration, depart, arrivee):
    """
    Fonction permettant de faire parcourir un individu dans le labyrinthe afin d'en retourner le chemin résultant.

    :param carte: La carte à parcourir                                  (numpy.ndarray)
    :param individu: L'individu qui va parcourir le labyrinthe          (list)
    :param indice: Le numéro de l'individu                              (int)
    :param exploration: La carte montrant l'exploration du labyrinthe   (numpy.ndarray)
    :param depart: Les coordonnées de départ de l'individu              (int, int)
    :param arrivee: Les coordonnées de la sortie du labyrinthe          (int, int)

    :return: La liste des cases parcourues par l'individu               (list)
    """

    # Dimensions du labyrinthe
    h = carte.shape[0]
    l = carte.shape[1]

    # Position de départ de l'individu
    pos = depart

    # Switch pour les coordonnées de la prochaine direction
    switch = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]

    # Retient les positions du chemin
    chemin = [pos]

    # Retient les intersections rencontrées
    intersections = [pos]

    # Variable qui indique s'il faut boucher une impasse
    bouche = False

    # On parcourt les gènes de l'individu
    for dir in individu:

        # On calcule la nouvelle coordonnée
        i = pos[0] + switch[dir][0]
        j = pos[1] + switch[dir][1]

        # Si la nouvelle coord est dans le labyrinthe
        if 0 <= i < h and 0 <= j < l:

            # Si c'est l'arrivée on arrête le parcours ici
            if (i, j) == arrivee:
                chemin.append((i, j))
                break

            # Si le chemin forme un cycle
            if len(intersections) > 2 and (exploration[i, j] == indice) and not ((i, j) == chemin[-2]):
                ind = chemin.index(intersections[-1])

                # On bouche le chemin avec des murs pour casser le cycle
                while chemin[ind] != intersections[-2]:
                    if ind < chemin.index(intersections[-1]) and chemin[ind] != depart:
                        carte[chemin[ind]] = -1
                        exploration[chemin[ind]] = -1

                    ind -= 1


            # Si la prochaine case n'est ni un mur, ni ne nous fait retourner en arrière
            elif carte[i, j] != -1 and exploration[i, j] != indice:
                pos = (i, j)
                exploration[pos] = indice
                chemin.append(pos)

                voisins = listeVoisins(carte, i, j)

                # Si elle n'a qu'un voisin, c'est une impasse à boucher
                if (i, j) != depart and len(voisins) == 1:
                    bouche = True
                    break
                # On sauvegarde les intersections
                elif len(voisins) > 2:
                    intersections.append((i, j))

    # Si on doit boucher une impasse, on bouche jusqu'à la dernière intersection (exclue)
    if bouche:
        ind = chemin.index(intersections[-1])
        for case in chemin[ind:]:
            carte[case] = -1
            exploration[case] = -1

    return chemin


def fitness(chemin_individu, arrivee, l):
    """
    Fonction qui permet de calculer le score de fitness en fonction de son parcours.

    :param chemin_individu: Chemin parcouru par un individu (list)
    :param arrivee: La sortie du labyrinthe                 (int, int)
    :param l: La longueur maximum des chemins               (int)

    :return: Le score de fitness relatid à ce chemin        (float)
    """

    # On récupère la position de fin du chemin
    fin = chemin_individu[-1]

    # On calcule la distance à vol d'oiseau de la fin du chemin à l'arrivee
    distance = (arrivee[0]-fin[0])**2 + (arrivee[1]-fin[1])**2

    # On calcule les pénalités (murs touchés ou sortie du labyrinthe)
    penalite = (l - len(chemin_individu))**2

    # Le score de fitness sera la distance + les pénalités
    return distance + penalite


def creationEnfant(population):
    """
    Fonction qui permet de créer un enfant à partir de deux parents aléatoires

    :param population: Liste des individus encore vivants   (list)

    :return: L'enfant créé                                  (list)
    """

    # On sélectionne deux parents aléatoires
    papa = random.choice(population)
    maman = random.choice(population)

    # On vérifie que les deux parents sont différents, sinon on retire aléatoirement
    while maman == papa:
        maman = random.choice(population)

    # On détermine la position de coupe
    cut = random.randint(2, len(papa))

    # On crée l'enfant
    enfant = papa[:cut] + maman[cut:]

    return enfant


def affiche_fitness(liste_fitness):
    """
    Fonction qui affiche la courbe de fitness en fonction de la liste en paramètres

    :param liste_fitness: La liste des scores de fitness    (list)

    :return: Affichage de la courbe fitness                 (None)
    """

    # On construit l'axe x du grahique, l'axe y étant les valeurs de fitness
    x = [i for i in range(len(liste_fitness))]

    # On affiche la courbe
    plt.plot(x, liste_fitness)
    plt.savefig("fitness.png")
    plt.show()