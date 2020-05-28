import numpy as np
from random import *
import pandas as pd
import pygame
from pygame.locals import *


class Labyrinth:

    """Géneration aléatoire de ligne pour construire chaque ligne d'un tableau'."""
    ##lign = [0]

    ##for i in range(14):
        ##i = lign.append(randint(0,1))

    """0 définit un sol et 1 définit un mur. Modification accessibilité chemin à la main, en remplaçant certains 
    murs par des sols. Départ supposé en bas à gauche et arrivée en haut à droite"""

    tab = [
        [0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    ]

    def show_lab(self):
        # chargement des images
        floor = pygame.image.load("floor.png")
        wall = pygame.image.load("wall.png")

        # # On parcourt la liste du niveau
        num_lign = 0
        for lign in self.tab:
            # On parcourt les listes de lignes
            num_case = 0
            for sprite in lign:
                # On calcule la position réelle en pixels
                x = num_case * 25
                y = num_lign * 25
                if sprite == 1:  # 1 = wall
                    fenetre.blit(wall, (x, y))
                elif sprite == 0:  # 0 = floor
                    fenetre.blit(floor, (x, y))
                num_case += 1
            num_lign += 1

class MacGyver:

    def show_mac (self):
        """Methode permettant d'initialiser le personnage"""
        # Sprites du personnage
        self = pygame.image.load("MacGyver.png")
        # Position du personnage
        fenetre.blit(self, (0, 350))

class Guardian:

    def show_guard (self):
        """Methode permettant d'initialiser le gardien"""
        # Sprites du personnage
        self = pygame.image.load("Guardian.png")
        # Position du personnage
        fenetre.blit(self, (350, 0))

class Items:
    def location (self, list):
        # # On parcourt la liste du labyrinthe
        num_lign = 0
        for lign in list:
            # On parcourt les listes de lignes
            num_case = 0
            for sprite in lign:
                if sprite == 1:  # 1 = wall
                    pass
                elif sprite == 0:  # 0 = floor
                    p = randint(0,2000) # p = possibilité d'avoir un objet sur la case
                    if p == 1:
                        # On calcule la position réelle en pixels des objets
                        x = num_case * 25
                        y = num_lign * 25
                        if not (x == 0 and y == 350) and (x == 350 and y == 0):
                            return [x, y]
                num_case += 1
            num_lign += 1
        return None

    def show_item (self, list):
        """Méthode permettant d'initialiser les objets"""
        # Coordonnées des objets sur tab
        for i in range(0,3):
            tab_loc = self.location(list)
            while tab_loc == None:
                tab_loc = self.location(list)
            x = tab_loc[0]
            y = tab_loc[1]
            # Sprites des objets en fonction de l'itération
            if i == 0:
                fenetre.blit(pygame.image.load("needle.png"), (x, y))
            elif i == 1:
                fenetre.blit(pygame.image.load("syringe.png"), (x, y))
            else:
                fenetre.blit(pygame.image.load("tube.png"), (x, y))
##random.sample




if __name__ == "__main__":

    pygame.init()

    fenetre = pygame.display.set_mode((375, 375))

    lab = Labyrinth()
    lab.show_lab()
    mac = MacGyver()
    mac.show_mac()
    guard = Guardian()
    guard.show_guard()
    item = Items()
    item.show_item(lab.tab)


    # Rafraîchissement de l'écran
    pygame.display.flip()

    continuer = 1
    # Boucle infinie
    while continuer:
        for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
            if event.type == QUIT:  # Si un de ces événements est de type QUIT
                continuer = 0



