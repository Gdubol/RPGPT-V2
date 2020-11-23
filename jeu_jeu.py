# -*- coding: utf-8 -*-
import pygame
from pygame.locals import*




# fenetre = pygame.display.set_mode((600,400))
# fond = pygame.image.load('background_test.jpg').convert()
# rock = pygame.image.load('rock.png').convert()
# perso = Player()
# position = perso.get_rect()
# pos_rock = rock.get_rect()
# fenetre.blit(fond, (0,0))
# fenetre.blit(rock, (50,50))
# fenetre.blit(perso, position)
# pygame.display.flip() #mettre à jour la fenetre
# pygame.key.set_repeat(400,30)
#
# def fct_inventaire():
#     fond_inventaire = pygame.image.load('inventaire.png').convert()
#     fenetre.blit(fond_inventaire, (0,0))
#
# def mainloop(fenetre,position):
#     global perso, fond, rock        #tres moche trouver une autre solution
#     continuer = 1
#     while continuer:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 continuer = 0
#                 pygame.quit()
#                 print("Fermeture du jeu")
#             if event.type == KEYDOWN:
#                 if pygame.key.get_pressed()[pygame.K_s]:
#                     position = position.move(0,5)
#                 if pygame.key.get_pressed()[pygame.K_z]:
#                     position = position.move(0,-5)
#                 if pygame.key.get_pressed()[pygame.K_d]:
#                     position = position.move(5,0)
#                 if pygame.key.get_pressed()[pygame.K_q]:
#                     position = position.move(-5,0)
#                 if pygame.key.get_pressed()[pygame.K_ESCAPE]:
#                     pygame.quit()
#                 if pygame.key.get_pressed()[pygame.K_i]:
#                     fond = pygame.image.load('inventaire.png').convert()
#                     fenetre.blit(fond, (0,0))
#                     #fct_inventaire()
#
#
#         fenetre.blit(fond, (0,0))
#         fenetre.blit(rock, (50,50))
#         fenetre.blit(perso, position)
#         pygame.display.flip()
#
# mainloop(fenetre,position)
pygame.init()

class Game:

    def __init__(self):
        self.player = Player()

#classe pour le perso du joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        self.health = 144
        self.max_health = 144
        self.attack = 12
        self.speed = 5
        self.image = pygame.image.load('perso_test.png')
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 250

    def move_right(self):
        self.rect.x += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed

pygame.display.set_caption('RPGPT')
screen = pygame.display.set_mode((1080,720))
background = pygame.image.load('background_test.jpg')
game = Game()
player = Player()

running = True
while running:
    screen.blit(background, (0,0))
    screen.blit(game.player.image, game.player.rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print('Fermeture du jeu')
        elif event.type == KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_s]:
                game.player.move_down()
            if pygame.key.get_pressed()[pygame.K_z]:
                game.player.move_up()
            if pygame.key.get_pressed()[pygame.K_d]:
                game.player.move_right()
            if pygame.key.get_pressed()[pygame.K_q]:
                game.player.move_left()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()

















#
