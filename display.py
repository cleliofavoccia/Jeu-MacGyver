import pygame
import controller


class Display:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((375, 375))
        self.sprite = 25
        self.ctr = controller.Controller()

    def load_image(self):
        pygame.image.load(self.ctr.labyrinth.wall_image)
        pygame.image.load(self.ctr.labyrinth.floor_image)
        pygame.image.load(self.ctr.mac_gyver.mac_image)
        pygame.image.load(self.ctr.guardian.guard_image)

    def map(self, controller):
        # # On parcourt la liste du niveau
        num_lign = 0
        for lign in self.ctr.labyrinth.lab:
            # On parcourt les listes de lignes
            num_case = 0
            for sprite in lign:
                # On calcule la position réelle en pixels
                x = num_case * self.sprite
                y = num_lign * self.sprite
                if sprite == '1':  # '1' = wall
                    self.window.blit(self.ctr.labyrinth.wall_image, (x, y))
                elif sprite == '0':  # '0' = floor
                    self.window.blit(self.ctr.labyrinth.floor_image, (x, y))

            num_case += 1
        num_lign += 1


    def mac(self):
        # Position en pixel
        self.window.blit(self.ctr.mac_gyver.mac_image, \
                         (self.ctr.mac_gyver.case_x * self.sprite, \
                          self.ctr.mac_gyver.case_y * self.sprite))


    def guard(self):
        # Position en pixel
        self.window.blit(self.ctr.guardian.guard_image, \
                         (self.ctr.guardian.case_x * self.sprite, \
                          self.ctr.guardian.case_y * self.sprite))


    def items(self):
        # position en pixel
        for item in self.ctr.items:
            self.window.blit(item.png, (item.case_x * self.sprite, item.case_y * self.sprite))




