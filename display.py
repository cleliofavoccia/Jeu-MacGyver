import pygame


class Display:
    def __init__(self):
        self.pygame_init = pygame.init()
        self.window = pygame.display.set_mode((375, 375))
        self.sprite = 25

    def load_image(self, wall_image, floor_image, mac_image, guard_image, item1, item2, item3):
        pygame.image.load(wall_image)
        pygame.image.load(floor_image)
        pygame.image.load(mac_image)
        pygame.image.load(guard_image)
        pygame.image.load(item1)
        pygame.image.load(item2)
        pygame.image.load(item3)

    def print_map(self, map, wall_image, floor_image):
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
                    self.window.blit(wall_image, (x, y))
                elif sprite == '0':  # '0' = floor
                    self.window.blit(floor_image, (x, y))

            num_case += 1
        num_lign += 1

    def print_mac(self, mac_image, case_x, case_y):
        # Position en pixel
        self.window.blit(mac_image, (case_x * self.sprite, case_y * self.sprite))

    def print_guard(self, guard_image, case_x, case_y):
        # Position en pixel
        self.window.blit(guard_image, (case_x * self.sprite, case_y * self.sprite))

    def print_items(self, items):
        for item in items:
            # position en pixel
            self.window.blit(items[item].image, (items[item].case_x * self.sprite, items[item].case_y * self.sprite))





