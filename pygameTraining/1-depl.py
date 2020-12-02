import pygame
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))


screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60

VEL = 5
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

rect = pygame.Rect((0, 0), (32, 32))
image = pygame.Surface((32, 32))
image.fill(WHITE)

deplStatus = [False, False, False, False]
deplVel = [(0, -VEL), (0, VEL), (-VEL, 0), (VEL, 0)]
zqsd = [pygame.K_z, pygame.K_s, pygame.K_q, pygame.K_d]

while True:
    clock.tick(FPS)
    velX, velY = 0, 0
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

    for i in range(len(zqsd)):
        if deplStatus[i]:
            velX += deplVel[i][0]
            velY += deplVel[i][1]
    print("\rvelX={}, velY={}   ".format(velX, velY), end = "")
    rect.move_ip(velX, velY)

    screen.fill(BLACK)
    screen.blit(image, rect)
    pygame.display.update()
