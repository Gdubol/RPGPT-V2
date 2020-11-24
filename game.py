import pygame
from player import Player
from monster import Monster

#classe pour le jeu
class Game:

    def __init__(self):
        self.player = Player()
        # self.pressed = {}  ##alternative pour les touches, creer un dictionnaire des touches avec True ou False pour si appuyer ou pas
        self.all_monsters = pygame.sprite.Group()
        self.spawn_monster()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster()
        self.all_monsters.add(monster)
