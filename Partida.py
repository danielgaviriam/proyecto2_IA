import sys
import time as t
import pygame

class Partida:

	def __init__(self,intefaz):
		self.interfaz=intefaz
		self.user_items=[]
		self.pc_items=[]
		#False:PC,True:Human
		self.turno=True
		self.start()
		
		

	def start(self):
		while self.interfaz.manzanas!=[]:
			if self.turno==True:
				pos=self.next(self.interfaz.pos_cb)
				self.crear_botones_player(pos)




	#Posibles Jugadas que tendra el jugador de acuerdo a su posicion
	def next(self,pos_gamer):
		posibilidades=[]
		x=int(pos_gamer[0])
		y=int(pos_gamer[1])


		if(x+1)<6 and (y+2)<6:
			posibilidades.append([(x+1),(y+2)])
		if(x+1)<6 and (y-2)>=0:
			posibilidades.append([(x+1),(y-2)])
		if(x+2)<6 and (y+1)<6:
			posibilidades.append([(x+2),(y+1)])
		if(x+2)<6 and (y-1)>=0:
			posibilidades.append([(x+2),(y-1)])
		if(x-1)>=0 and (y-2)>=0:
			posibilidades.append([(x-1),(y-2)])
		if(x-1)>=0 and (y+2)<6:
			posibilidades.append([(x-1),(y+2)])
		if(x-2)>=0 and (y-1)>=0:
			posibilidades.append([(x-2),(y-1)])
		if(x-2)>=0 and (y+1)<6:
			posibilidades.append([(x-2),(y+1)])

		return posibilidades

	#muestras las opciones al jugador
	def crear_botones_player(self, posibilidades):
		marco=pygame.image.load('pix/marco.png')

		for pos in posibilidades:
			self.interfaz.ventana.blit(marco,( int(pos[0])*60 , int(pos[1])*60 ))

		pygame.display.update()

