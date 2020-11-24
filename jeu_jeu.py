# -*- coding: utf-8 -*-
import pygame
from pygame.locals import*
import time

pygame.init()

#classe pour le jeu
class Game:

    def __init__(self):
        self.player = Player()
        # self.pressed = {}  ##alternative pour les touches, creer un dictionnaire des touches avec True ou False pour si appuyer ou pas

#classe pour le test projectile
class Projectile(pygame.sprite.Sprite):
    #comme on sera en point de vue du dessus je pensais rajouter une fonction qui lance des choses
    #si on fait pop des mobs sur la map on peut les fight en leur lancant des règles, stylo, colle (en mode cours Agoutin)
    #ça peut être fun de faire ça

    def __init__(self, player): #on récupère les infos joueur dans le constructeur
        super().__init__()
        self.vitesse = 1
        self.player = player
        self.image = pygame.image.load('projectile.png')
        self.image = pygame.transform.scale(self.image, (80,80))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x - 60
        self.rect.y = player.rect.y - 18
        self.origin_image = self.image #on crée une image résiduel pour pouvoir la modifier en la tournant après
        self.angle = 0 #on déf l'angle de base pour le 'rotate'

    #pour faire tourner les projectiles
    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1) #rotozoom bb
        self.rect = self.image.get_rect(center = self.rect.center)

    #pour virer les projectiles qui sortent de l'écran
    def remove(self):
        self.player.all_projectiles.remove(self)

    #pour faire bouger les projectiles (Note : dans l'idéal faire une fonction qui bouge par rapport à un vecteur dans la direction de la souris)
    def move(self):
        self.rect.x -= self.vitesse #reglage de la vitesse (déjà au minimum d'ailleurs et c'est trop rapide à mon goût ce qui m'a obligé à faire l'histoire du time.sleep projectiles)
        self.rotate() #pour faire des projectiles tournant pcq c'est plus fun
        time.sleep(0.0001) #slow pour les projectiles et plus on en tire moins ils vont vite

        #penser à vérifier qu'il est plus sur l'écran pour le détruire
        if self.rect.x < 0:
            self.remove()


#classe pour le perso du joueur
class Player(pygame.sprite.Sprite):

    #Toutes les valeurs qu'on initialise sont données ici
    def __init__(self):
        super().__init__()
        #truc à perso plus tard
        self.health = 144 #pt de vie de base du perso
        self.max_health = 144 #cap max en cas de recup de vie par exemple
        self.attack = 12 #attack de base du perso

        #le set du groupe de projectiles pour qu'on en ai plusieurs en même temps
        self.all_projectiles = pygame.sprite.Group()

        #vitesse de l'image du perso
        self.speed = 10

        #bordel du perso et de son affichage
        self.image_gauche = pygame.image.load('perso_test_gauche.png') #importer image perso
        self.image_droite = pygame.image.load('perso_test_droite.png')
        self.rect = self.image_gauche.get_rect() #récup sa position sous forme d'un carré qui prend ses dimensions
        #self.rect = self.image_droite.get_rect()
        self.rect.x = 250 #positionnement du perso
        self.rect.y = 250

    #Définition des projectiles
    def lancement_projectile(self):
        self.all_projectiles.add(Projectile(self))

    #Définition des déplacements au sein de la classe Player
    def move_right(self):
        self.rect.x += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed

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
