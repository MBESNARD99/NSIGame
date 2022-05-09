"""
Programme affichage
"""
import pygame

#constantes de la fenêtre d'affichage
HAUTEUR=500
LARGEUR=500      #largeur de la fenêtre
ROUGE=(255,0,0)     # définition de 3 couleurs
VERT=(0,255,0)
BLEU=(0,0,255)

#Utilisation de la bibliothèque pygame
pygame.init()
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("PONGGGGGGGGGGGGGGGGGGGGGGGGGGGG")             #titre de la fenêtre
font = pygame.font.Font('freesansbold.ttf', 20)     #choix de la police de caractères
frequence = pygame.time.Clock()                     #mode animation dans pygame

#variables de gestion de la balle
RAYONBALLE=25
balleX=LARGEUR//2
balleY=HAUTEUR//2          #position x y de la balle au milieu dans la fenêtre
vecteurBalleX=5            #vecteur de déplacement
vecteurBalleY=4

rectangleBleuY=HAUTEUR//2
vecteurBleuY=3
rectangleRougeY=HAUTEUR//2
vecteurRougeY=3


def afficheRectangleBleu(x,y,largeur,hauteur):
    """
    affiche un rectangle en position x,y avec une largeur et une hauteur
    """
    pygame.draw.rect(fenetre, BLEU, [x, y, largeur, hauteur])





def afficheRectangleRouge(x,y,largeur,hauteur):
    """
    affiche un rectangle en position x,y avec une largeur et une hauteur
    """
    pygame.draw.rect(fenetre, ROUGE, [x, y, largeur, hauteur])






def afficheBalle():
    """
    affiche un cercle aux coordonnées x,y avec un rayon
    """
    pygame.draw.circle(fenetre, VERT, (balleX,balleY), RAYONBALLE)

def deplacementBalle():
    """
    deplace la balle
    """
    global balleX,balleY        #permet de modifier les variables balleX,balleY
    balleX=balleX+vecteurBalleX #on deplace la balle selon l'axeX
    balleY=balleY+vecteurBalleY

def deplacementRectangleBleu():

    global rectangleBleuY

    rectangleBleuY = rectangleBleuY + vecteurBleuY

def deplacementRectangleRouge():

    global rectangleRougeY

    rectangleRougeY = rectangleRougeY + vecteurRougeY

def testCollisionMurs():
    """
    test les collisions avec les murs
    """
    global vecteurBalleX,vecteurBalleY,vecteurBleuY,rectangleBleuY,vecteurRougeY,rectangleRougeY
    if balleX+RAYONBALLE>LARGEUR:
        vecteurBalleX=vecteurBalleX*-1
    if balleX-RAYONBALLE<0:
        vecteurBalleX=vecteurBalleX*-1
    if balleY+RAYONBALLE>HAUTEUR:
        vecteurBalleY=vecteurBalleY*-1
    if balleY-RAYONBALLE<0:
        vecteurBalleY=vecteurBalleY*-1

    if rectangleBleuY+80>HAUTEUR:
        vecteurBleuY=vecteurBleuY*0-1
    if rectangleBleuY<0:
        vecteurBleuY=vecteurBleuY*0+1

    if rectangleRougeY+80>HAUTEUR:
        vecteurRougeY=vecteurRougeY*0-1
    if rectangleRougeY<0:
        vecteurRougeY=vecteurRougeY*0+1


loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenêtre (croix rouge)
        if event.type == pygame.KEYDOWN:  #une touche a été pressée...laquelle ?
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False

    keys = pygame.key.get_pressed()         #recupération des touches appuyées en continu
    if keys[pygame.K_UP]:    #est-ce la touche UP
        vecteurBleuY=-3
    elif keys[pygame.K_DOWN]:  #est-ce la touche DOWN
        vecteurBleuY=3
    else:
        vecteurBleuY=0
    if keys[pygame.K_w]:    #est-ce la touche UP
        vecteurRougeY=-3
    elif keys[pygame.K_s]:  #est-ce la touche DOWN
        vecteurRougeY=3
    else:
        vecteurRougeY=0

    fenetre.fill((0,0,0))   #efface la fenêtre
    afficheBalle()
    deplacementBalle()
    testCollisionMurs()
    afficheRectangleBleu(20,rectangleBleuY,10,80)
    deplacementRectangleBleu()
    afficheRectangleRouge(480,rectangleRougeY,10,80)
    deplacementRectangleRouge()
    frequence.tick(60)
    pygame.display.update() #mets à jour la fenêtre graphique
pygame.quit()



