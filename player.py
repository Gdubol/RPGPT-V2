import pygame
from projectile import Projectile 

#classe pour le perso du joueur
class Player(pygame.sprite.Sprite):

    #Toutes les valeurs qu'on initialise sont données ici
    def __init__(self):
        super().__init__()
        # self.game = game
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
        self.rect.x = 250 #positionnement du perso
        self.rect.y = 250

    #Définition des projectiles
    def lancement_projectile(self):
        self.all_projectiles.add(Projectile(self))

    #Définition des déplacements au sein de la classe Player
    def move_right(self):
        self.rect.x += self.speed
        # if not self.game.check_collision(self, self.game.all_monsters):
        #     self.rect.x += self.speed
    def move_left(self):
        self.rect.x -= self.speed
    def move_up(self):
        self.rect.y -= self.speed
    def move_down(self):
        self.rect.y += self.speed
