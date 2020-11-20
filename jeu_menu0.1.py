# -*- coding: utf-8 -*-
####################
import pygame
import pygame_menu
from pygame.locals import*

X = 800
Y = 600
pygame.init()
surface = pygame.display.set_mode((X, Y))

def set_difficulty(value, difficulty):
    pass

def option():
    def set_resolution(value, resolution):
        name, index = value
        print("Change résolution to : ", name)
        X = resolution[0]
        Y = resolution[1]
        surface_option = pygame.display.set_mode((X,Y))
    surface_option = pygame.display.set_mode((X,Y))
    menu_option = pygame_menu.Menu(Y, X, 'RPGPT')
    menu.add_selector('Affichage :', [('720 x 480',(720,480)),('720 x 576',(720,576)),('1280 x 720',(1280,720)),('1280 x 1024',(1280,1024)),('1920 x 1080',(1920,1080))], onchange = set_resolution)
    menu.mainloop(surface)

def start():
    pass
    #import jeu_debut

menu = pygame_menu.Menu(Y, X, 'RPGPT', theme=pygame_menu.themes.THEME_DARK)
menu.add_text_input('Name :', default='THE DOUZEUR')
menu.add_selector('Difficulty :', [('Hard', 3), ('Easy', 2), ('Normal', 1)], onchange=set_difficulty)
menu.add_vertical_margin(100)
menu.add_button('Play', start)
menu.add_button('Option', option)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)
