# Módulos
import sys, pygame
from pygame.locals import *
 
 
# Constantes
WIDTH = 1300
HEIGHT = 650
MposX1 =10
 
 
cont=6
direc=True
i=0
p1={}#xinicial y xfinal
Rp1={}
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
#================================================================
 
#======================TECLADO===================================
#================================================================
def teclado1():
    teclado1 = pygame.key.get_pressed()
     
    global MposX1
    global cont, direc
   
       
    if teclado1[K_d]:
        MposX1+=2
        cont+=1
        direc=True
    elif teclado1[K_a]:
        MposX1-=2
        cont+=1
        direc=False
    elif teclado1[K_q]:
        #SALTO
        MposX1-=2
    #else :
         #cont=6
       
    return
   
 
#===================SPRITE===============================
#========================================================
def sprite1():
 
    global cont
 
    p1[0]=(0,0,161,300)
    p1[1]=(161,0,135,300)
    p1[2]=(296,0,137,300)
    p1[3]=(433,0,146,300)
    p1[4]=(585,0,155,300)
    p1[5]=(734,0,135,300)
   
    Rp1[0]=(719,0,161,300)
    Rp1[1]=(565,0,140,300)
    Rp1[2]=(425,0,155,300)
    Rp1[3]=(275,0,155,300)
    Rp1[4]=(130,0,155,300)
    Rp1[5]=(0,0,149,300)
   
    p=6
   
    global i
       
    if cont==p:
        i=0
   
    if cont==p*2:
        i=1
   
    if cont==p*3:
        i=2
   
    if cont==p*4:
        i=3
   
    if cont==p*5:
        i=4
   
    if cont==p*6:
       i=5
       cont=0
   
    return
 
 
 
 
 
def main():
    pygame.init()    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Killer Instinct")
   
 
    fondo = imagen("fondo.png")
   
         
    personaje1 = imagen("combo.png",True)  
    personaje1_inv=pygame.transform.flip(personaje1,True,False);
     
    clock = pygame.time.Clock()
   
     
 
    # el bucle principal del juego
    while True:
       
        time = clock.tick(60)
       
        sprite1()
        teclado1()
       
       
   
        fondo = pygame.transform.scale(fondo, (1300, 650))
             
        screen.blit(fondo, (0, 0))
       
        if direc==True:
            screen.blit(personaje1, ( MposX1, 350),(p1[i]))
   
        if direc==False:
            screen.blit(personaje1_inv, ( MposX1, 350),(Rp1[i]))
   
        pygame.display.flip()
       
       
       
       
        # Cerrar la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
   
    return 0
 
 
 
 
if __name__ == '__main__':
    main()
