# -*- coding: utf-8 -*-
####################
import pygame
import pygame_menu
from pygame.locals import*

pygame.init()
surface = pygame.display.set_mode((600, 400))
def set_difficulty(value, difficulty):
    pass
def start():
    fenetre = pygame.display.set_mode((600,400))
    fond = pygame.image.load('background_test.jpg').convert()
    fenetre.blit(fond, (0,0))
    perso = pygame.image.load('perso_test.png').convert_alpha()
    position = perso.get_rect()
    fenetre.blit(perso, position)
    pygame.display.flip()
    pygame.key.set_repeat(400,30)
    continuer = 1
    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    position = position.move(0,5)
                if event.key == K_UP:
                    position = position.move(0,-5)
                if event.key == K_RIGHT:
                    position = position.move(5,0)
                if event.key == K_LEFT:
                    position = position.move(-5,0)
        fenetre.blit(fond, (0,0))
        fenetre.blit(perso, position)
        pygame.display.flip()
menu = pygame_menu.Menu(400, 600, 'RPGPT',
                       theme=pygame_menu.themes.THEME_DARK)
menu.add_text_input('Name :', default='DOUZE')
menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2), ('Normal', 3)], onchange=set_difficulty)
menu.add_button('Play', start)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)