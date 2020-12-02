from PIL import Image

class Col:
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 255, 0)
    GREEN = (0, 0, 255)

def colorToInt(colorTuple):
    idDict = {
    Col.WHITE:0,
    Col.BLACK:1,
    Col.RED:2,
    Col.BLUE:3,
    Col.GREEN:4
    }

    try:
        tileID = idDict[colorTuple]
    except KeyError:
        tileID = -1
    return tileID

def imgToMat(dir):
    """
    dir donne l'arborescence de l'image à convertir
    palette est une liste de tuples qui donne une valeur à une couleur
    """
    im = Image.open(dir)
    wid, hei = im.size
    mat = [[0 for i in range(wid)] for i in range(hei)]
    for y in range(hei):
        for x in range(wid):
            mat[y][x] = colorToInt(im.getpixel((x, y)))
    return mat
