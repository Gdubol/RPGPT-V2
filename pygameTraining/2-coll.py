import pygame
# # TESTS D'IMPORTS REUSSIS
# successes, failures = pygame.init()
# print("{0} successes and {1} failures".format(successes, failures))

FPS = 60
VEL = 3
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((1080, 720))
clock = pygame.time.Clock()

# CUBE QUE L'ON CONTRÔLE
rect = pygame.Rect((100, 100), (32, 32))
perso = pygame.Surface((32, 32))
img = pygame.image.load("persoxd.png")

# VARS DE DEPL DU CUBE
deplStatus = [False, False, False, False]
deplVel = [(0, -VEL), (0, VEL), (-VEL, 0), (VEL, 0)]
zqsd = [pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d]

# CARTE DES ENTITÉS
collideMap =    [[pygame.Rect((0, 0), (720, 32)), pygame.Surface((720, 32))],
                [pygame.Rect((0, 448), (720, 32)), pygame.Surface((720, 32))],
                [pygame.Rect((0, 0), (32, 480)), pygame.Surface((32, 480))],
                [pygame.Rect((688, 0), (32, 480)), pygame.Surface((32, 480))]]

while True:
    clock.tick(FPS)
    velX, velY = 0, 0
    posX, posY = rect.x, rect.y

    # DÉTECTION DES ENTRÉES UTILISATEURS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            for i in range(len(zqsd)):
                if event.key == zqsd[i]:
                    deplStatus[i] = True

        if event.type == pygame.KEYUP:
            for i in range(len(zqsd)):
                if event.key == zqsd[i]:
                    deplStatus[i] = False

    # TRACÉ DES ENTITÉS
    screen.fill(BLACK)
    screen.blit(img, rect)
    for border in collideMap:
        border[1].fill(RED)
        screen.blit(border[1], border[0])

    # BOUCLE DE CALCUL DE DEPLACEMENT
    for i in range(len(zqsd)):
        if deplStatus[i]:
            velX += deplVel[i][0]
            velY += deplVel[i][1]

    # TEST DE COLLISION
    # On crée un Rect qui aura la position prévue s'il n'y a pas de collision
    # On teste s'il y a collision avec le Rect prévu

    cloneRect = pygame.Rect((posX+velX, posY+velY), (32, 32))
    collision = cloneRect.collidelist([collideMap[i][0] for i in range(len(collideMap))]) != -1
    if not collision:
        # Pas de collision : le mvt est valide
        rect.move_ip(velX, velY)
        posX, posY = rect.x, rect.y

    # Sortie de contrôle sur la console
    print("\rvelX={}, velY={} ; posX = {}, posY = {} ; collision : {}\t\t".format(velX, velY, posX, posY, collision), end = "")
    pygame.display.update()
