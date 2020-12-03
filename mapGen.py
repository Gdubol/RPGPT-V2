import pygame
import vars
from PIL import Image

def loadFromImg(dir, idDict):
    """
    Entrée :    emplacement de l'image
                dictionnaire des ID
    Sortie :    matrice des tiles\id à afficher
                liste des rect (collisions)
    """
    im = Image.open(dir)
    wid, hei = im.width, im.height
    tileMap = [[None for i in range(wid)] for i in range(hei)]
    collideMap = []

    for xPix in range(wid):
        for yPix in range(hei):
            pix = im.getpixel((yPix, xPix))
            id, collision = idDict.get(pix)
            if collision:
                pos = (xPix*vars.TILESIZE,yPix*vars.TILESIZE)
                size = (vars.TILESIZE, vars.TILESIZE)
                collideMap.append(pygame.Rect(pos, size))
            tileMap[xPix][yPix] = id
    return tileMap, collideMap

def loadMap(screen, tileMap, imgDict):
    """
    Entrée :    écran pygame sur lequel on blit
                matrice des tiles\id à afficher
                dictionnaire faisant le lien entre ID et images à afficher
    Sortie :    Rien
    """
    for x in range(len(tileMap)):
        for y in range(len(tileMap[0])):
            pos = (y*vars.TILESIZE,x*vars.TILESIZE)
            imgDir = imgDict.get(tileMap[x][y])
            tileImg = pygame.image.load(imgDir).convert()
            # tileImg = pygame.transform.scale(tileImg, (4, 4))
            screen.blit(tileImg, pos)
    return None

def disp(mat):
    """
    Fonction de test, purement esthéPUTE et inutile pour le jeu en soit
    """
    for line in mat:
        for elt in line:
            print(str(elt)+" ", end = "")
        print("\n", end = "")
    return None
