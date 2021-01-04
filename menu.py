import pygame
import pygame_menu
from pygame.locals import*
import pygame_menu.events as _events
import pygame_menu.widgets as _widgets

#============================================================================================================================================#
#================================================================ Les Variables =============================================================#

Mytheme = pygame_menu.themes.Theme( background_color = (0,0,0,0),
                                    title_shadow = True,
                                    title_background_color = (74,101,127),
                                    title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_TITLE_ONLY_DIAGONAL,
                                    widget_font = pygame_menu.font.FONT_MUNRO,
                                    widget_font_size = 40,
                                    cursor_color = (135,73,187),
                                    title_font =  pygame_menu.font.FONT_MUNRO,
                                    title_font_color = (147,87,5),
                                    title_font_size = 50)

X = 1280
Y = 720
FPS = 60
skin = 1
perso_name = 'THE DOUZEUR'
game_value = 0

ctrl_forward = 'z'
ctrl_backward = 's'
ctrl_left = 'q'
ctrl_right = 'd'
touche_en_cours = ''


capacity_point = 12
stat_force = 12
stat_speed = 12
stat_magie = 12
stat_esqve = 12
stat_douze = 12

#============================================================================================================================================#
#================================ Utilisation d'un .txt pour stockage de valeur =============================================================#

# def getParam(param, file):
#     f = open("{0}.txt".format(file), "r")
#     x = f.readlines()
#     f.close()
#     for i in range(len(x)):
#         x[i] = x[i].strip("\n").split(":")
#     value = None
#     for cfgParam, cfgVal in x:
#         if cfgParam == param:
#             value = cfgVal
#     return value
#
# def setParam(param, value, file):
#     f = open("{0}.txt".format(file), "r")
#     x = f.readlines()
#     for i in range(len(x)):
#         x[i] = x[i].strip("\n").split(":")
#     f = open("{0}.txt".format(file), "w")
#     for cfgParam, cfgVal in x:
#         if cfgParam != param:
#             f.write("{0}:{1}\n".format(cfgParam, cfgVal))
#         else:
#             f.write("{0}:{1}\n".format(param, value))
#             print("[LOG] Changed {0} from {1} to {2}".format(param, cfgVal, value))
#     return None
# print(getParam("cx", "test"))
# setParam("cx", "pute", "test")
# print(getParam("cx", "test"))


#============================================================================================================================================#
#======================================================= Menu Parametre / Option =============================================================#
"""
    Variables en Global :
        FPS : défini la vitesse d'affichage (int)
        X : affichage en largeur de la fenetre (int)
        Y : affichage en hauteur de la fenetre (int)
        menu_option : menu servant pour les option (pygame_menu.Menu())
        surface : surface d'affichage pour le menu (pygame.display.set_mode())
"""
def touche_action(touche):
    global fonction_touche, ctrl_forward, ctrl_backward, ctrl_left, ctrl_right, touche_en_cours
    touche_en_cours = touche
    if fonction_touche == 'FORWARD' :
        ctrl_forward = touche
        change_touche('FORWARD')
    if fonction_touche == 'BACKWARD' :
        ctrl_backward = touche
        change_touche('BACKWARD')
    if fonction_touche == 'LEFT' :
        ctrl_left = touche
        change_touche('LEFT')
    if fonction_touche == 'RIGHT' :
        ctrl_right = touche
        change_touche('RIGHT')

def change_touche(fonction):
    global fonction_touche, ctrl_forward, ctrl_backward, ctrl_left, ctrl_right
    fonction_touche = fonction
    menu_controle.clear()
    menu_controle.add_text_input(fonction+' :   ', default = touche_en_cours, onchange = touche_action, maxchar = 2)
    menu_controle.add_button('Save And Apply', controle)
    menu_controle.mainloop(surface)

def controle():
    global menu_controle
    menu.disable
    surface_controle = pygame.display.set_mode((X,Y))
    menu_controle = pygame_menu.Menu(Y,X, 'RPGPT', theme = Mytheme)
    menu_controle.add_button('FORWARD : '+ctrl_forward, change_touche, 'FORWARD').set_margin(0,10) #prévoir d'ajouter la possibilité de voir la touche en question qui est mise sur chaque fonction avec ### +getParam("FORWARD", "controle.txt") ###
    menu_controle.add_button('BACKWARD : '+ctrl_backward, change_touche, 'BACKWARD' ).set_margin(10,10)
    menu_controle.add_button('LEFT : '+ctrl_left, change_touche, 'LEFT' )
    menu_controle.add_button('RIGHT : '+ctrl_right, change_touche, 'RIGHT' )
    menu_controle.add_button('Save Return Menu', option)
    menu_controle.mainloop(surface)

def set_fps(value, fps):

    global FPS

    name, index = value
    print('Change fps to :'+name)
    FPS = fps

def para_graphique():
    menu.disable
    menu_graphique = pygame_menu.Menu(Y,X,'RPGPT', theme = Mytheme)
    menu_graphique.add_selector('FPS :', [('60fps',(60)),('30fps',(30))], onchange = set_fps)
    menu_graphique.add_button('Save and Apply', option)
    menu_graphique.mainloop(surface)

def set_resolution(value, resolution):

    global X,Y

    name, index = value
    print('Change résolution to :' + name)
    X = resolution[0]
    Y = resolution[1]

def para_affichage():
    menu.disable
    menu_affichage = pygame_menu.Menu(Y,X, 'RPGPT', theme = Mytheme)
    menu_affichage.add_selector('Affichage :', [('720 x 480',(720,480)),('720 x 576',(720,576)),('1280 x 720',(1280,720)),
                                            ('1280 x 1024',(1280,1024)),('1920 x 1080',(1920,1080))],default = 2, onchange = set_resolution)
    menu_affichage.add_button('Save and Apply', option)
    menu_affichage.mainloop(surface)

def option():

    global menu_option, surface

    menu.disable #désactive le premier menu
    surface = pygame.display.set_mode((X, Y))
    menu_option = pygame_menu.Menu(Y,X, 'RPGPT', theme = Mytheme) #active le menu des options
    menu_option.add_button('Affichage', para_affichage)
    menu_option.add_button('Graphisme', para_graphique)
    menu_option.add_button('Controle', controle)
    menu_option.add_vertical_margin(100)
    menu_option.add_button('Save Return Menu',  menu_principal)
    menu_option.mainloop(surface)

#=========================================================================================================================================================================================#
#=============================================================================== START A NEW GAME ========================================================================================#
#=========================================================================================================================================================================================#
#=========================================================================================================================================================================================#
"""
    Variables en Global :
        skin : le skin de personnage choisi (int)
        game_difficulty : difficulté du jeu (int)
        name_difficulty : nom de la difficulté du jeu (str)
        game_value : pour garder l'affiche dans le selecteur de difficulté (int)
        perso_name : non du perso donné par le joueur (str)
        menu_debut : le menu de début de jeu, aussi utilisé pour le lancement d'une nouvelle partie (pygame_menu.Menu())
        stat_force :
        stat_speed :
        stat_magie :
        stat_esqve :
        stat_douze :
        capacity_point :
"""

def dim_point(arg):
    """
    fonction de retire point de capacité
    à voir si on la laisse au début car on peut faire en sorte de pas dépasser un seuil de valeur trop basse dès le début
    style on peut pas passer en dessous de 5 pour une capacité
    à voir
    """
    global capacity_point, stat_force, stat_speed, stat_magie, stat_esqve, stat_douze

    if arg == 'stat_force' :
        if stat_force > 0 :
            stat_force -= 1
            capacity_point += 1
            set_capacity()
    if arg == 'stat_speed' :
        if stat_speed > 0 :
            stat_speed -= 1
            capacity_point += 1
            set_capacity()
    if arg == 'stat_magie' :
        if stat_magie > 0 :
            stat_magie -= 1
            capacity_point += 1
            set_capacity()
    if arg == 'stat_esqve' :
        if stat_esqve > 0 :
            stat_esqve -= 1
            capacity_point += 1
            set_capacity()
    if arg == 'stat_douze' :
        if stat_douze > 0 :
            stat_douze -= 1
            capacity_point += 1
            set_capacity()
    set_capacity()


def aug_point(arg): #fonction d'augmente point de capacité
    """
    Oui on peut augmenter les stats à l'infinie
    """

    global capacity_point, stat_force, stat_speed, stat_magie, stat_esqve, stat_douze

    if capacity_point > 0 :
        if arg == 'stat_force' :
            stat_force += 1
            capacity_point -= 1
            set_capacity()
        if arg == 'stat_speed' :
            stat_speed += 1
            capacity_point -= 1
            set_capacity()
        if arg == 'stat_magie' :
            stat_magie += 1
            capacity_point -= 1
            set_capacity()
        if arg == 'stat_esqve' :
            stat_esqve += 1
            capacity_point -= 1
            set_capacity()
        if arg == 'stat_douze' :
            stat_douze += 1
            capacity_point -= 1
            set_capacity()
    set_capacity()

def set_capacity(): #reprint le menu des stats avec la modif de stat effectuées
    menu_stat.clear()
    menu_stat.add_label('')
    menu_stat.add_button('-', dim_point, 'stat_force')
    menu_stat.add_button('-', dim_point, 'stat_speed')
    menu_stat.add_button('-', dim_point, 'stat_magie')
    menu_stat.add_button('-', dim_point, 'stat_esqve')
    menu_stat.add_button('-', dim_point, 'stat_douze')
    menu_stat.add_label('Point restant : '+str(capacity_point))
    menu_stat.add_label('Force : '+str(stat_force))
    menu_stat.add_label('Speed : '+str(stat_speed))
    menu_stat.add_label('Magie : '+str(stat_magie))
    menu_stat.add_label('Esqve : '+str(stat_esqve))
    menu_stat.add_label('Douze : '+str(stat_douze))
    menu_stat.add_label('')
    menu_stat.add_button('+', aug_point, 'stat_force')
    menu_stat.add_button('+', aug_point, 'stat_speed')
    menu_stat.add_button('+', aug_point, 'stat_magie')
    menu_stat.add_button('+', aug_point, 'stat_esqve')
    menu_stat.add_button('+', aug_point, 'stat_douze')
    menu_stat.mainloop(surface)

def stat_menu(): #print une première fois le menu de stat, pour pouvoir ensuite faire les modifications de stats. Renvoie dans la fonction set_capacity()

    global menu_stat
    """
    menu_stat : (3 colonnes / 6 lignes) menu de start pour la mise en place des stats souhaitées
    """

    menu.disable
    menu_stat = pygame_menu.Menu(Y,X,'RPGPT', theme = Mytheme, columns = 3, rows = 6)

    menu_stat.add_label('')
    menu_stat.add_button('-', dim_point, 'stat_force')
    menu_stat.add_button('-', dim_point, 'stat_speed')
    menu_stat.add_button('-', dim_point, 'stat_magie')
    menu_stat.add_button('-', dim_point, 'stat_esqve')
    menu_stat.add_button('-', dim_point, 'stat_douze')
    menu_stat.add_label('Point restant : '+str(capacity_point))
    menu_stat.add_label('Force : '+str(stat_force))
    menu_stat.add_label('Speed : '+str(stat_speed))
    menu_stat.add_label('Magie : '+str(stat_magie))
    menu_stat.add_label('Esqve : '+str(stat_esqve))
    menu_stat.add_label('Douze : '+str(stat_douze))
    menu_stat.add_label('')
    menu_stat.add_button('+', aug_point, 'stat_force')
    menu_stat.add_button('+', aug_point, 'stat_speed')
    menu_stat.add_button('+', aug_point, 'stat_magie')
    menu_stat.add_button('+', aug_point, 'stat_esqve')
    menu_stat.add_button('+', aug_point, 'stat_douze')

    menu_stat.mainloop(surface)


def set_personnage(value, perso):

    global skin

    name, index = value
    skin = perso


def set_difficulty(value, difficulty):

    global game_difficulty, name_difficulty, game_value

    name_difficulty, game_value = value
    game_difficulty = difficulty
    print(game_difficulty)
    print(name_difficulty)

def set_name(name):

    global perso_name

    perso_name = name
    print(perso_name)

def change_personnage():
    menu_debut.clear()
    menu_debut.add_text_input('Name :', default=perso_name, onchange=set_name)
    menu_debut.add_vertical_margin(20)
    menu_debut.add_selector('Difficulty :', [('Hard', 3), ('Normal', 2), ('Easy', 1)], default = game_value, onchange=set_difficulty)
    menu_debut.add_vertical_margin(20)
    menu_debut.add_selector('Personnage :', [('Perso 1', 1), ('Perso 2', 2), ('Perso 3', 3)], default = skin-1, onchange=set_personnage)
    menu_debut.add_button('Apply', change_personnage)
    menu_debut.add_image('.\\ressources\\perso'+str(skin)+'.png', scale = (5,5))
    menu_debut.add_button('Continue', stat_menu)
    menu_debut.mainloop(surface)

def start():
    """
    Fonction pour lancer une première partie
    Utilise **  change_personnage()  **
    Utilise **  set_personnage()     **
    Utilise **  set_difficulty()     **
    Utilise **  set_name()           **
    Utilise la variable ** skin **
    Utilise les variables ** X ; Y **
    """

    global menu_debut

    menu.disable
    menu_debut = pygame_menu.Menu(Y,X,'RPGPT', theme = Mytheme, columns = 2, rows = 6)
    menu_debut.add_text_input('Name :', default='THE DOUZEUR', onchange=set_name)
    menu_debut.add_vertical_margin(20)
    menu_debut.add_selector('Difficulty :', [('Hard', 3), ('Normal', 2), ('Easy', 1)], onchange=set_difficulty)
    menu_debut.add_vertical_margin(20)
    menu_debut.add_selector('Personnage :', [('Perso 1', 1), ('Perso 2', 2), ('Perso 3', 3)], default = 0, onchange=set_personnage)
    menu_debut.add_button('Apply', change_personnage)
    menu_debut.add_image('.\\ressources\\perso'+str(skin)+'.png', scale = (5,5))
    menu_debut.mainloop(surface)

    # pygame_menu.events.EXIT #on ferme tout le bordel du pygame_menu
    # import jeu_jeu #import pour utiliser la fonction après
    # exec(open("jeu_jeu.py").read()) #ouverture du fichier
    # mainloop(fenetre,position) #on ouvre la fonction pour les déplacements de jeu_jeu.py ##ça marche pas en faite

#============================================================================================================================================#
#=============================================================== MENU PRINCIPAL =============================================================#
"""
    Fonction du Menu d'arrivé dans le jeu
    Renvoie au Menu start
    Renvoie au Menu Option
    Utilise les variables ** X ; Y ; Mytheme ; surface ; menu **
"""

def menu_principal():

    global menu, surface

    pygame.init()
    surface = pygame.display.set_mode((X, Y))
    menu = pygame_menu.Menu(Y, X, 'RPGPT', theme = Mytheme)
    menu.add_button('Play', start)
    menu.add_button('Option', option)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)

#============================================================================================================================================#
#============================================================= Lancement du Jeu =============================================================#
menu_principal()
