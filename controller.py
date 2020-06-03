import pygame
from pygame.locals import *
import random
from model import Guardian
from model import Item
from model import Labyrinth
from model import MacGyver
import display


class Controller:
    def __init__(self):
        self.game = 1
        self.win_inventory = 3
        self.win = False
        self.mac_is_alive = True
        self.items = []
        self.mac_gyver = MacGyver(14, 0, "MacGyver.png")
        self.guardian = Guardian(0, 14, "Guardian.png")
        self.labyrinth = Labyrinth("wall.png", "floor.png")
        self.gen_lab = Labyrinth.generate_labyrinth(self.labyrinth)
        self.disp = display.Display()


    def generate_items(self):
        number_of_items = 3
        png = ["needle.png", "serynge.png", "tube.png"]
        x = []
        y = []
        # METHODE AVEC RANDOM.SAMPLE
        x_location = random.sample(range(15), 3)
        y_location = random.sample(range(15), 3)
        for i in range(number_of_items):
            while self.labyrinth.lab[x_location[i]][y_location[i]] == '1':
                x_location = random.sample(range(15), 3)
                y_location = random.sample(range(15), 3)
            x.append(x_location)
            y.append(y_location)
        for i in range(number_of_items):
            self.items.append(Item(y[i], x[i], png[i]))

    def display(self):
        self.disp.load_image()
        self.disp.map()
        self.disp.mac()
        self.disp.guard()
        self.disp.items()

    def gameloop(self):
        while self.game == 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game = 0

                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        if self.mac_gyver.case_x < 14:
                            if self.labyrinth.lab[self.mac_gyver.case_y][self.mac_gyver.case_x + 1] != '1':
                                self.mac_gyver.move_right()
                    elif event.key == K_LEFT:
                        if self.mac_gyver.case_x < 14:
                            if self.labyrinth.lab[self.mac_gyver.case_y][self.mac_gyver.case_x - 1] != '1':
                                self.mac_gyver.move_left()

                    elif event.key == K_UP:
                        if self.mac_gyver.case_y < 14:
                            if self.labyrinth.lab[self.mac_gyver.case_y - 1][self.mac_gyver.case_x] != '1':
                                self.mac_gyver.move_up()
                    elif event.key == K_DOWN:
                        if self.mac_gyver.case_y < 14:
                            if self.labyrinth.lab[self.mac_gyver.case_y + 1][self.mac_gyver.case_x] != '1':
                                self.mac_gyver.move_down()

        # Mise en inventaire
        for item in self.items:
            if item.case_x == self.mac_gyver.case_x and item.case_y == self.mac_gyver.case_y:
                self.mac_gyver.add_items(item)


        # Check Victory/Loose
        if len(self.mac_gyver.inventory) == self.win_inventory and self.guardian.case_y == self.mac_gyver.case_y and \
                self.guardian.case_x == self.mac_gyver.case_x:
            self.win = True
        elif self.guardian.case_y == self.mac_gyver.case_y and self.guardian.case_x == self.mac_gyver.case_x:
            self.mac_is_alive = False

        # Victory
        if self.win:
            print("You win")
            self.game = 0
        # Loose
        if not self.mac_is_alive:
            print("You loose")
            self.game = 0

        pygame.display.flip()


if __name__ == "__main__":
    controller = Controller()
    # Overture Pygame window

    # Generate labyrinth
    controller.gen_lab
    # Generate items
    controller.generate_items()
    # Display
    controller.disp()
    # Game loop
    controller.gameloop()

