# Módulos
import sys, pygame
from pygame.locals import *
 
 
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
    elif teclado1[K_f]:
        MposX1+=5
    #else :
         #cont=6
       
    return

def teclado2():
    teclado2 = pygame.key.get_pressed()
     
    global MposX2
    global cont2, direc
   
       
    if teclado2[K_RIGHT]:
        MposX2+=2
        cont2+=1
        direc=False
    elif teclado2[K_LEFT]:
        MposX2-=2
        cont2+=1
        direc=True
    elif teclado2[K_UP]:
        #SALTO
        MposX2-=2
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

    '''gp1[0]=(0,0,161,300)
    gp1[1]=(161,0,175,300)
    gp1[2]=(336,0,161,300)
    gp1[3]=(497,0,175,300)'''

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
        cont=0
   
    if cont==p*5:
        i=4
   
    if cont==p*6:
       i=5
       cont=0
   
    return

'''def golpep1():
    global cont

    gp1[0]=(0,0,161,300)
    gp1[1]=(161,0,175,300)
    gp1[2]=(336,0,161,300)
    gp1[3]=(497,0,175,300)
   
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
        cont=0;
    return'''

def sprite2():
 
    global cont2
 
    p2[0]=(850,0,200,300)
    p2[1]=(655,0,180,300)
    p2[2]=(490,0,161,300)
    p2[3]=(325,0,175,300)
    p2[4]=(155,0,161,300)
    p2[5]=(0,0,161,300)

    Rp2[0]=(0,0,200,300)
    Rp2[1]=(200,0,180,300)
    Rp2[2]=(380,0,175,300)
    Rp2[3]=(555,0,175,300)
    Rp2[4]=(730,0,175,300)
    Rp2[5]=(910,0,200,300)
   
    p=6
   
    global j
       
    if cont2==p:
        j=0
   
    if cont2==p*2:
        j=1
   
    if cont2==p*3:
        j=2
   
    if cont2==p*4:
        j=3
   
    if cont2==p*5:
        j=4
   
    if cont2==p*6:
       j=5
       cont2=0
   
    return
 
 
 
 
 
def main():
    pygame.init()    
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("KILLER INSTINCT")
    #sonido1=pygame.mixer.Sound("intro.mp3")
   
 
    fondo = imagen("fondo.png")
   
         
    personaje1 = imagen("Personajes/combo.png",True)  
    personaje1_inv=pygame.transform.flip(personaje1,True,False);
    #golpep1 = imagen("Personajes/combo_golpe.png", True)

    personaje2 = imagen("Personajes/fulgore.png",True)
    personaje2_inv = pygame.transform.flip(personaje2,True,False);
     
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

        '''if direc==True:
            screen.blit(golpep1, (MposX1, 350), (gp1[i]))'''

        sprite2()
        teclado2()

        if direc==True:
            screen.blit(personaje2, (MposX2, 350),(p2[j]))

        if direc==False:
            screen.blit(personaje2_inv, (MposX2, 350),(Rp2[j]))

   
        pygame.display.flip()
       
       
       
       
        # Cerrar la ventana
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
   
    return 0 
 
 
if __name__ == '__main__':
    main()

