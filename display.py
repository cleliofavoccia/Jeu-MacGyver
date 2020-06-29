"""Creation of methods to display the game"""
import pygame


class Display:
    """Attributes and methods of objects type Display"""
    def __init__(self):
        """Attributes of Display :
        Initialization of pygame and pygame window with his features.
        Initialization of objects image
        """
        self.pygame = pygame.init()
        # Window initialization
        self.window = pygame.display.set_mode((375, 375))
        # Sprites size in pixels
        self.sprite = 25
        # Max sprite in width and height
        self.max_sprite = 14
        # Min sprite in width and height
        self.min_sprite = 0
        # Counter items font and text
        self.items_font = pygame.font.Font(None, 18)
        self.counter_text = self.items_font.render("items number : 0", True,
                                                   pygame.Color("#FFFF00"))
        # Event win/loose font and text
        self.wl_font = pygame.font.Font(None, 50)
        self.win_text = self.wl_font.render("YOU WIN",
                                            True, pygame.Color("#FFFF00"))
        self.loose_text = self.wl_font.render("YOU ARE DEAD",
                                              True, pygame.Color("#FFFF00"))
        # Object image initialization
        self.wall_image = None
        self.floor_image = None
        self.mac_image = None
        self.guard_image = None
        self.image = None

    def load_image(self, wall_image, floor_image,
                   mac_image, guard_image, list):
        """Load images for all objects insert in parameters"""
        self.wall_image = pygame.image.load(wall_image)
        self.floor_image = pygame.image.load(floor_image)
        self.mac_image = pygame.image.load(mac_image)
        self.guard_image = pygame.image.load(guard_image)
        # Load image for item in items list
        self.image = []
        for i in range(len(list)):
            self.image.append(pygame.image.load(list[i].image))

    def print_map(self, map):
        """Build the labyrinth map from labyrinth list
        insert in parameter,
        and print the labyrinth map in game"""
        # We browse the lists
        num_line = 0
        for line in map:
            # We browse the elements in each list
            num_case = 0
            for sprite in line:
                # We calculate the location in pixels
                x = num_case * self.sprite
                y = num_line * self.sprite
                if sprite == '1':  # '1' = wall
                    self.window.blit(self.wall_image, (x, y))
                elif sprite == '0':  # '0' = floor
                    self.window.blit(self.floor_image, (x, y))

                num_case += 1
            num_line += 1

    def print_mac(self, case_x, case_y):
        """Print MacGyver position
        with an image in game"""
        # Location in pixels
        self.window.blit(self.mac_image,
                         (case_x * self.sprite,
                          case_y * self.sprite))

    def print_guard(self, case_x, case_y):
        """Print Guardian position
        with an image in game"""
        # Location in pixels
        self.window.blit(self.guard_image,
                         (case_x * self.sprite,
                          case_y * self.sprite))

    def print_items(self, list):
        """Print items position
        with an image in game"""
        # Location in pixels for each item in items list
        for i in range(len(list)):
            self.window.blit(self.image[i],
                             (list[i].case_x * self.sprite,
                              list[i].case_y * self.sprite))

    def print_counter_items(self, text):
        """Print number of item(s)
         in MacGyver inventory in game"""
        self.window.blit(text, (0, 0))

    def print_result(self, text):
        """Print if the user win or loose in game"""
        self.window.blit(text, (50, 100))
