import pygame

pygame.init()

fenetre = pygame.display.set_mode((750, 750))

floor = pygame.image.load("floor.png")
wall = pygame.image.load("wall.png")
fenetre.blit(floor, (0,0))
fenetre.blit(wall, (10,10))
#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
	continuer = int(input())