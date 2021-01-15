"""
Projet - Résolution d'un labyrinthe 2D/3D

Alexandre HAMON
Margaux SCHNELZAUER-HENRY

Bibliothèque de fonctions permettant l'affinement de l'algorithme génétique
"""
# Built-in modules
from decimal import Decimal


def detectionStagnation(liste_fitness):
    """
    Fonction qui détecte lorsque la fonction fitness stagne

    :param liste_fitness: La liste des valeurs de fitness   (list)

    :return: Vrai si la fitness stagne, Faux sinon          (boolean)
    """

    # On sélectionne les 10 dernières valeurs de la liste fitness
    liste_select = liste_fitness[-10:]

    # Pourcentage de valeur pour lequel la fitness est considérée comme un plateau
    pourcentage_declenche = 0.4

    # Variable de retour
    declenchement = False

    # Les valeurs qui ont dépassé le seuil (référence +/- pourcentage_erreur)
    liste_depass =[]

    # Référence pour le seuil de valeur
    reference = liste_select[-1]
    liste_select.remove(liste_select[-1])

    # Seuil pour lequel une valeur est considérée comme proche ou non
    pourcentage_erreur = 0.60 * reference

    # On regarde les valeurs qui sont proches de notre référence
    for elem in liste_select:
        if reference - pourcentage_erreur <= elem <= reference + pourcentage_erreur:
            liste_depass.append(elem)

        # On regarde si il y a plus de 60% des valeurs proche de la référence
        if len(liste_depass) >= pourcentage_declenche*len(liste_select):
            declenchement=True
            break

    return declenchement


def correctionErreur(nb_plateau, taux_selection, taux_mutation, choix, l):
    """
    Fonction qui permet de modifier les paramètres de génétique.
    Utilisé dans le cas où la fonction fitness stagne.

    :param nb_plateau: Le nombre de plateaux rencontrés (int)
    :param taux_selection: Le taux pour la sélection    (float)
    :param taux_mutation: Le taux pour la mutation      (float)
    :param choix: Le choix pour la mutation des gènes   (boolean)
    :param l: La longueur max des chemins               (int)

    :return: Les 4 paramètres: - taux_selection (float)
                               - taux_mutation  (float)
                               - choix          (boolean)
                               - l              (int)
    """

    if nb_plateau % 4 == 0:
        print("modif 1")
        taux_selection -= Decimal("0.1")

        if taux_selection == 0:
            taux_selection = Decimal("0.50")

    if nb_plateau % 4 == 1:
        print("modif 2")
        taux_mutation += Decimal("0.15")

    if nb_plateau % 4 == 2:
        print("modif 3")
        choix = False

    if nb_plateau % 4 == 3:
        print("modif 4")
        l += (1/4) * l

    return taux_selection, taux_mutation, choix, l