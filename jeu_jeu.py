# -*- coding: utf-8 -*-
import pygame
from pygame.locals import*

fenetre = pygame.display.set_mode((600,400))
fond = pygame.image.load('background_test.jpg').convert()
fenetre.blit(fond, (0,0))
perso = pygame.image.load('perso_test.png').convert_alpha()
position = perso.get_rect()
fenetre.blit(perso, position)
pygame.display.flip()
pygame.key.set_repeat(400,30)

def mainloop(fenetre,position):
    global perso, fond          #tres moche trouver une autre solution
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_s]:
                    position = position.move(0,5)
                if pygame.key.get_pressed()[pygame.K_z]:
                    position = position.move(0,-5)
                if pygame.key.get_pressed()[pygame.K_d]:
                    position = position.move(5,0)
                if pygame.key.get_pressed()[pygame.K_q]:
                    position = position.move(-5,0)
        fenetre.blit(fond, (0,0))
        fenetre.blit(perso, position)
        pygame.display.flip()

mainloop(fenetre,position)
