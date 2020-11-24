import pygame

class Monster(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('caillou_ennemi.png')
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
