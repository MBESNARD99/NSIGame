"""
Programme réalisé par Besnard, Mathéo, 1G8
"""
import pygame

#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Jeu d'Aventure - BESNARD Mathéo")
font = pygame.font.Font('Symtext.ttf', 20)

welcome=pygame.image.load("welcome.jpg")
hall=pygame.image.load("hall.jpg")
salon=pygame.image.load("salon.jpg")
escalier=pygame.image.load("escalier.jpg")
cuisine=pygame.image.load("cuisine.jpg")
lingerie=pygame.image.load("lingerie.jpg")
jardin=pygame.image.load("jardin.jpg")
cabanon=pygame.image.load("cabanon.jpg")
etage=pygame.image.load("etage.jpg")
chambre=pygame.image.load("chambre.jpg")
bathroom=pygame.image.load("bathroom.jpg")
etage2=pygame.image.load("etage2.jpg")
grenier=pygame.image.load("grenier.jpg")

map_hall=pygame.image.load("map_hall.png")
map_hall=pygame.transform.scale(map_hall, (900, 500))
text_hall=font.render("Hall", True, (0, 0, 0))
text_hall=pygame.transform.scale(text_hall, (70, 50))


map_salon=pygame.image.load("map_salon.png")
map_salon=pygame.transform.scale(map_salon, (900, 500))
text_salon=font.render("Salon", True, (0, 0, 0))
text_salon=pygame.transform.scale(text_salon, (70, 50))

map_escalier=pygame.image.load("map_escalier.png")
map_escalier=pygame.transform.scale(map_escalier, (900, 500))
text_escalier=font.render("Escalier", True, (0, 0, 0))
text_escalier=pygame.transform.scale(text_escalier, (90, 50))

map_cuisine=pygame.image.load("map_cuisine.png")
map_cuisine=pygame.transform.scale(map_cuisine, (900, 500))
text_cuisine=font.render("Cuisine", True, (0, 0, 0))
text_cuisine=pygame.transform.scale(text_cuisine, (90, 50))

map_lingerie=pygame.image.load("map_lingerie.png")
map_lingerie=pygame.transform.scale(map_lingerie, (900, 500))
text_lingerie=font.render("Lingerie", True, (0, 0, 0))
text_lingerie=pygame.transform.scale(text_lingerie, (90, 50))

map_jardin=pygame.image.load("map_jardin.png")
map_jardin=pygame.transform.scale(map_jardin, (900, 500))
text_jardin=font.render("Jardin", True, (0, 0, 0))
text_jardin=pygame.transform.scale(text_jardin, (90, 50))

map_cabanon=pygame.image.load("map_cabanon.png")
map_cabanon=pygame.transform.scale(map_cabanon, (900, 500))
text_cabanon=font.render("Cabanon", True, (0, 0, 0))
text_cabanon=pygame.transform.scale(text_cabanon, (90, 50))
text_newzone=font.render("Nouvelle zone découverte !", True, (255, 255, 255))
text_newzone=pygame.transform.scale(text_newzone, (800, 75))
text_key=font.render("Vous avez trouvé une clée dans le cabanon", True, (255, 0, 0))
text_key=pygame.transform.scale(text_key, (600, 50))

mapetage_etage=pygame.image.load("mapetage_etage.png")
mapetage_etage=pygame.transform.scale(mapetage_etage, (900, 500))
text_etage=font.render("Etage", True, (0, 0, 0))
text_etage=pygame.transform.scale(text_etage, (90, 50))

mapetage_chambre=pygame.image.load("mapetage_chambre.png")
mapetage_chambre=pygame.transform.scale(mapetage_chambre, (900, 500))
text_chambre=font.render("Chambre", True, (0, 0, 0))
text_chambre=pygame.transform.scale(text_chambre, (90, 50))

mapetage_bathroom=pygame.image.load("mapetage_bathroom.png")
mapetage_bathroom=pygame.transform.scale(mapetage_bathroom, (900, 500))
text_bathroom=font.render("Salle de Bain", True, (0, 0, 0))
text_bathroom=pygame.transform.scale(text_bathroom, (130, 50))

mapetage_etage2=pygame.image.load("mapetage_etage2.png")
mapetage_etage2=pygame.transform.scale(mapetage_etage2, (900, 500))
text_etage2=font.render("Etage", True, (0, 0, 0))
text_etage2=pygame.transform.scale(text_etage2, (90, 50))
text_notkey=font.render("Vous n'avez pas de clée !", True, (255, 0, 0))
text_notkey=pygame.transform.scale(text_notkey, (400, 50))

help=pygame.image.load("help.png")
help_rect = help.get_rect()
help_rect.x = 1010
help_rect.y = 650
help=pygame.transform.scale(help, (75, 75))

texthelp=font.render("Allez voir plus loin dans le jardin !", True, (0, 0, 0))
texthelp=pygame.transform.scale(texthelp, (400, 50))

key=pygame.image.load("clé.png")
key_rect = key.get_rect()
key_rect.x = 0
key_rect.y = 0
key=pygame.transform.scale(key, (75, 75))

newzone = 1
keyfind = 1
clickedhelp = 1
dansQuellePierceEstLePersonnage = "welcome"


def decrireLaPiece(piece):
    global keyfind
    global newzone
    global clickedhelp
    if piece=="welcome":
        fenetre.blit(welcome,(0,0))
    elif piece=="hall":
        fenetre.blit(hall,(0,0))
        fenetre.blit(map_hall,(475,-210))
        fenetre.blit(text_hall, (842, 108))
        if keyfind==2:
            fenetre.blit(key, key_rect)
    elif piece=="salon":
        fenetre.blit(salon,(0,0))
        fenetre.blit(map_salon, (475, -210))
        fenetre.blit(text_salon, (842, 108))
        if keyfind==2:
            fenetre.blit(key, key_rect)
    elif piece=="escalier":
        fenetre.blit(escalier,(0,0))
        fenetre.blit(map_escalier, (475, -210))
        fenetre.blit(text_escalier, (835, 108))
        if keyfind==2:
            fenetre.blit(key, key_rect)
    elif piece=="cuisine":
        fenetre.blit(cuisine,(0,0))
        fenetre.blit(map_cuisine, (475, -210))
        fenetre.blit(text_cuisine, (835, 108))
        if keyfind==2:
            fenetre.blit(key, key_rect)
    elif piece=="lingerie":
        fenetre.blit(lingerie,(0,0))
        fenetre.blit(map_lingerie, (475, -210))
        fenetre.blit(text_lingerie, (835, 108))
        if keyfind==2:
            fenetre.blit(key, key_rect)
    elif piece=="jardin":
        fenetre.blit(jardin,(0,0))
        fenetre.blit(map_jardin, (475, -210))
        fenetre.blit(text_jardin, (835, 108))
        if keyfind==2:
            fenetre.blit(key, key_rect)
    elif piece=="cabanon":
        fenetre.blit(cabanon,(0,0))
        fenetre.blit(map_cabanon, (390, -210))
        fenetre.blit(text_cabanon, (790, 108))
        if newzone==2:
            fenetre.blit(text_key, (250, 590))
            fenetre.blit(text_newzone, (170, 630))
        fenetre.blit(key, key_rect)
        keyfind=2
        clickedhelp=clickedhelp+1
    elif piece=="etage":
        fenetre.blit(etage,(0,0))
        fenetre.blit(mapetage_etage, (450, -160))
        fenetre.blit(text_etage, (855, 135))
        if keyfind==2:
            fenetre.blit(key, key_rect)
    elif piece=="chambre":
        fenetre.blit(chambre,(0,0))
        fenetre.blit(mapetage_chambre, (450, -160))
        fenetre.blit(text_chambre, (870, 135))
        if keyfind==2:
            fenetre.blit(key, key_rect)
    elif piece=="bathroom":
        fenetre.blit(bathroom,(0,0))
        fenetre.blit(mapetage_bathroom, (450, -160))
        fenetre.blit(text_bathroom, (855, 135))
        if keyfind==2:
            fenetre.blit(key, key_rect)
    elif piece=="etage2":
        fenetre.blit(etage2,(0,0))
        fenetre.blit(mapetage_etage2, (450, -160))
        fenetre.blit(text_etage2, (855, 135))
        if keyfind==2:
            fenetre.blit(key, key_rect)
        else:
            fenetre.blit(text_notkey, (15,10))
            fenetre.blit(help, help_rect)
        if clickedhelp==2:
            fenetre.blit(texthelp, (610, 660))
        if clickedhelp > 2:
            fenetre.blit(texthelp, (5000, 5000))
    elif piece=="grenier":
        fenetre.blit(grenier,(0,0))
        keyfind=1

def decision(direction,piece):
    global newzone
    memorisePiece=piece

    if event.key == pygame.K_SPACE:
        if piece == "welcome":
            piece = "hall"

    if direction=='z':
        if piece=="etage2":
            if keyfind==2:
               piece="grenier"
            else:
                print("Tu n'as pas la clé requise !")

        if piece=="etage":
            piece="chambre"

        if piece=="hall":
            piece="salon"

        if piece=="escalier":
            piece="cuisine"

    if direction=='s':
        if piece=="salon":
            piece="hall"

        if piece=="cuisine":
            piece="escalier"

        if piece=="etage":
            piece="escalier"

        if piece=="chambre":
            piece="etage"

    if direction=='d':
        if piece=="etage":
            piece="bathroom"

        if piece=="escalier":
            piece="etage"

        if piece=="jardin":
            piece="cabanon"
            newzone = newzone + 1

        if piece=="lingerie":
            piece="jardin"

        if piece=="hall":
            piece="escalier"

        if piece=="cuisine":
            piece="lingerie"

        if piece=="salon":
            piece="cuisine"

        if piece=="etage2":
            piece="etage"

    if direction=='q':
        if piece=="etage":
            piece="etage2"

        if piece=="escalier":
            piece="hall"

        if piece=="cuisine":
            piece="salon"

        if piece=="lingerie":
            piece="cuisine"

        if piece=="jardin":
            piece="lingerie"

        if piece=="cabanon":
            piece="jardin"

        if piece=="bathroom":
            piece="etage"

    if memorisePiece==piece:
        print("Tu ne peux pas !")
    print("Vous êtes actuellement dans le/la", piece)
    return piece

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False            #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN:  #lecture du clavier
            dansQuellePierceEstLePersonnage=decision(event.unicode,dansQuellePierceEstLePersonnage)
            if event.key == pygame.K_ESCAPE:
                loop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if help_rect.collidepoint(event.pos):
                clickedhelp = clickedhelp+1

    decrireLaPiece(dansQuellePierceEstLePersonnage)
    # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()