"""
Projet - Résolution d'un labyrinthe 2D/3D

Alexandre HAMON
Margaux SCHNELZAUER-HENRY

Bibliothèque des fonctions principales pour la génétique
"""
# Personnal modules
from libs.genetic.genetic_utils import *
import random

def genese(n, l):
    """
    Fonction qui permet de générer une population aléatoire

    :param n: Le nombre d'individus à générer                       (int)
    :param l: La longueur maximum qu'un chemin peut parcourir       (int)
    :return: La liste des individus de la population                (list)
    """

    population = []

    # On génère n individus
    for i in range(n):
        # Chaque individu étant une suite de l nombres (de 0 à 7)
        new_ind = [random.randint(0, 7) for i in range(l)]
        population.append(new_ind)

    return population


def selection(liste_fitness, population, taux_selection):
    """
    Fonction qui permet de sélectionner les meilleurs individus d'une population

    :param liste_fitness: La liste des scores de fitness                (list)
    :param population: La population d'individus                        (list)
    :param taux_selection: Le pourcentage d'individus à sélectionner    (float)

    :return: La nouvelle population, contenant les meilleurs individus  (list)
    """

    # On calcule le nombre d'individus que nous allons supprimer
    nb_mort = int(len(liste_fitness) * (1 - taux_selection))

    # On supprime les individus possédant la fitness maximum en concordance avec le nombre de morts
    for i in range(nb_mort):
        index = liste_fitness.index(max(liste_fitness))
        del liste_fitness[index]
        del population[index]

    return population


def reproduction(population, n):
    """
    Fonction qui permet de reproduire les individus entre eux pour créer des enfants.

    :param population: La liste des individus sélectionnés      (list)
    :param n: Le nombre d'individus maximum de la population    (int)

    :return: La liste des enfants créés                         (list)
    """

    # On initialise la liste des enfants
    liste_enfant = []

    # Tant que les sélectionnés + les enfants créés ne dépassent pas la taille de population max
    while len(liste_enfant) + len(population) < n:
        # On crée un enfant
        enfant = creationEnfant(population)

        # On l'ajoute à la population s'il n'a pas de jumeau
        if enfant not in population:
            liste_enfant.append(enfant)

    return liste_enfant


def mutation(population, taux_mutation, choix):
    """
    Fonction qui permet de muter des individus de manière aléatoire.

    :param population: La population à muter                                                            (list)
    :param taux_mutation: Le pourcentage d'individus à muter                                            (float)
    :param choix: Si Vrai, on peut muter n'importe quel gène, si Faux, on mute que les derniers gènes   (boolean)

    :return: La population mutée                                                                        (list)
    """

    # On initialise la liste des mutants
    liste_mutants = []

    # Calcule du nombre d'individus à muter
    nb_mutant = len(population) * taux_mutation

    # Tant qu'il reste des individus à muter
    while len(liste_mutants) < nb_mutant:

        # S'il reste des individus non mutés (taux_mutation < 1)
        if len(population) > 0:
            mutant = random.choice(population)
            population.remove(mutant)

        # Si tous les individus ont déjà été mutés (taux_mutation > 1)
        else:
            mutant = random.choice(liste_mutants)

        # On choisit un gène aléatoire qu'on modifie aléatoirement
        if choix:
            gene_idx = random.randint(2, len(mutant)-1)
        else:
            gene_idx = random.randint(len(mutant)//2, len(mutant) - 1)

        # On choisit une valeur aléatoire pour le gène
        gene_val = random.randint(0, 7)

        # Tant que c'est la même valeur, on retire aléatoirement la valeur
        while mutant[gene_idx] == gene_val:
            gene_val = random.randint(0, 7)

        # On change la valeur du gène
        mutant[gene_idx] = gene_val

        # On ajoute l'individu à la liste des mutés
        liste_mutants.append(mutant)

    return population + liste_mutants


def generation(population, liste_fitness, n, taux_selection, taux_mutation, choix):
    """
    Fonction qui effectue toutes les étapes d'une génération :  - Sélection
                                                                - Reproduction
                                                                - Mutation

    :param population: La liste des individus                                   (list)
    :param liste_fitness: La liste des scores fitness des individus             (list)
    :param n: Le nombre maximum d'individus dans la population                  (int)
    :param taux_selection: Le taux pour la sélection                            (float)
    :param taux_mutation: Le taux pour la mutation                              (float)
    :param choix: La sélection du gène pour la mutation                         (boolean)

    :return: La nouvelle population après sélection, reproduction et mutation   (list)
    """

    # On sélectionne les meilleurs individus
    vivant = selection(liste_fitness, population, taux_selection)

    # On reproduit les meilleurs individus
    enfant = reproduction(vivant, n)

    # On mute les enfants ainsi créés
    enfant_mutant = mutation(enfant, taux_mutation, choix)

    return vivant + enfant_mutant