import pygame
from pygame.locals import*
from sys import exit
from random import randint


pygame.init()

puntaje=0
perder= False
vida1=100
vida2=100

#Musica del juego
pygame.mixer.music.set_volume(0.8) #Configuracion del Volumen
pygame.mixer.music.load("figther.mp3") #Carga de mp3 sonido de fondo
pygame.mixer.music.play(-1, 0.0) #Bucle infinito de reproduccion del sonido, se detiene al momento de un evento
while True:
	for event in pygame.event.get():
		if event.type== QUIT:
			exit()
	if perder: 
		vida1 = 0 #Cuando personaje 1 se queda sin vida
		vida2 = 0 #Cuando personaje 2 se queda sin vida
		screen.blit(pygame.image.load("perdio.png"), (150, 340)) #Cargamos la imagen de game over
		pygame.mixer.music.set_volume(0.9) #Configuracion del Volumen
		pygame.mixer.music.load("GameOver.mp3") #Carga de mp3 sonido de gameover
		pygame.mixer.music.play() #Ejecucion al momento de evento
		perder= True #Se ejecuta cuando se pierde el juego


screen.blit(pygame.font.SysFont("tahoma", 30).render("Puntacion: " + str(puntaje), True, blanco), (650, 500)) #Puntaje mostrado en pantalla con el fondo blanco

