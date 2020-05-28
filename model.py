import os
import pygame
import random

class MacGyver:
    inventory = []
    # position list
    case_x = 0
    case_y = 15
    # image
    mac_image = pygame.image.load("MacGyver.png")

    def move_right (self, case_x, case_y):
        self.case_x + 1, case_y
        x = case_x * 25
        y = case_y * 25


    def move_left (self, case_x, case_y):
        self.case_x - 1, case_y
        x = case_x * 25
        y = case_y * 25

    def move_up (self, case_x, case_y):
        case_x, case_y - 1
        x = case_x * 25
        y = case_y * 25

    def move_down (self, case_x, case_y):
        case_x, case_y + 1
        x = case_x * 25
        y = case_y * 25

    # prise d’objet pour son inventaire
    def add_items(self, items):
        self.inventory.append(items)


class Guardian:
    # position list
    case_x = 15
    case_y = 0
    # image
    guard_image = pygame.image.load("Guardian.png")

class Item:

    png = ["needle.png", "serynge.png", "tube.png"]
    # Constructeur qui permettra au controlleur de créer les différents items du jeu
    def __init__(self, case_x, case_y, image):
        self.case_x = case_x
        self.case_y = case_y
        self.image = image

class Labyrinth:
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'labyrinth.txt')
    # image
    wall_image = pygame.image.load("wall.png")
    floor_image = pygame.image.load("floor.png")

    # initalisation de la liste labyrinth
    lab = []

    # géneration de la liste de liste labyrinth

    def generate_labyrinth (self):
        #Ouverture fichier (ajouter des caractères à la place des sprites)
        with open('labyrinth.txt', "r") as labyrinth:
            # Parcourt les lignes du fichier
            for line in labyrinth:
                lign = []
                # Parcourt les caractères du fichier
                for char in line:
                # On ignore fin de ligne
                    if char != "\n":
                        # Ajout caractère à la liste lign
                        lign.append(char)
                self.lab.append(lign)


##if __name__ == "__main__":
    ##laby = Labyrinth()
    ##laby.generate_labyrinth()
    ##print(Labyrinth.lab)



