"""Game mechanics with instantiation of model's objects"""
import random
import pygame
from model import Guardian
from model import Item
from model import Labyrinth
from model import MacGyver
from display import Display


class Controller:
    """Attributes and methods (game loop, view, ect...)
    of object type Controller"""

    def __init__(self):
        """Attributes of Controller :
        Instantiation of model's objects (MacGyver, Labyrinth, ect...).
        Variables which manage game mechanics (game, win, loose...)"""
        # Active or deactive game loop
        self.game = 1
        # Winning inventory
        self.win_inventory = 3
        # If the game is win
        self.win = False
        # If MacGyver is alive
        self.mac_is_alive = True
        # List of items
        self.items = []
        # Display instance
        self.dsp = Display()
        # Model instances
        self.mac_gyver = MacGyver(self.dsp.max_sprite, 0,
                                  "./images/MacGyver.png")
        self.guardian = Guardian(0, self.dsp.max_sprite,
                                 "./images/Guardian.png")
        self.labyrinth = Labyrinth("./images/wall.png",
                                   "./images/floor.png")

    def view(self):
        """Display of all objects on pygame window
        with methods call from class Display (display.py)."""
        # Load image from image instance attributes
        self.dsp.load_image(self.labyrinth.wall_image,
                            self.labyrinth.floor_image,
                            self.mac_gyver.mac_image,
                            self.guardian.guard_image,
                            self.items)
        # Print labyrinth
        self.dsp.print_map(self.labyrinth.lab)
        # Print MacGyver
        self.dsp.print_mac(self.mac_gyver.case_x, self.mac_gyver.case_y)
        # Print Guardian
        self.dsp.print_guard(self.guardian.case_x, self.guardian.case_y)
        # Print Items
        self.dsp.print_items(self.items)
        # Print Items counter
        self.dsp.print_counter_items(self.dsp.counter_text)
        if self.win is True:
            # Print "YOU WIN"
            self.dsp.print_result(self.dsp.win_text)
        if not self.mac_is_alive:
            # Print "YOU ARE DEAD"
            self.dsp.print_result(self.dsp.loose_text)
        # Refresh pygame window image
        pygame.display.flip()

    def generate_items(self):
        """Generation of random location of items (serynge, needle, tube)
        each time the game is opened"""
        number_of_items = 3
        # Image list
        png = ["./images/needle.png", "./images/syringe.png",
               "./images/tube.png"]
        # Generate x location list
        x_location = random.sample(range(self.dsp.max_sprite),
                                   number_of_items)
        # Generate y location list
        y_location = random.sample(range(self.dsp.max_sprite),
                                   number_of_items)
        # Loop for create item instance from class Item
        for i in range(number_of_items):
            # While position in lab list is not a wall
            while self.labyrinth.lab[y_location[i]][x_location[i]]\
                    == '1':
                # Change value x_location element list in position i
                x_location[i] = random.randint(self.dsp.min_sprite,
                                               self.dsp.max_sprite)
                # Change value y_location element list in position i
                y_location[i] = random.randint(self.dsp.min_sprite,
                                               self.dsp.max_sprite)
            # Creation of item in items list (Controller's attribute)
            self.items.append(Item(y_location[i], x_location[i], png[i]))

    def drop_item(self):
        """Add item in MacGyver inventory
        when MacGyver walk through it"""
        for item in self.items:
            # If MacGyver is on the same case of an item
            if item.case_x == self.mac_gyver.case_x \
                    and item.case_y == self.mac_gyver.case_y:
                # Add the item in MacGyver inventory
                self.mac_gyver.add_items()
                # Remove the item from items list
                self.items.remove(item)

    def counter_items(self):
        """Text mechanics to print number of
        item(s) in MacGyver's inventory
        at every moment of game"""
        # If Macgyver have one item in his inventory
        if len(self.mac_gyver.inventory) == 1:
            # The text is "items number : 1" with "#FFFF00" color
            self.dsp.counter_text = \
                self.dsp.items_font.render("items number : 1",
                                           True, pygame.Color("#FFFF00"))
        # If Macgyver have two item in his inventory
        elif len(self.mac_gyver.inventory) == 2:
            # The text is "items number : 2" with "#FFFF00" color
            self.dsp.counter_text = \
                self.dsp.items_font.render("items number : 2",
                                           True, pygame.Color("#FFFF00"))
        # If Macgyver have three item in his inventory
        elif len(self.mac_gyver.inventory) == 3:
            # The text is "items number : 3" with "#FFFF00" color
            self.dsp.counter_text = \
                self.dsp.items_font.render("items number : 3",
                                           True, pygame.Color("#FFFF00"))

    def check_results(self):
        """Check results when user meet guardian
        if he win or loose (MacGyver death)"""
        # If Macgyver have three item in his inventory
        # and he is exactly in the same guardian's position
        if len(self.mac_gyver.inventory) == self.win_inventory \
                and self.guardian.case_y == self.mac_gyver.case_y \
                and self.guardian.case_x == self.mac_gyver.case_x:
            # Victory
            self.win = True
            # If Macgyver is only in the same guardian's
            # position
        elif self.guardian.case_y == self.mac_gyver.case_y \
                and self.guardian.case_x == self.mac_gyver.case_x:
            # MacGyver dead
            self.mac_is_alive = False

        # In case of victory
        if self.win is True:
            # Delay to have time to see results
            pygame.time.delay(1000)
            # Game's close after delay
            self.game = 0

        # In case of death
        if not self.mac_is_alive:
            # Delay to have time to see results
            pygame.time.delay(1000)
            # Game's close after delay
            self.game = 0

    def game_loop(self):
        """Launching and maintaining the game.
        Manage user input to move MacGyver and play to the game"""
        # Generating labyrinth and items
        self.labyrinth.generate_labyrinth()
        self.generate_items()
        # Game loop
        while self.game == 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game = 0

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        # Check when user put K_RIGHT button
                        # if MacGyver will be out of map and/or in a wall
                        if self.dsp.max_sprite > self.mac_gyver.case_x\
                                >= self.dsp.min_sprite and\
                                self.labyrinth.lab[self.mac_gyver.case_y][
                                        self.mac_gyver.case_x + 1] != '1':
                            self.mac_gyver.move_right()

                    elif event.key == pygame.K_LEFT:
                        # Check when user put K_LEFT button
                        # if MacGyver will be out of map and/or in a wall
                        if self.dsp.max_sprite >= self.mac_gyver.case_x\
                                > self.dsp.min_sprite and\
                                self.labyrinth.lab[self.mac_gyver.case_y][
                                        self.mac_gyver.case_x - 1] != '1':
                            self.mac_gyver.move_left()

                    elif event.key == pygame.K_UP:
                        # Check when user put K_UP button
                        # if MacGyver will be out of map and/or in a wall
                        if self.dsp.max_sprite >= self.mac_gyver.case_y\
                                > self.dsp.min_sprite and\
                                self.labyrinth.lab[self.mac_gyver.case_y - 1][
                                        self.mac_gyver.case_x] != '1':
                            self.mac_gyver.move_up()

                    elif event.key == pygame.K_DOWN:
                        # Check when user put K_DOWN button
                        # if MacGyver will be out of map and/or in a wall
                        if self.dsp.max_sprite > self.mac_gyver.case_y\
                                >= self.dsp.min_sprite and\
                                self.labyrinth.lab[self.mac_gyver.case_y + 1][
                                        self.mac_gyver.case_x] != '1':
                            self.mac_gyver.move_down()

            # Call methods view() to print
            # all objects in pygame window
            self.view()

            # Check MacGyver action
            self.drop_item()
            self.counter_items()
            self.check_results()
            # Recall view() to print
            # results
            self.view()
