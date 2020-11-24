# -*- coding: utf-8 -*-
import pygame
from pygame.locals import*
from game import Game
from player import Player

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
    screen.blit(background, (0,0)) #mettre le fond
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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #stop la boucle
            exec(open("jeu_menu0.1.py").read()) #femer le jeu et rouvre le menu (Note : à utiliser plus tard dans le menu Echap, avec un "Retour au Menu Principale")

        # elif event.type == pygame.KEYDOWN:  #détection des touches et activation ou désactivation
        #     game.pressed[event.key] = True
        # elif event.type == pygame.KEYUP:
        #     game.pressed[event.key] = False

#utilisation des Touches pour le déplacements et les interractions

        if pygame.key.get_pressed()[pygame.K_s] and game.player.rect.y + game.player.rect.height < background.get_height() :
            game.player.move_down()
        if pygame.key.get_pressed()[pygame.K_z] and game.player.rect.y > 0:
            game.player.move_up()
        if pygame.key.get_pressed()[pygame.K_d] and game.player.rect.x + game.player.rect.width < background.get_width() :
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
