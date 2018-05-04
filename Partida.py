import sys
import pygame
import time as t
from pygame.locals import *


class Partida:

	def __init__(self,intefaz):
		self.interfaz=intefaz
		self.user_items=[]
		self.pc_items=[]
		#False:PC,True:Human
		self.turno=True
		#self.start()
		self.b1=""
		self.b2=""
		self.b3=""
		self.b4=""
		self.b5=""
		self.b6=""
		self.b7=""
		self.b8=""
		self.button_user=[self.b1,self.b2,self.b3,self.b4,self.b5,self.b6,self.b7,self.b8]
		
		

	def start(self):

		while self.interfaz.manzanas!=[]:
			self.actualizar_turno()
			#Eventos de tablero
			if self.turno==True:	
				pos=self.next(self.interfaz.pos_cn)
				self.crear_botones_player(pos)


			for evento in pygame.event.get():

				if evento.type == QUIT:
					pygame.quit()
					sys.exit()
							
				if evento.type == pygame.MOUSEBUTTONDOWN:
			
					mouse_pos = evento.pos  # gets mouse position
			
					if self.b1.collidepoint(mouse_pos):
						print "hola"
					if self.b2.collidepoint(mouse_pos):
						print "hola"
					if self.b3.collidepoint(mouse_pos):
						print "hola"
					if self.b4.collidepoint(mouse_pos):
						print "hola"
					if self.b5.collidepoint(mouse_pos):
						print "hola"
					if self.b6.collidepoint(mouse_pos):
						print "hola"
					if self.b7.collidepoint(mouse_pos):
						print "hola"
					if self.b8.collidepoint(mouse_pos):
						print "hola"


			
			
				


	#evalua que no caigan en la posicion del otro jugador
	def misma_posicion(self,x,y):
		if self.turno==True:
			if int(x)==int(self.interfaz.pos_cb[0]) and int(y)==int(self.interfaz.pos_cb[1]):
				return False
		if self.turno==False:
			if int(x)==int(self.interfaz.pos_cn[0]) and int(y)==int(self.interfaz.pos_cn[1]):
				return False

		return True


	#Posibles Jugadas que tendra el jugador de acuerdo a su posicion
	def next(self,pos_gamer):
		posibilidades=[]
		x=int(pos_gamer[0])
		y=int(pos_gamer[1])


		if(x+1)<6 and (y+2)<6:
			if self.misma_posicion((x+1),(y+2)):
				posibilidades.append([(x+1),(y+2)])
		if(x+1)<6 and (y-2)>=0:
			if self.misma_posicion((x+1),(y-2)):
				posibilidades.append([(x+1),(y-2)])
		if(x+2)<6 and (y+1)<6:
			if self.misma_posicion((x+2),(y+1)):
				posibilidades.append([(x+2),(y+1)])
		if(x+2)<6 and (y-1)>=0:
			if self.misma_posicion((x+2),(y-1)):
				posibilidades.append([(x+2),(y-1)])
		if(x-1)>=0 and (y-2)>=0:
			if self.misma_posicion((x-1),(y-2)):
				posibilidades.append([(x-1),(y-2)])
		if(x-1)>=0 and (y+2)<6:
			if self.misma_posicion((x-1),(y+2)):
				posibilidades.append([(x-1),(y+2)])
		if(x-2)>=0 and (y-1)>=0:
			if self.misma_posicion((x-2),(y-1)):
				posibilidades.append([(x-2),(y-1)])
		if(x-2)>=0 and (y+1)<6:
			if self.misma_posicion((x-2),(y+1)):
				posibilidades.append([(x-2),(y+1)])

		return posibilidades

	def actualizar_turno(self):
		turnero=pygame.image.load('pix/flecha.png')
		if self.turno==True:
			self.interfaz.ventana.blit(turnero,( 370 , 155))
		else:
			self.interfaz.ventana.blit(turnero,(370 , 195))	

		pygame.display.update()


	#adiciona botones en aquellas casillas que el se pueda mover
	def crear_botones_player(self, posibilidades):
		#transparent= pygame.Color(0, 0, 0, 0)#transparente

		#self.interfaz.b1
		i=0
		for pos in posibilidades:
			self.button_user[i]=pygame.Rect((pos[0]*60),(pos[1]*60),60,60)
			pygame.draw.rect(self.interfaz.ventana, [0, 0, 0], self.button_user[i])
			i=i+1

		self.button_user[0].move(10,10)
		pygame.display.update()	
		
			

		