import pygame
import time
#classe pour le test projectile
class Projectile(pygame.sprite.Sprite):
    #comme on sera en point de vue du dessus je pensais rajouter une fonction qui lance des choses
    #si on fait pop des mobs sur la map on peut les fight en leur lancant des règles, stylo, colle (en mode cours Agoutin)
    #ça peut être fun de faire ça
    #on peut lancer aussi des cailloux pour activer un levier ou un bouton par exemple aussi

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
