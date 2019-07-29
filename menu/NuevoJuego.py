import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from random import randint
from sys import exit
import sys
import time

tinicial=time.strftime("%H:%M:%S")
print ("Tiempo Inicial: " + tinicial)

pygame.init()
# Constantes
WIDTH = 1300
HEIGHT = 650
MposX1 =10
MposX2 =1100
 
 
puntaje1=0
puntaje2=0
total1=0
total2=0
blanco =(255,255,255)

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
 
def crear():
  archi=open('puntaje.txt','w')
  archi.close()

#funciones para crear y guardar archivos planos
def ptotal():
    global puntaje2,total1,puntaje1,total2
    total1=puntaje1
    total2=puntaje2
    archi=open('puntaje.txt','w')
    archi.write('Puntaje del Jugador1 : ')
    archi.write(str(total1)+'\n')
    archi.write('Puntaje del Jugador 2: ')
    archi.write(str(total2)+'\n')
    archi.close()

def tiempo():
    global tinicial, tfinal
    archi=open('puntaje.txt', 'a')
    archi.write('Tiempo Inicial: ')
    archi.write(tinicial+'\n')
    archi.write('Tiempo Final: ')
    archi.write(tfinal+'\n')
    archi.close()

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
        self.image = personaje = pygame.image.load("Personajes/goku.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(50, 300)
        self.muerto = 0
        self.sonidoDisparo= pygame.mixer.Sound("disparo.wav")#caraga del sonido del evento de disparo
        
    def update(self):
        teclas = pygame.key.get_pressed()
        #asignacion de teclas al personaje 1
        if teclas[K_f]:
            self.image = personaje = pygame.image.load("Personajes/gokukamehameha.png").convert_alpha()
            self.sonidoDisparo.play()#Ejecucion al momento de evento
            
        elif kamehameha.rect.x > 860:
            self.image = personaje = pygame.image.load("Personajes/goku.png").convert_alpha()

        if teclas[K_a]:
            self.image = personaje = pygame.image.load("Personajes/gokuleft.png").convert_alpha()
            if self.rect.x > 0:
                self.rect.x -= 10
        elif teclas[K_d]:
            self.image = personaje = pygame.image.load("Personajes/gokuright.png").convert_alpha()
            if self.rect.x < 740:
                self.rect.x += 10

        if teclas[K_w]:
            self.image = personaje = pygame.image.load("Personajes/gokuup.png").convert_alpha()
            if self.rect.y > 32:
                self.rect.y -= 10
        elif teclas[K_s]:
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
            if teclas[K_f]:
                self.rect.x = (personaje.rect.x + 60)
                self.rect.y = (personaje.rect.y + 14)
        if self.rect.x < 870:
            self.rect.x += 20

class Barravidagoku(Sprite):
    def __init__(self):
        self.image = barravidagoku = pygame.image.load("Personajes/barravidagoku.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(18, 4)
    def update(self):
        if barravidagoku.rect.x <= -152:
            personaje.muerto = 1
        if disparo.rect.y >= (personaje.rect.y - 36):
            if disparo.rect.y <= (personaje.rect.y + 62):
                if disparo.rect.x >= personaje.rect.x:
                    if disparo.rect.x <= (personaje.rect.x + 43):
                        barravidagoku.rect.x -= 26
                        disparo.rect.x = -400
        if minicell.rect.y >= (personaje.rect.y - 36):
            if minicell.rect.y <= (personaje.rect.y + 62):
                if minicell.rect.x >= personaje.rect.x:
                    if minicell.rect.x <= (personaje.rect.x + 43):
                        barravidagoku.rect.x -= 26
                        #disparo.rect.x = -400

class Minicell(Sprite):
    def __init__(self):
        self.image = minicell = pygame.image.load("Personajes/minicell.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(750, 300)
        self.bandera = 0
        self.muerto = 0
        self.sonidoDisparo2= pygame.mixer.Sound("disparo.wav")#caraga del sonido del evento de disparo
        
    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[K_j]:
            self.image = personaje = pygame.image.load("Personajes/minicell.png").convert_alpha()
            self.sonidoDisparo2.play()
            
        elif kamehameha.rect.x > 860:
            self.image = personaje = pygame.image.load("Personajes/minicell.png").convert_alpha()

        if teclas[K_LEFT]:
            self.image = personaje = pygame.image.load("Personajes/minicell.png").convert_alpha()
            if self.rect.x > 0:
                self.rect.x -= 10
        elif teclas[K_RIGHT]:
            self.image = personaje = pygame.image.load("Personajes/minicell.png").convert_alpha()
            if self.rect.x < 740:
                self.rect.x += 10

        if teclas[K_UP]:
            self.image = personaje = pygame.image.load("Personajes/minicell.png").convert_alpha()
            if self.rect.y > 32:
                self.rect.y -= 10
        elif teclas[K_DOWN]:
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
            if teclas[K_j]:#al presionar la tecla se ejecuta el evento
                self.rect.x = (minicell.rect.x - 60) #hacia donde avanza el disparo
                self.rect.y = (minicell.rect.y - 14)
        if self.rect.x > -400:
            self.rect.x -= 20

class Barravidaminicell(Sprite):
    def __init__(self):
        self.image = barravidaminicell = pygame.image.load("Personajes/barravidaminicell.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.move_ip(612, 4)
    def update(self):
        if self.rect.x >= 782:
            minicell.muerto = 1
        if kamehameha.rect.y >= minicell.rect.y:
            if kamehameha.rect.y <= (minicell.rect.y + 62):
                if kamehameha.rect.x >= minicell.rect.x:
                    if kamehameha.rect.x <= (minicell.rect.x + 43):
                        self.rect.x += 6
                        kamehameha.rect.x = 900

if __name__ == '__main__':
    # Variables.
    salir = False
    #musica
    pygame.mixer.music.set_volume(0.9) #Configuracion del Volumen
    pygame.mixer.music.load("fighter.mp3") #Carga de mp3 sonido de fondo
    pygame.mixer.music.play(100) #Numero de veces de reproduccion del sonido
    # Establezco la pantalla.
    screen = pygame.display.set_mode((800,600))

    # Establezco el título.
    pygame.display.set_caption("DBZ fighter")

    # Creo dos objetos surface.
    fondo = pygame.image.load("Personajes/namek.jpg").convert()
    cuadrovidagoku = pygame.image.load("Personajes/cuadrovidagoku.png").convert_alpha()
    cuadrovidaminicell = pygame.image.load("Personajes/cuadrovidaminicell.png").convert_alpha()
    hasperdido = pygame.image.load("Personajes/Hasperdido.png").convert()
    hasganado = pygame.image.load("Personajes/Hasganado.png").convert()
    # .convert() convierten la superficie a un formato de color que permite imprimirlas mucho mas rápido.

    # Objetos
    temporizador = pygame.time.Clock()
    personaje = Personaje()
    kamehameha = Kamehameha()
    minicell = Minicell()
    disparo = Disparo()
    barravidagoku = Barravidagoku()
    barravidaminicell = Barravidaminicell()

    # Movimiento del personaje.
    while not salir:
        personaje.update()
        kamehameha.update()
        minicell.update()
        disparo.update()

        if kamehameha.rect.y >= minicell.rect.y:
            if kamehameha.rect.y <= (minicell.rect.y + 62):
                if kamehameha.rect.x >= minicell.rect.x:
                   if kamehameha.rect.x <= (minicell.rect.x + 43):
                       barravidaminicell.rect.x += 26
                       kamehameha.rect.x = 900
                       puntaje1 += 15
                       ptotal1=puntaje1
                       
        #verifica si hay colision para sumar/restar puntaje
        if disparo.rect.y >= (personaje.rect.y - 56):
            if disparo.rect.y <= (personaje.rect.y + 62):
                if disparo.rect.x >= personaje.rect.x:
                    if disparo.rect.x <= (personaje.rect.x + 43):
                        barravidagoku.rect.x -= 26
                        disparo.rect.x = -400
                        puntaje2+= 15
                        ptotal2=puntaje2
                        


        #actualizacion de objetos
        barravidagoku.update()
        barravidaminicell.update()
        minicell.update()
        disparo.update()
        ptotal()



        # actualizacion grafica
        screen.blit(fondo, (0, 0))
        screen.blit(personaje.image, personaje.rect)
        screen.blit(kamehameha.image, kamehameha.rect)
        screen.blit(minicell.image, minicell.rect)
        screen.blit(disparo.image, disparo.rect)
        screen.blit(barravidagoku.image, barravidagoku.rect)
        screen.blit(barravidaminicell.image, barravidaminicell.rect)
        screen.blit(cuadrovidagoku, (0,0))
        screen.blit(cuadrovidaminicell, (608,0))
        screen.blit(pygame.font.SysFont("tahoma", 20).render("Puntacion 1: " + str(puntaje1), True, blanco), (0,40))
        screen.blit(pygame.font.SysFont("tahoma", 20).render("Puntacion 2: " + str(puntaje2), True, blanco), (600,40))


        if personaje.muerto == 1:
            screen.blit(hasperdido, (250,264))
        if minicell.muerto == 1:
            screen.blit(hasganado, (250,264))
        pygame.display.flip()

        if personaje.muerto == 1:
            pygame.time.delay(3000)
            salir = True
        elif minicell.muerto == 1:
            pygame.time.delay(3000)
            salir = True
        temporizador.tick(60)

        # gestion de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                    salir = True
                    pygame.quit() #detenemos todos los modulos
                    sys.exit()
tfinal=time.strftime("%H:%M:%S")
print("Tiempo Final: " + tfinal)
tiempo()