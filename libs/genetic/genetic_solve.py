"""
Projet - Résolution d'un labyrinthe 2D/3D

Alexandre HAMON
Margaux SCHNELZAUER-HENRY

Bibliothèque de fonctions permettant de résoudre des labyrinthes avec des algorithmes génétiques
"""
# Built-in imports
import time
# Personnal imports
from libs.maze.maze_gen import *
from libs.genetic.genetic_steps import *
from libs.display import *
from libs.genetic.genetic_filtering import *


def resolutionSansDetection(taille, nb_max_gen):
    """
    Cette fonction permet de resoudre le problème du labyrinthe sans la partie optimisation


    :param taille: taille de labyrinthe souhaitée
    :param nb_max_gen: nombre maximum de générations souhaitées

    :return: Cette fonciton affiche différents éléments tel que la solution trouvées pour la labyrinthe,
            la fonction fitness, la labyrinthe initial et toutes les 100 générations elle affiche l'état
            de parrcour du labyrinthe
    """

    # Variables
    n = 100
    found = False
    nb_gen = 0


    # Récupération des données initiales
    res = genereMapDij(taille, taille)
    l = res[3]
    depart = res[1]
    arrivee = res[2]
    labyrinthe = res[0]
    exploration = np.full((taille, taille), -1)
    exploration[arrivee] = -10

    # Création de la population de départ
    population = genese(n, taille//10*l)

    # liste contenant les valeurs de fitness
    fitness_li =[]

    tps0=time.time()
    indice = 0

    # Affichage du labyrinthe initial
    colorCarte(labyrinthe, [], 'lab')

    # Variable globale :
    choix = True
    taux_mutation = Decimal("0.30")
    taux_selection = Decimal("0.50")

    # On résoud tant que nous n'avons pas trouvé le résultat
    while not found :

        print("Generation ", nb_gen, end = "     ")
        tps1 =time.time()
        nb_gen +=1
        liste_fitness = []

        for individu in population:

            # On deploie notre population  :
            chemin_individu = parcoursIndividu(labyrinthe, individu, indice, exploration, depart, arrivee)
            indice += 1
            # On regarde si on a trouvé le bon chemin ou pas :
            end = chemin_individu[-1]

            # On calcule le fitness
            fit = fitness(chemin_individu, arrivee, l)
            liste_fitness.append(fit)

            if end == arrivee:
                found = True
                break

        # On ajoute le plus petit de notre éléments à la liste fitness afin de le rajotuer à notre courbe
        fitness_li.append(min(liste_fitness))

        # On créer notre nouvelle population
        population = generation(population, liste_fitness, n, taux_selection, taux_mutation, choix)
        print("Temps d'execution : ", time.time() - tps1)

        # On affiche l'état de parcoure du labyrinte toutes les 100 générations
        if nb_gen%100 == 0:
            colorCarte(exploration, [], 'progress')

        # On arrête la recherche si on arrive au nombre de génération maximum
        if nb_gen == nb_max_gen:
            print("La résolution a échouée")
            break

    #On affiche la fonction fitness
    affiche_fitness(fitness_li)

    # On affiche la solution
    colorCarte(labyrinthe, chemin_individu, 'sol')

    print("Temps total d'execution : ", time.time()-tps0)

    return found

#-------------------------------------------------------------------------------------------------#

def resolutionAvecDetection(taille, nb_max_gen):

    # Variables
    n = 100
    found = False
    nb_gen = 0

    # Récupération des données initiale ;
    res = genereMapDij(taille, taille)
    l = res[3]
    depart = res[1]
    arrivee = res[2]
    labyrinthe = res[0]
    exploration = np.full((taille, taille), -1)
    exploration[arrivee] = -10

    # Création de la population de départ
    population = genese(n, taille // 10 * l)

    fitness_li = []

    tps0 = time.time()

    # Affichage du labyrinthe de départ
    colorCarte(labyrinthe, [], "lab")

    # compteur permettant de savoir le nombre de plateau
    compt_stagnation = 0

    indice = 0

    # Variable globale :
    choix = True
    taux_mutation = Decimal("0.30")
    taux_selection = Decimal("0.50")

    while not found:
        print("Generation ", nb_gen, end="     ")
        tps1 = time.time()
        nb_gen += 1
        liste_fitness = []

        for individu in population:
            # On deploie notre population  :
            chemin_individu = parcoursIndividu(labyrinthe, individu, indice, exploration, depart, arrivee)
            indice += 1
            # On regarde si on a trouvé le bon chemin ou pas :
            end = chemin_individu[-1]

            # On calcule le fitness
            fit = fitness(chemin_individu, arrivee, l)
            liste_fitness.append(fit)

            # si l'arrivée est trouvée on s'arrête
            if end == arrivee:
                found = True
                break

        # On ajoute la plus petite valeur à notre liste fitness afin de l'affiche sur la courbe
        fitness_li.append(min(liste_fitness))

        # Détection des plateaux
        if nb_gen > 10 and detectionStagnation(fitness_li):
            if compt_stagnation == 16:
                # Renouvellement de la population
                l = res[3]
                population = genese(n, (taille // 10) * l)

            if compt_stagnation == 0 or nb_gen % 5 == 0:
                print("plateau")
                # Application de la correction d'erreur
                taux_selection, taux_mutation, choix, l = correctionErreur(compt_stagnation, taux_selection,
                                                                           taux_mutation, choix, l)
                compt_stagnation += 1

        # On créer notre nouvelle population
        population = generation(population, liste_fitness, n, taux_selection, taux_mutation, choix)
        print("Temps d'execution : ", time.time() - tps1)

        if nb_gen % 100 == 0:
            colorCarte(exploration, [],'')

        if nb_gen == nb_max_gen:
            break

    # Afffichage de notre fonction fitness
    affiche_fitness(fitness_li)
    colorCarte(labyrinthe, chemin_individu, "sol")
    print("Nombre de plateaux : ", compt_stagnation)
    print("Temps total d'execution : ", time.time() - tps0)

    return found