import pygame
from pygame.locals import *
from pygame.sprite import Sprite

# Constantes
WIDTH = 1300
HEIGHT = 650
MposX1 =10
MposX2 =1100
 
 
cont=6
cont2=6
direc=True
i=0
j=0
k=0
p1={}#xinicial y xfinal
Rp1={}
gp1={}
p2={}
Rp2={}
#===========================================================
#=================IMAGEN====================================
 
def imagen(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error.message:
                raise SystemExit.message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

class Personaje(Sprite):
    def __init__(self):
        self.image = personaje = pygame.image.load("Personajes/combo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(50, 300)
        self.muerto = 0
    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_SPACE]:
            self.image = personaje = pygame.image.load("Personajes/gokukamehameha.png").convert_alpha()
        elif kamehameha.rect.x > 860:
            self.image = personaje = pygame.image.load("Personajes/goku.png").convert_alpha()

        if teclas[K_LEFT]:
            self.image = personaje = pygame.image.load("Personajes/gokuleft.png").convert_alpha()
            if self.rect.x > 0:
                self.rect.x -= 10
        elif teclas[K_RIGHT]:
            self.image = personaje = pygame.image.load("Personajes/gokuright.png").convert_alpha()
            if self.rect.x < 740:
                self.rect.x += 10

        if teclas[K_UP]:
            self.image = personaje = pygame.image.load("Personajes/gokuup.png").convert_alpha()
            if self.rect.y > 32:
                self.rect.y -= 10
        elif teclas[K_DOWN]:
            if self.rect.y < 530:
                self.image = personaje = pygame.image.load("Personajes/gokudown.png").convert_alpha()
                self.rect.y += 10

class Kamehameha(Sprite):
    def __init__(self):
        self.image = kamehameha = pygame.image.load("Personajes/kamehameha.gif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(900, 700)
    def update(self):
        teclas = pygame.key.get_pressed()
        if self.rect.x > 840:
            if teclas[K_SPACE]:
                self.rect.x = (personaje.rect.x + 60)
                self.rect.y = (personaje.rect.y + 14)
        if self.rect.x < 870:
            self.rect.x += 20

class Minicell(Sprite):
    def __init__(self):
        self.image = minicell = pygame.image.load("Personajes/minicell.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(750, 300)
        self.bandera = 0
        self.muerto = 0
    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_e]:
            self.image = personaje = pygame.image.load("Personajes/disparominicell.png").convert_alpha()
        elif kamehameha.rect.x > 860:
            self.image = personaje = pygame.image.load("Personajes/minicell.png").convert_alpha()

        if teclas[K_a]:
            self.image = personaje = pygame.image.load("Personajes/minicell.png").convert_alpha()
            if self.rect.x > 0:
                self.rect.x -= 10
        elif teclas[K_d]:
            self.image = personaje = pygame.image.load("Personajes/minicell.png").convert_alpha()
            if self.rect.x < 740:
                self.rect.x += 10

        if teclas[K_w]:
            self.image = personaje = pygame.image.load("Personajes/minicell.png").convert_alpha()
            if self.rect.y > 32:
                self.rect.y -= 10
        elif teclas[K_s]:
            if self.rect.y < 530:
                self.image = personaje = pygame.image.load("Personajes/minicell.png").convert_alpha()
                self.rect.y += 10

class Disparo(Sprite):
    def __init__(self):
        self.image = barravidagoku = pygame.image.load("Personajes/disparominicell.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(-400, -400)
    def update(self):
        teclas = pygame.key.get_pressed()
        if self.rect.x == -400:
            if teclas[K_e]:
                self.rect.x = (minicell.rect.x - 60)
                self.rect.y = (minicell.rect.y - 14)
        if self.rect.x > -400:
            self.rect.x -= 20