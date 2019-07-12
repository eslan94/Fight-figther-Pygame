fondo='fondo.png'
personaje='combo.png'
import pygame
from pygame.locals import*
from sys import exit

pygame.init()

screen=pygame.display.set_mode((510, 240), 0, 32)#ajuste de ventana para imagen de fondo
pygame.display.set_caption("Fight Fighter")
background=pygame.image.load(fondo).convert()
mouse_cursor=pygame.image.load(personaje).convert()

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit()
		screen.blit(background, (0,0))
		x, y=pygame.mouse.get_pos()
		x-=mouse_cursor.get_width()/2
		y-=mouse_cursor.get_height()/2
		screen.blit(mouse_cursor, (x, y))
		pygame.display.update()
