"""
Projet - Résolution d'un labyrinthe 2D/3D

Alexandre HAMON
Margaux SCHNELZAUER
"""


import time
import matplotlib.pyplot as plt
# Personnal modules
from libs.maze.maze_gen import *
from libs.maze.maze_solve import *
from libs.maze.dijkstra import *
from libs.display import *



def exectutionPart1(h,l):
    """
    Cette fonction va nous permettre d'executer la résolution par la méthode 1

    :param h: hauteur du labyrinthe
    :param l: largeur du labyrinthe

    :return: Cette fonction ne renvoie rien
    """

    # On créer notre carte
    carte, fin = initMapAleatoire(h, l)

    # On lui applique Dijkstra
    carte = dijkstra(carte, fin)

    # On génère notre carte directionnelle
    carte_dir = carteDirectionnelle(carte)

    # On résoud notre labyrinthe
    solution = resolve(carte_dir, debut(carte))

    # On affiche le résultat pour voir la qualité de la matrice
    colorCarte(carte, solution, "exec_part1")

#----------------------------------------------------------------------------------#
def exectutionPart2(h,l):
    """
    Cette fonction va nous permettre d'executer la résolution par la méthode 2

    :param h: hauteur du labyrinthe
    :param l: largeur du labyrinthe

    :return: Cette fonction ne renvoie rien
    """

    # On créer notre carte
    carte, fin = initMapDFS(h, l)

    # On lui applique Dijkstra
    carte = dijkstra(carte, fin)

    # On génère notre carte directionnelle
    carte_dir = carteDirectionnelle(carte)

    # On résoud notre labyrinthe
    solution = resolve(carte_dir, debut(carte))

    # On affiche le résultat pour voir la qualité de la matrice
    colorCarte(carte, solution, "exec_part2")

#----------------------------------------------------------------------------------#
def temps_execution(fonction, taille):
    """
    Cette fonction va nous permettre de renvoyer le temps d'execution d'une fonction prenant en
    paramètre l et h (ici on normalise une matrice carrée ou l=h=taille)

    :param fonction: fonction a tester
    :param l: largeur de la carte
    :param h: hauteur de la carte

    :return: temps : temps d'execution de la fonction
    """

    temps0 = time.time()
    fonction(taille, taille)
    temps = time.time() - temps0

    return temps

#----------------------------------------------------------------------------------#
if __name__ == "__main__":

    # On test les fonctions pour différentes valeurs
    # Pour la partie 1
    temps1_50 = temps_execution(exectutionPart1, 50)
    temps1_100 = temps_execution(exectutionPart1, 100)
    temps1_500 = temps_execution(exectutionPart1, 500)
    temps1_1000 = temps_execution(exectutionPart1, 1000)
    # temps1_5000 = temps_execution(exectutionPart1, 5000)
    # temps1_10000 = temps_execution(exectutionPart1, 10000)


    # Pour la partie 2
    temps2_50 = temps_execution(exectutionPart2, 50)
    temps2_100 = temps_execution(exectutionPart2, 100)
    temps2_500 = temps_execution(exectutionPart2, 500)
    temps2_1000 = temps_execution(exectutionPart2, 1000)
    # temps2_5000 = temps_execution(exectutionPart2, 5000)
    # temps2_10000 = temps_execution(exectutionPart2, 10000)

    barWidth = 0.4
    y1 = [temps1_50, temps1_100, temps1_500, temps1_1000]
    y2 = [temps2_50, temps2_100, temps2_500, temps2_1000]

    r1 = range(len(y1))
    r2 = [x + barWidth for x in r1]



    plt.bar(r1, y1, width=barWidth, color=['yellow' for i in y1], edgecolor=['blue' for i in y1], linewidth=2)
    plt.bar(r2, y2, width=barWidth, color=['pink' for i in y1], edgecolor=['green' for i in y1], linewidth=4)
    plt.title("Comparaison des parties 1 et 2")
    plt.xticks([r + barWidth / 2 for r in range(len(y1))], ['50', '100', '500 ', '1 000', '5 000', '10 000'])

    plt.savefig("./images/Comparaison")
    plt.show()





