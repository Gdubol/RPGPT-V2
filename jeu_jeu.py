# -*- coding: utf-8 -*-
import pygame
from pygame.locals import*
from game import Game
from player import Player
from map import *

pygame.init()

#Affichage de la fenetre de jeu

pygame.display.set_caption('RPGPT') #Pour le titre de la fenetre
screen = pygame.display.set_mode((1080,720)) #Affichage fenetre (Note : affichage personnalisé à prévoir avec l'import des conditions données dans le menu)
background = pygame.image.load('background_test.jpg') #importation du background

game = Game() #initialisation du "game." pour la classe Game

player = Player() #initialisation du "player." pour la classe Player

perso_default = game.player.image_gauche #initialisation pour changer le sens du perso




running = True
while running:  #boucle infinie

    #en toute logique le fond (donc la map doit se mettre ici)
    #on va tester d'afficher le fond avec une boucle for case par case 10pxl par 10 pxl
    # print(map1) #pour test
    # print(len(map1)) #toujours un test

    for i in range(0, len(map1[0])):
        var1 = t_pxl*i
        for j in range(0, len(map1)):
            var2 = t_pxl*j
            if map1[j][i] == 1: #c'est une case_sol donc on va afficher une case sol ici
                screen.blit(case_sol, (var1, var2))
            if map1[j][i] == 2: #c'est une case_mur donc on va afficher une case mur ici
                screen.blit(case_mur, (var1, var2))
                L_case_mur.append((var1, var2))



    #### screen.blit(background, (0,0)) #mettre le fond #on cache ça pour le moment pour le test

    screen.blit(perso_default, game.player.rect) #appliquer l'image du joueur

    #afficher les projectiles sur l'écran
    for projectile in game.player.all_projectiles:
        projectile.move()

    game.player.all_projectiles.draw(screen) #dessine tout ce qu'il y a dans le groupe sur l'écran

    # game.all_monsters.draw(screen) #dessine les monstres test

    # if game.pressed.get(pygame.K_d):  #pour l'alternative des touches encore, pour les conditions de déplacements
    #     game.player.move_right()
    # elif game.pressed.get(pygame.K_q):
    #     game.player.move_left()

    pygame.display.flip() #mettre à jour l'écran

    # print(L_case_mur) #test pour collision
    # for case in L_case_mur:
    #     if game.player.rect.collidepoint(case):
    #         game.player.rect =

#Pour récupérer les positions des cases autour du perso on fait :
#   "game.player.rect.x"        Donne les coord x de la gauche du rectangle du perso
#   "game.player.rect.y"        Donne les coord y du haut du rectangle du perso
#   "game.player.rect.x + 80"   Donne les coord x de la droite du rectangle du perso
#   "game.player.rect.y + 60"   Donne les coord y du bas du rectangle du perso

    for event in pygame.event.get():

        #conditions de déplacement :
        
        Dpc_down = (    pygame.key.get_pressed()[pygame.K_s] == True and
                        game.player.rect.y + game.player.rect.height < t_pxl*len(map1)
                    )


        if event.type == pygame.QUIT:
            running = False #stop la boucle
            exec(open("jeu_menu0.1.py").read()) #femer le jeu et rouvre le menu (Note : à utiliser plus tard dans le menu Echap, avec un "Retour au Menu Principale")

        # elif event.type == pygame.KEYDOWN:  #détection des touches et activation ou désactivation
        #     game.pressed[event.key] = True
        # elif event.type == pygame.KEYUP:
        #     game.pressed[event.key] = False

#utilisation des Touches pour le déplacements et les interractions

        if  Dpc_down : #t_pxl est la variable pour le taille des pixels / c'est pour empêcher le perso de sortir de la fenêtre ici (Note = à gérer plus tard pour les collision avec les objets)
            game.player.move_down()

        if pygame.key.get_pressed()[pygame.K_z] and game.player.rect.y > 0:
            game.player.move_up()

        if pygame.key.get_pressed()[pygame.K_d] and game.player.rect.x + game.player.rect.width < t_pxl*len(map1[0]) : #t_pxl est la variable pour le taille des pixels
            game.player.move_right()
            perso_default = game.player.image_droite #met le perso vers la droite

        if pygame.key.get_pressed()[pygame.K_q] and game.player.rect.x > 0:
            game.player.move_left()
            perso_default = game.player.image_gauche #met le perso vers la gauche

        if pygame.key.get_pressed()[pygame.K_SPACE]: #touche projectiles
            game.player.lancement_projectile()

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            exec(open("jeu_menu0.1.py").read()) #femer le jeu et rouvre le menu (Note : à utiliser plus tard dans le menu Echap, avec un "Retour au Menu Principale")
















#
