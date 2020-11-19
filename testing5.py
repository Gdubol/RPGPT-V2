import pygame
import pygame_menu
pygame.init()
surface = pygame.display.set_mode((600, 400))
def set_difficulty(value, difficulty):
    pass
def start():
    x = 1000
    y = 900
    pygame.event.clear
    fenetre = pygame.display.set_mode((x,y))
    #fenetre = pygame.display.set_mode((640,480), FULLSCREEN)

    fond = pygame.image.load('background.png').convert() #importer une image
    fenetre.blit(fond, (0,0)) #positionner l'image dans la fenetre -- 0,0 = coin en haut a gauche

    perso = pygame.image.load('perso.png').convert_alpha() #importer une image avec transparence
    position = perso.get_rect()
    fenetre.blit(perso, position) #positionner l'image dans la fenetre -- 0,0 = coin en haut a gauche

    pygame.display.flip() #acctualiser/rafraichir la fenetre

    pygame.key.set_repeat(400,30)

    continuer = 1

    while continuer:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = 0

            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    position = position.move(0,5)
                if event.key == K_UP:
                    position = position.move(0,-5)
                if event.key == K_RIGHT:
                    position = position.move(5,0)
                if event.key == K_LEFT:
                    position = position.move(-5,0)

            # if event.type == MOUSEBUTTONDOWN and event.button == 1:
            #     position = event.pos
            # if event.type == MOUSEBUTTONDOWN and event.button == 3:
            #     print("NO")
            #
            # if event.type == MOUSEMOTION:
            #     position = event.pos

        fenetre.blit(fond, (0,0))
        fenetre.blit(perso, position)
        pygame.display.flip()

    # fenetre = pygame.display.set_mode((600,400))
    # fond = pygame.image.load('background.png').convert()
    # fenetre.blit(fond, (0,0))
    # perso = pygame.image.load('perso.png').convert_alpha()
    # position = perso.get_rect()
    # fenetre.blit(perso, position)
    # pygame.display.flip()
    # pygame.key.set_repeat(400,30)
    # continuer = 1
    # while continuer:
    #     for event in pygame.event.get():
    #         if event.type == QUIT:
    #             continuer = 0
    #         if event.type == KEYDOWN:
    #             if event.key == K_DOWN:
    #                 position = position.move(0,5)
    #             if event.key == K_UP:
    #                 position = position.move(0,-5)
    #             if event.key == K_RIGHT:
    #                 position = position.move(5,0)
    #             if event.key == K_LEFT:
    #                 position = position.move(-5,0)
    #     fenetre.blit(fond, (0,0))
    #     fenetre.blit(perso, position)
    #     pygame.display.flip()
menu = pygame_menu.Menu(400, 600, 'RPGPT',
                       theme=pygame_menu.themes.THEME_DARK)
menu.add_text_input('Name :', default='DOUZE')
menu.add_selector('Difficulty :', [('Hard', 1), ('Easy', 2), ('Normal', 3)], onchange=set_difficulty)
menu.add_button('Play', start)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)
