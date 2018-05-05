import sys
import pygame
import time as t
from pygame.locals import *
from random import randint


class Partida:

	def __init__(self,intefaz):
		self.interfaz=intefaz
		self.user_items=[]
		self.pc_items=[]
		#False:PC,True:Human
		self.turno=True
		#self.start()
		#Botones de movimiento
		self.b1=pygame.Rect(800,800,60,60)
		self.b2=pygame.Rect(800,800,60,60)
		self.b3=pygame.Rect(800,800,60,60)
		self.b4=pygame.Rect(800,800,60,60)
		self.b5=pygame.Rect(800,800,60,60)
		self.b6=pygame.Rect(800,800,60,60)
		self.b7=pygame.Rect(800,800,60,60)
		self.b8=pygame.Rect(800,800,60,60)

	def start(self):
		self.actualizar_turno()
		while self.interfaz.manzanas!=[]:
			
			#Eventos de tablero
			if self.turno==True:	
				pos=self.next(self.interfaz.pos_cn)
				self.crear_botones_player(pos)

			elif self.turno==False:
				pos=self.next(self.interfaz.pos_cb)
				self.move_pc(pos)


			for evento in pygame.event.get():

				if evento.type == QUIT:
					pygame.quit()
					sys.exit()
							
				if evento.type == pygame.MOUSEBUTTONDOWN:
			
					mouse_pos = evento.pos  # gets mouse position
			
					if self.b1.collidepoint(mouse_pos):
						self.moves([int(self.b1.x/60),int(self.b1.y/60)],1)
					if self.b2.collidepoint(mouse_pos):
						self.moves([int(self.b2.x/60),int(self.b2.y/60)],1)
					if self.b3.collidepoint(mouse_pos):
						self.moves([int(self.b3.x/60),int(self.b3.y/60)],1)
					if self.b4.collidepoint(mouse_pos):
						self.moves([int(self.b4.x/60),int(self.b4.y/60)],1)
					if self.b5.collidepoint(mouse_pos):
						self.moves([int(self.b5.x/60),int(self.b5.y/60)],1)
					if self.b6.collidepoint(mouse_pos):
						self.moves([int(self.b6.x/60),int(self.b6.y/60)],1)
					if self.b7.collidepoint(mouse_pos):
						self.moves([int(self.b7.x/60),int(self.b7.y/60)],1)
					if self.b8.collidepoint(mouse_pos):
						self.moves([int(self.b8.x/60),int(self.b8.y/60)],1)


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
		capa=pygame.image.load('pix/capa.jpg')
		if self.turno==True:
			self.interfaz.ventana.blit(turnero,( 370 , 155))
			self.interfaz.ventana.blit(capa,( 370 , 195))
		else:
			self.interfaz.ventana.blit(turnero,(370 , 195))	
			self.interfaz.ventana.blit(capa,( 370 , 155))

		pygame.display.update()


	#adiciona botones en aquellas casillas que el se pueda mover
	def crear_botones_player(self, posibilidades):
		#transparent= pygame.Color(0, 0, 0, 0)#transparente

		#self.interfaz.b1
		i=1
		for pos in posibilidades:
			self.create_buttons(i,pos[0],pos[1])
			i=i+1

		pygame.display.update()	
		
			
	def create_buttons(self,id_button,x,y):
		color=Color(255,255,255,127)
		if id_button==1:
			self.b1=pygame.Rect((x*60),(y*60),60,60)
			pygame.draw.rect(self.interfaz.ventana, color, self.b1)
		if id_button==2:
			self.b2=pygame.Rect((x*60),(y*60),60,60)
			pygame.draw.rect(self.interfaz.ventana, color, self.b2)
		if id_button==3:
			self.b3=pygame.Rect((x*60),(y*60),60,60)
			pygame.draw.rect(self.interfaz.ventana, color, self.b3)
		if id_button==4:
			self.b4=pygame.Rect((x*60),(y*60),60,60)
			pygame.draw.rect(self.interfaz.ventana, color, self.b4)
		if id_button==5:
			self.b5=pygame.Rect((x*60),(y*60),60,60)
			pygame.draw.rect(self.interfaz.ventana, color, self.b5)
		if id_button==6:
			self.b6=pygame.Rect((x*60),(y*60),60,60)
			pygame.draw.rect(self.interfaz.ventana, color, self.b6)
		if id_button==7:
			self.b7=pygame.Rect((x*60),(y*60),60,60)
			pygame.draw.rect(self.interfaz.ventana, color, self.b7)
		if id_button==8:
			self.b8=pygame.Rect((x*60),(y*60),60,60)
			pygame.draw.rect(self.interfaz.ventana, color, self.b8)

	#Actualiza es estado del escenario y evalua si tomo o no una manzana
	def moves(self,coord,turn):
		#si tomo una manzana
		if coord in self.interfaz.manzanas:
			self.interfaz.manzanas.remove(coord)
			if turn==True:
				self.interfaz.pos_cn=coord
				self.user_items.append(coord)
				self.turno=False
			else:
				self.interfaz.pos_cb=coord
				self.pc_items.append(coord)
				self.turno=True
			
			self.interfaz.pintar_escenario()
			self.update_marker()
		#si no tomo una manzana
		else:
			if turn==True:
				self.interfaz.pos_cn=coord
				self.turno=False
			else:
				self.interfaz.pos_cb=coord
				self.turno=True
			
			self.interfaz.pintar_escenario()

		self.actualizar_turno()


	def update_marker(self):
		manzana_m=pygame.image.load('pix/manzana_m.png')
		x_n=450
		y_n=150
		x_b=450
		y_b=195
		for pos in self.user_items:
			self.interfaz.ventana.blit(manzana_m,( x_n , y_n))
			x_n=x_n+30

		for pos in self.pc_items:
			self.interfaz.ventana.blit(manzana_m,( x_b , y_b))
			x_b=x_b+30

	#Funcion temporal, es para que la CPU escoja una opcion aleatoria entre sus opciones
	def move_pc(self,posibilidades):
		sel=randint(0, len(posibilidades)-1)
		self.moves(posibilidades[sel],0)

