import pygame


class Display:
    def __init__(self):
        self.pygame_init = pygame.init()
        self.window = pygame.display.set_mode((375, 375))
        self.sprite = 25
        self.wall_image = None
        self.floor_image = None
        self.mac_image = None
        self.guard_image = None
        self.image = None

    def load_image(self, wall_image, floor_image, mac_image, guard_image, list):
        self.wall_image = pygame.image.load(wall_image)
        self.floor_image = pygame.image.load(floor_image)
        self.mac_image = pygame.image.load(mac_image)
        self.guard_image = pygame.image.load(guard_image)
        self.image = []

        for i in range(len(list)):
            self.image.append(pygame.image.load(list[i].image))

    def print_map(self, map):
        # # On parcourt la liste du niveau
        num_lign = 0
        for lign in map:
            # On parcourt les listes de lignes
            num_case = 0
            for sprite in lign:
                # On calcule la position réelle en pixels
                x = num_case * self.sprite
                y = num_lign * self.sprite
                if sprite == '1':  # '1' = wall
                    self.window.blit(self.wall_image, (x, y))
                elif sprite == '0':  # '0' = floor
                    self.window.blit(self.floor_image, (x, y))

                num_case += 1
            num_lign += 1

    def print_mac(self, case_x, case_y):
        # Position en pixel
        self.window.blit(self.mac_image, (case_x * self.sprite, case_y * self.sprite))

    def print_guard(self, case_x, case_y):
        # Position en pixel
        self.window.blit(self.guard_image, (case_x * self.sprite, case_y * self.sprite))

    def print_items(self, list):
        for i in range(len(list)):
            # position en pixel
            self.window.blit(self.image[i], (list[i].case_x * self.sprite, list[i].case_y * self.sprite))





