import pygame
from model import Item
from model import MacGyver
from model import Guardian
from model import Labyrinth

from pygame.locals import *
import random


class Controller:

    win = False
    mac_is_alive = True
    needle = None
    serynge = None
    tube = None
    mac_gyver = MacGyver()
    guardian = Guardian()
    labyrinth = Labyrinth()
    display = Display()

    def generate_items(self):
        png = ["needle.png", "serynge.png", "tube.png"]
        x = []
        y = []
        for i in range(3):
            x_location = random.sample(self.labyrinth.lab, 1)
            while x_location != 1 and x_location in x:
                x_location = random.sample(self.labyrinth.lab, 1)
            y_location = random.sample(self.labyrinth.lab, 1)
            while y_location != 1 and y_location in y:
                y_location = random.sample(self.labyrinth.lab, 1)
            x.append(self.labyrinth.lab.[x_location])
            y.append(self.labyrinth.lab.[y_location])
        self.needle = Item(x[0], y[0], "needle.png")
        self.serynge = Item(x[1], y[1], "serynge.png")
        self.tube = Item(x[2], y[2], "tube.png")

    def display(self):
        display.map()
        display.mac()
        display.guard()
        display.serynge()
        display.needle()
        display.tube()

    def gameloop(self): 
        while game:
            for event in pygame.event.get():
                if event.type == QUIT:
                    game = 0

                elif event.type == KEYDOWN:
                # move button
                elif event.key == K_RIGHT:
                    if mac_gyver.case_x < 24:
                        if labyrinth.lab[mac_gyver.case_x + 1][mac_gyver.case_y] != 1
                            mac_gyver.move_right
                elif event.key == K_LEFT:
                    if mac_gyver.case_x < 24:
                        if labyrinth.lab[mac_gyver.case_x - 1][mac_gyver.case_y] != 1
                            mac_gyver.move_left

                elif event.key == K_UP:
                    if mac_gyver.case_x < 24:
                        if labyrinth.lab[mac_gyver.case_x][mac_gyver.case_y - 1] != 1
                            mac_gyver.move_up
                elif event.key == K_DOWN:
                    if mac_gyver.case_x < 24:
                        if labyrinth.lab[mac_gyver.case_x][mac_gyver.case_y + 1] != 1
                            mac_gyver.move_down

        # Mise en inventaire
        if [serynge.case_x][serynge.case_y] == [mac_gyver.case_x][mac_gyver.case_y]:
            mac_gyver.add_serynge
        if [needle.case_x][needle.case_y] == [mac_gyver.case_x][mac_gyver.case_y]:
            mac_gyver.add_needle
        if [tube.case_x][tube.case_y] == [mac_gyver.case_x][mac_gyver.case_y]:
            mac_gyver.add_tube

        pygame.display.flip()

        # Check Victory/Loose
        if mac_gyver.len(mac_gyver.inventory) == 3 and [guardian.case_x][guardian.case_y] == [mac_gyver.case_x][mac_gyver.case_y]:
            win = True
        else:
            mac_is_alive = False

        # Victory
        if win == True:
            print("You win")
            game = 0
        # Loose
        if mac_is_alive == False:
            print("You loose")
            game = 0



    # def init(self):
    #     pygame.init()
    #     game = 1
    #
    # # Ouverture de la fenêtre Pygame
    # fenetre = pygame.display.set_mode((375, 375))
    # # Tout afficher
    # display()
    # # Faire la boucle de jeu
    # gameloop()



