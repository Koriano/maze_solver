"""
Projet - Résolution d'un labyrinthe 2D/3D

Alexandre HAMON
Margaux SCHNELZAUER-HENRY

Sous-partie 2
"""
# Built-in modules
import time
# Personnal modules
from libs.maze.maze_gen import *
from libs.maze.maze_solve import *
from libs.maze.dijkstra import *
from libs.display import *


if __name__ == "__main__":
    DEBUG = False

    # Affichage et input utilisateur
    print("Bienvenue dans le Maze Runner version DFS !")
    h = int(input("Veuillez sélectionner la hauteur du labyrinthe : "))
    l = int(input("Veuillez sélectionner la largeur du labyrinthe : "))

    # On génère le labyrinthe
    print("Génération du labyrinthe en cours...")
    t1 = time.time()
    carte, fin = initMapDFS(h, l)
    if DEBUG: print("Temps gen: " + str(time.time() - t1))

    # On applique Dijkstra
    if DEBUG: t2 = time.time()
    carte_dij = dijkstra(carte, fin)
    if DEBUG: print("Temps dij: " + str(time.time() - t2))
    print("La carte a été générée en " + str(time.time() - t1) + " secondes")

    # On génère la carte directionnelle
    print("Résolution du labyrinthe...")
    t3 = time.time()
    carte_dir = carteDirectionnelle(carte_dij)
    if DEBUG: print("Temps map_dir:" + str(time.time() - t3))

    # On résoud le labyrinthe
    if DEBUG: t4 = time.time()
    deb = debut(carte_dij)
    solution = resolve(carte_dir, deb)
    if DEBUG: print("Temps résolution:" + str(time.time() - t4))
    print("La solution a été trouvée en " + str(time.time() - t3) + " secondes")

    # On affiche le labyrinthe et la solution
    colorCarte(carte_dij, [], 'lab')
    colorCarte(carte, solution, "Partie2")
    if h < 50 and l < 50:
        affiche3D(carte_dij)
        colorCartePIL(carte, deb, fin)

    print("La génération et la résolution ont donc pris ensemble " + str(time.time() - t1) + " secondes")