# -*- coding: utf-8 -*-
####################
import pygame
import pygame_menu
from pygame.locals import*
import pygame_menu.events as _events
import pygame_menu.widgets as _widgets

def getParam(param, file):
    f = open("{0}.txt".format(file), "r")
    x = f.readlines()
    f.close()
    for i in range(len(x)):
        x[i] = x[i].strip("\n").split(":")
    value = None
    for cfgParam, cfgVal in x:
        if cfgParam == param:
            value = cfgVal
    return value
def setParam(param, value, file):
    f = open("{0}.txt".format(file), "r")
    x = f.readlines()
    for i in range(len(x)):
        x[i] = x[i].strip("\n").split(":")
    f = open("{0}.txt".format(file), "w")
    for cfgParam, cfgVal in x:
        if cfgParam != param:
            f.write("{0}:{1}\n".format(cfgParam, cfgVal))
        else:
            f.write("{0}:{1}\n".format(param, value))
            print("[LOG] Changed {0} from {1} to {2}".format(param, cfgVal, value))
    return None
# print(getParam("cx", "test"))
# setParam("cx", "pute", "test")
# print(getParam("cx", "test"))


X = 1280
Y = 720

pygame.init()
surface = pygame.display.set_mode((X, Y))
Mytheme = pygame_menu.themes.Theme( background_color = (0,0,0,0),
                                    title_shadow = True,
                                    title_background_color = (74,101,127),
                                    title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
                                    widget_font = pygame_menu.font.FONT_MUNRO,
                                    widget_font_size = 40,
                                    cursor_color = (135,73,187),
                                    title_font =  pygame_menu.font.FONT_MUNRO,
                                    title_font_color = (147,87,5),
                                    title_font_size = 50)

def set_difficulty(value, difficulty):
    pass


def option():

    def set_resolution(value, resolution): 
        pass
        # name, index = value
        # print("Change résolution to : ", name)
        # X = resolution[0]
        # Y = resolution[1]
        # surface_option = pygame.display.set_mode((X,Y))
        # menu_option = pygame_menu.Menu(Y, X, 'RPGPT', theme=Mytheme)

    def controle(): #FONCTIONNE PAS !!!! fonction pour afficher toutes les touches utiles dans le jeu / avec futur possibilité de les changers
        def change_touche(): #futur fonction de changement de touches
            pass
        _events.CLOSE #devrait fermer toutes les fenetres pygame_menu
        surface_controle = pygame.display.set_mode((X,Y))
        menu_controle = pygame_menu.Menu(Y,X, 'RPGPT', theme = Mytheme)
        menu_controle.add_button('FORWARD : ', change_touche() ) #prévoir d'ajouter la possibilité de voir la touche en question qui est mise sur chaque fonction avec ### +getParam("FORWARD", "controle.txt") ###
        menu_controle.add_button('BACKWARD : ', change_touche() )
        menu_controle.add_button('LEFT : ', change_touche() )
        menu_controle.add_button('RIGHT : ', change_touche() )


    menu.disable #désactive le premier menu
    surface_option = pygame.display.set_mode((X,Y)) #active le second menu, pour les options
    menu_option = pygame_menu.Menu(Y,X, 'RPGPT', theme = Mytheme)
    menu_option.add_selector('Affichage :', [('720 x 480',(720,480)),('720 x 576',(720,576)),('1280 x 720',(1280,720)),
                                            ('1280 x 1024',(1280,1024)),('1920 x 1080',(1920,1080))], onchange = set_resolution)
    menu_option.add_button('Controle', controle()) #pourquoi ce boutton ne marche pas je ne comprends pas XD
    menu_option.add_button('Save Return Menu', menu_option.disable)
    menu_option.mainloop(surface)

def start(): #fonction pour lancer le programme de jeu / fonctionnel en l'état
    pygame_menu.events.EXIT #on ferme tout le bordel du pygame_menu
    import jeu_jeu #import pour utiliser la fonction après
    exec(open("jeu_jeu.py").read()) #ouverture du fichier
#    mainloop(fenetre,position) #on ouvre la fonction pour les déplacements de jeu_jeu.py ##ça marche pas en faite

menu = pygame_menu.Menu(Y, X, 'RPGPT', theme = Mytheme)
menu.add_text_input('Name :', default='THE DOUZEUR')
menu.add_selector('Difficulty :', [('Hard', 3), ('Easy', 2), ('Normal', 1)], onchange=set_difficulty)
menu.add_vertical_margin(100)
menu.add_button('Play', start)
menu.add_button('Option', option)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)
