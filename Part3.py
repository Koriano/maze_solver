"""
Algorithmique et programmation impérative - Projet

Sous-partie 3

SCHNELZAUER-HENRY Margaux
HAMON Alexandre
"""
# Built-in modules
# Personnal Modules
#from libs.interface import *
from libs.genetic.genetic_solve import *


"""
Projet - Résolution d'un labyrinthe 2D/3D

Alexandre HAMON
Margaux SCHNELZAUER-HENRY

Bibliothèque permettant l'affichage de labyrinthes
"""

from tkinter import *
from PIL import Image, ImageTk


def Suivant():
    """
    Cette fonction permet d'afficher les différentes fenêtres lors de la résolution du labyrinthe

    :return: elle ne renvoie rien
    """

    # fenêtre de résultat
    resultat = Tk()
    resultat.configure(bg="White")

    # Le labyrinthe a été solutionné
    if trouver:

        # Affichage de la fonction fitness
        fitness = Label(resultat, text="Voici notre fonction fitness", bg="white")
        fitness.grid(row=0, column=1, sticky="nsew", padx=15, pady=5)
        im2 = Image.open("./images/fitness.png")

        photo2 = ImageTk.PhotoImage(im2, master=resultat)
        fond = Label(resultat, image=photo2, bg="white")
        fond.grid(row=1, column=1, sticky="nsew", padx=15, pady=5)


        # Affichage du chemin trouvé
        sol = Label(resultat, text="Voici notre solution", bg="white")
        sol.grid(row=0, column=2, sticky="nsew", padx=15, pady=5)

        im3 = Image.open("./images/sol.png")

        photo3 = ImageTk.PhotoImage(im3, master=resultat)
        fond = Label(resultat, image=photo3, bg="white")
        fond.grid(row=1, column=2, sticky="nsew", padx=15, pady=5)


    # Le labyrinthe n'a pas été solutionné
    else :
        # Message informant l'utilisateur
        affiche = Label(resultat, text="La labyrinthe n'a pas pu être solutionné", bg="white")
        affiche.grid(row=0, column=0, sticky="nsew", padx=15, pady=5)


    resultat.mainloop()



#----------------------------------------------------------------------------------------------------#

def valider():
    """
    Cette fonciton permet la validation des données saisie et l'ouverture de la fenêtre d'attente
    des résultats

    :return: cette fonction ne renvoie rien
    """

    #Variable globale
    global trouver

    # Récupération des données saisies
    taille, nbGenMax, opti = taille_x.get(), taille_gen.get(), v.get()

    # Fenetre d'attente :
    main = Tk()
    main.configure(bg="White")

    enCours = Label(main, text="La résolution est en cours", bg="white")
    enCours.grid(row=0, column=0, sticky="nsew", padx=15, pady=5)

    main.title("Insérer une image")
    im = Image.open("./images/gif-chargement-9.gif")

    photo = ImageTk.PhotoImage(im, master=main)
    fond = Label(main, image=photo, bg="white")
    fond.grid(row=1, column=0, sticky="nsew", padx=15, pady=5)


    # Sans correction
    if opti == 0:
        trouver = resolutionSansDetection(taille, nbGenMax)

    # Avec correction
    else:
        trouver = resolutionAvecDetection(taille, nbGenMax)


    # Bouton Valider
    bouton_Suivant= Button(main, text="Suivant", command=Suivant)
    bouton_Suivant.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

    main.mainloop()

#------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    trouver = False

    # Fenetre initiale
    fenetre = Tk()

    bjrs = Label(fenetre, text="Bienvenue, veuillez entrer les données suivantes : ")
    bjrs.grid(row=0, column=0, sticky="nsew", padx=15, pady=5)

    # Taille
    pos_x = Label(fenetre, text="Taille du labyrinthe: ")
    pos_x.grid(row=1, column=0, sticky="nsew", padx=15, pady=5)
    taille_x = IntVar()
    champ_x = Entry(fenetre, textvariable=taille_x)
    champ_x.focus_set()
    champ_x.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

    # Nombre de génération maximum
    nbGenMax = Label(fenetre, text="Nombre de génération maximum : ")
    nbGenMax.grid(row=2, column=0, sticky="nsew", padx=15, pady=5)
    conseil1 = Label(fenetre, text="Sans correction : 500 / Avec correction : 5000")
    conseil1.grid(row=3, column=0, sticky="nsew", padx=15, pady=0)

    taille_gen = IntVar()
    champ_gen = Entry(fenetre, textvariable=taille_gen)
    champ_gen.focus_set()
    champ_gen.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

    # Optimisation
    opti = Label(fenetre, text="Pour la version optimisée, cocher cette case")
    opti.grid(row=4, column=0, sticky="nsew", padx=15, pady=5)
    v = IntVar()
    button = Checkbutton(fenetre, text="", variable=v)
    button.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)

    # Bouton Valider
    bouton_valider = Button(fenetre, text="Valider", command=valider)
    bouton_valider.grid(row=5, column=2, sticky="nsew", padx=5, pady=5)

    fenetre.mainloop()

    ## Nous commençons par tester sans correction pour une matrice 20 x20
    ## Nous limitons à 500 generations (peu souvent résolu)
    #print("Résolution d'un labyrinthe 20 x 20 sans optimisation : \n")
    #resolutionSansDetection(20, 500)

    ## Nous testons maintenant sur une matrice 40 x 40
    #print("\n\n\n\nRésolution d'un labyrinthe 40 x 40 sans optimisation : \n")
    #resolutionSansDetection(40, 500)


    ## Nous testons maintenant avec correction sur une matrice 20 x 20
    #print("\n\n\n\nRésolution d'un labyrinthe 20 x 20 avec optimisation : \n")
    #resolutionAvecDetection(20, 5000)

    ## Nous testons maintenant sur une matrice 50 x 50
    #print("\n\n\n\nRésolution d'un labyrinthe 50 x 50 avec optimisation : \n")
    #resolutionAvecDetection(50, 5000)


    ## Nous testons maintenant sur une matrice 50 x 50
    #print("\n\n\n\nRésolution d'un labyrinthe 100 x 100 avec optimisation : \n")
    #resolutionAvecDetection(100, 5000)


