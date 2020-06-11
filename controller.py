import os
import pygame
from pygame.locals import *
import random
from model import Guardian
from model import Item
from model import Labyrinth
from model import MacGyver
from display import Display


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
        self.display = Display()
        self.labyrinth.generate_labyrinth()

    #DISPLAY
    def view(self):
        self.display.load_image(self.labyrinth.wall_image, self.labyrinth.floor_image, self.mac_gyver.mac_image, \
                           self.guardian.guard_image, self.items[0].image, \
                           self.items[1].image, self.items[2].image)

        self.display.print_map(self.labyrinth.lab, self.labyrinth.wall_image, self.labyrinth.floor_image)
        self.display.print_mac(self.mac_gyver.mac_image, self.mac_gyver.case_x, self.mac_gyver.case_y)
        self.display.print_guard(self.guardian.guard_image, self.guardian.case_x, self.guardian.case_y)
        self.display.print_items(self.items)

    def generate_items(self):
        number_of_items = 3
        png = ["needle.png", "syringe.png", "tube.png"]
        x = []
        y = []
        x_location = random.sample(range(14), 3)
        y_location = random.sample(range(14), 3)
        for i in range(number_of_items):
            while self.labyrinth.lab[x_location[i]][y_location[i]] == '1':
                x_location = random.sample(range(14), 3)
                y_location = random.sample(range(14), 3)
            x.append(x_location)
            y.append(y_location)
        for i in range(number_of_items):
            self.items.append(Item(y[i], x[i], png[i]))

    def game_loop(self):
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

