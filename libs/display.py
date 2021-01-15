"""
Projet - Résolution d'un labyrinthe 2D/3D

Alexandre HAMON
Margaux SCHNELZAUER-HENRY

Bibliothèque servant à afficher des labyrinthes
"""
# Built-in modules
import numpy as np
import matplotlib.pyplot as plt
from pylab import cm
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D



def colorCarte(carte, solution, nom):
    """
    Cette fonction permet d'afficher le labyrinthe avec des couleurs correspondant à la distance par
    rapport au point d'arrivée.
    Le chemin de solution y est aussi coloré

    :param mat: Carte renvoyée par Dijkstra                     (numpy.ndarray)
    :param solution: Chemin de la solution                      (list)
    :param nom: Le nom du fichier pour enregistrer la solution  (str)
    :return: None                                               (None)
    """

    val = max(carte.shape[0], carte.shape[1])
    for case in solution:
        carte[case] = val

    fig, ax = plt.subplots()
    ax.matshow(carte)
    plt.savefig("./images/" + nom)
    plt.show()


def colorCartePIL(matrice, depart, arrivee):
    """
    Fonction qui permet d'afficher une carte grâce à PIL.

    :param matrice: Labyrinthe à afficher                   (numpy.ndarray)
    :param depart: Coordonnées du point de départ           (int, int)
    :param arrivee: Coordonnées de la sortie du labyrinthe  (int, int)
    :return: L'affichage du labyrinthe                      (None)
    """

    # On commence par créer une matrice de la même taille
    image = np.zeros((matrice.shape[0], matrice.shape[1],3), dtype='uint8')
    i_debut, j_debut = depart
    i_fin, j_fin = arrivee
    # On regarde la plus grande valeur dans la matrice

    maxi = 0
    for i in range(matrice.shape[0]):
        for j in range(matrice.shape[1]):

            if matrice[i][j] > maxi:
                maxi = matrice[i][j]

    pas = (255/(maxi-1))


    # On remplie le reste des valeurs

    for i in range(matrice.shape[0]):
        for j in range(matrice.shape[1]):

            if matrice[i][j] == -1:
                image[i][j] = [0, 0, 0]

            else:
                val = matrice[i][j]
                image[i][j] = [100, 50, (val*pas)]


    # On modifie le point de départ et d'arrivée
    image[i_debut][j_debut] = [255, 0, 0]
    image[i_fin][j_fin] = [0, 255, 0]

    # enregistrement et affichage de l'image
    img = Image.fromarray(image)
    img.save("./images/Labyrinthe.png")

    plt.imshow(image)

    return plt.show()


def affiche3D(matrice):
    """
    Fonction qui permet d'afficher en 3D un labyrinthe

    :param matrice: le labyrinthe à afficher    (numpy.ndarray)
    :return: L'affichage 3D du labyrinthe       (None)
    """

    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')

    taille_x = matrice.shape[0]
    taille_y = matrice.shape[1]

    # Initialisation des 3 axes
    liste_pos_x = []
    liste_pos_y = []
    liste_pos_z = np.zeros(taille_x*taille_y)
    dx = np.ones(taille_x*taille_y)
    dy = np.ones(taille_x*taille_y)
    dz = []

    pos_y = [x for x in range(taille_y)]

    # Construction de l'axe x
    i = 0
    while i < taille_x:
        for k in range(taille_x):
            liste_pos_x.append(i)

        i += 1

    # Construction de l'axe y
    for i in range(taille_y):
        liste_pos_y += pos_y

    # Construction de l'axe z
    for i in range(taille_x):
        for j in range(taille_y):
            dz.append(matrice[i][j])


    nx = taille_x*taille_y
    colors = cm.tab20(np.linspace(0, 1, nx))

    # On affiche le labyrinthe 3D
    ax1.bar3d(liste_pos_x, liste_pos_y, liste_pos_z, dx, dy, dz, color='g')
    plt.show()