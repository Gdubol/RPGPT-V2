import pygame
import vars
import mapGen

FPS = vars.FPS
SPEED = vars.SPEED

screen = pygame.display.set_mode((vars.FENETREWIDTH, vars.FENETREHEIGHT))
clock = pygame.time.Clock()

# INIT DU PERSO ET DE SES VARIANTES
imgPerso = []
for i in range(0,8):
    imgPerso.append(pygame.image.load("perso"+str(i+1)+".png"))
rect = pygame.Rect((vars.SPAWNPOINTX, vars.SPAWNPOINTY), (32,32))

# VARS DE DEPL DU CUBEg
deplStatus = [False, False, False, False]
deplVel = [(0, -SPEED), (0, SPEED), (-SPEED, 0), (SPEED, 0)]
zqsd = [pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d]

# idDICT UTLISE POUR TEST
idDICT = {  (0,0,0) : 0,
            (255,255,255) : 1
            }

# imgDICT A DEFINIR POUR LE TEST DE MAP
imgDICT = {

}

# LISTE DES ENTITÉS COLLISION GENEREE DANS mapGen.py
tileMap, collideList = mapGen.loadFromImg('testImg.png', idDICT)

# DEBUT BOUCLE INFINIE POUR EVENT
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

    # TRACE DES ENTITES
    mapGen.loadMap(screen, tileMap, imgDICT)

    # BOUCLE DE CALCUL DE DEPLACEMENT
    for i in range(len(zqsd)):
        if deplStatus[i]:
            velX += deplVel[i][0]
            velY += deplVel[i][1]

    # GESTION DES COLLISIONS
    cloneRect = pygame.Rect((posX+velX, posY+velY), (32, 32))
    collision = cloneRect.collidelist(collideList[i] for i in range(len(collideList))]) != -1
    if not collision:
        rect.move_ip(velX, velY)
        posX, posY = rect.x, rect.y

    print("\rvelX={}, velY={} ; posX = {}, posY = {} ; collision : {}\t\t".format(velX, velY, posX, posY, collision), end = "")
    pygame.display.update()
