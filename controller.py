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
        self.max_sprite = 14
        self.min_sprite = 0
        self.items = []
        self.mac_gyver = MacGyver(self.max_sprite, 0, "MacGyver.png")
        self.guardian = Guardian(0, self.max_sprite, "Guardian.png")
        self.labyrinth = Labyrinth("wall.png", "floor.png")
        self.display = Display()
        self.labyrinth.generate_labyrinth()
        self.generate_items()

    # DISPLAY
    def view(self):
        self.display.load_image(self.labyrinth.wall_image, self.labyrinth.floor_image, self.mac_gyver.mac_image, \
                                self.guardian.guard_image, self.items)

        self.display.print_map(self.labyrinth.lab)
        self.display.print_mac(self.mac_gyver.case_x, self.mac_gyver.case_y)
        self.display.print_guard(self.guardian.case_x, self.guardian.case_y)
        self.display.print_items(self.items)
        pygame.display.flip()
        pygame.display.update()

    def generate_items(self):
        number_of_items = 3
        png = ["needle.png", "syringe.png", "tube.png"]
        # x_location = [0,0,0]
        # y_location = [0,0,0]
        x_location = random.sample(range(self.max_sprite), number_of_items)
        y_location = random.sample(range(self.max_sprite), number_of_items)
        for i in range(number_of_items):
            while self.labyrinth.lab[y_location[i]][x_location[i]] == '1':
                x_location[i] = random.randint(self.min_sprite, self.max_sprite)
                y_location[i] = random.randint(self.min_sprite, self.max_sprite)
            self.items.append(Item(y_location[i], x_location[i], png[i]))

        # for i in range(number_of_items):
        #     print(self.labyrinth.lab[6][12])
        #     x_location[i] = random.randint(0, 14)
        #     y_location[i] = random.randint(0, 14)
        #     while self.labyrinth.lab[x_location[i]][y_location[i]] == '1':
        #         x_location[i] = random.randint(0, 14)
        #         y_location[i] = random.randint(0, 14)
        #     self.items.append(Item(y_location[i], x_location[i], png[i]))

    def game_loop(self):
        while self.game == 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game = 0

                elif event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        if self.max_sprite > self.mac_gyver.case_x >= self.min_sprite:
                            if self.labyrinth.lab[self.mac_gyver.case_y][self.mac_gyver.case_x + 1] != '1':
                                self.mac_gyver.move_right()

                    elif event.key == K_LEFT:
                        if self.max_sprite >= self.mac_gyver.case_x > self.min_sprite:
                            if self.labyrinth.lab[self.mac_gyver.case_y][self.mac_gyver.case_x - 1] != '1':
                                self.mac_gyver.move_left()

                    elif event.key == K_UP:
                        if self.max_sprite >= self.mac_gyver.case_y > self.min_sprite:
                            if self.labyrinth.lab[self.mac_gyver.case_y - 1][self.mac_gyver.case_x] != '1':
                                self.mac_gyver.move_up()

                    elif event.key == K_DOWN:
                        if self.max_sprite > self.mac_gyver.case_y >= self.min_sprite:
                            if self.labyrinth.lab[self.mac_gyver.case_y + 1][self.mac_gyver.case_x] != '1':
                                self.mac_gyver.move_down()
            self.view()
            pygame.display.flip()

            # Add items in Mac Gyver inventory
            for item in self.items:
                if item.case_x == self.mac_gyver.case_x and item.case_y == self.mac_gyver.case_y:
                    self.mac_gyver.add_items()
                    self.items.remove(item)

            # Check Victory/Loose
            if len(self.mac_gyver.inventory) == self.win_inventory and self.guardian.case_y == self.mac_gyver.case_y \
                    and self.guardian.case_x == self.mac_gyver.case_x:
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
