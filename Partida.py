import sys
import copy
import pygame
import time as t
from pygame.locals import *
from random import randint
from Interfaz import *
from Minimax import *
from Nodo import *
from copy import copy, deepcopy



class Partida:

	def __init__(self,intefaz):
		#Tipo interfaz,
		self.interfaz=intefaz
		#Lista que tendra la cantidad de manzanas que tomen el usuario y el pc
		self.user_items=[]
		self.pc_items=[]

		self.super_matriz = []

		self.blanco=[]
		self.negro=[]
		#Variable global para manejar los turnos durante el juego
		self.turno=False
		#Funcion utilizada para pintar en la pantalla una flecha que indica quien esta jugando(a quien le toca)
		self.actualizar_turno()
		self.iniciar_super_matriz()

		#Botones de movimiento para el usuario, estas se pintan en una posicion no visible inicialmente
		#luego son movimos hacia las opciones de jugada del usuario en cada turno
		self.b1=pygame.Rect(800,800,60,60)
		self.b2=pygame.Rect(800,800,60,60)
		self.b3=pygame.Rect(800,800,60,60)
		self.b4=pygame.Rect(800,800,60,60)
		self.b5=pygame.Rect(800,800,60,60)
		self.b6=pygame.Rect(800,800,60,60)
		self.b7=pygame.Rect(800,800,60,60)
		self.b8=pygame.Rect(800,800,60,60)

		self.b_reset = pygame.Rect(550,305,100,30)
		font = pygame.font.SysFont("comicsansms", 25)
		text_br=font.render("Salir", True, (0, 0, 0))
		pygame.draw.rect(self.interfaz.ventana, [170, 170, 170], self.b_reset)
		self.interfaz.ventana.blit(text_br,(580,310))
		pygame.display.update()


	def iniciar_super_matriz(self):
		self.super_matriz = [[0]*6,[0]*6,[0]*6,[0]*6,[0]*6,[0]*6]
		matriz_cn = [[0]*6,[0]*6,[0]*6,[0]*6,[0]*6,[0]*6]
		

		for i in range(6):
			for j in range(6):

				utilidades = []
				for x in range(34):
					utilidades.append([0]*34)

				#items_pc y items_user
				list_items = [[0]*34,[0]*34,utilidades]

				matriz_cn[i][j] = list_items


		for i in range(6):
			for j in range(6):
				self.super_matriz[i][j] = deepcopy(matriz_cn)

	def start(self):

		
		while True:
			
			#Evaluacion para no terminar con todos los items
			#if self.interfaz.manzanas==[] or abs(len(self.user_items)-len(self.pc_items))>len(self.interfaz.manzanas):
			#Evalua si el juego Termino
			if self.interfaz.manzanas==[]:

				self.pintar_ganador()

			#Eventos de tablero
			#turno tablero
			elif self.turno==True:	
				pos=self.next(self.interfaz.pos_cn)
				self.crear_botones_player(pos)
			#turno pc
			elif self.turno==False:
				minimax = Minimax(self.interfaz.pos_cn,self.interfaz.pos_cb,self.user_items,self.pc_items,self.interfaz.manzanas,self.super_matriz)
				
				print "mi_pos",minimax.pos_cb

				matriz_cn = [[0]*6,[0]*6,[0]*6,[0]*6,[0]*6,[0]*6]
		

				for i in range(6):
					for j in range(6):

						utilidades = []
						for x in range(34):
							utilidades.append([0]*34)

						#items_pc y items_user
						list_items = [[0]*34,[0]*34,utilidades]

						matriz_cn[i][j] = list_items

				self.super_matriz[minimax.pos_cb[0]][minimax.pos_cb[1]] = matriz_cn
				
				#mover caballo blanco
				self.moves(minimax.pos_cb,False)


				#aleatorio
				#pos=self.next(self.interfaz.pos_cb)
				#self.move_pc(pos)

			for evento in pygame.event.get():

				if evento.type == QUIT:
					pygame.quit()
					sys.exit()
							
				if evento.type == pygame.MOUSEBUTTONDOWN:
			
					mouse_pos = evento.pos  # gets mouse position
					#Cuando un usuario selecciona una opcion envia la coordenada que selecciono el jugador
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
					if self.b_reset.collidepoint(mouse_pos):
						pygame.quit()
						


	#LA funcion misma_posicion y next, seran redefinidas en minimax, las de la clase partida seran unicamente
	#para las jugadas del usuario, ya que se esta trabajando con las variables de la clase interfaz, miestras que
	#en minimax debemos trabajar con las de los nodos que se van expandiendo

	#Evita que ambos caballos no caigan en la misma posicion
	def misma_posicion(self,x,y):
		if self.turno==True:
			if int(x)==int(self.interfaz.pos_cb[0]) and int(y)==int(self.interfaz.pos_cb[1]):
				return False
		if self.turno==False:
			if int(x)==int(self.interfaz.pos_cn[0]) and int(y)==int(self.interfaz.pos_cn[1]):
				return False

		return True


	#Posibles Jugadas que tendra quien se encuentre jugando, es decir
	#Recibe como parametro la posicion del caballo negro o blanco
	#Retornar un array con las coordenadas de posibles opciones que tiene segun la posicion
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

	#Funcion utilizada para pintar en la pantalla una flecha que indica quien esta jugando(a quien le toca)
	def actualizar_turno(self):
		turnero=pygame.image.load('pix/flecha.png')
		capa=pygame.image.load('pix/capa.jpg')
		if self.turno==True:
			self.interfaz.ventana.blit(turnero,( 370 , 155))
			self.interfaz.ventana.blit(capa,( 370 , 235))
		else:
			self.interfaz.ventana.blit(turnero,(370 , 235))	
			self.interfaz.ventana.blit(capa,( 370 , 155))

		pygame.display.update()

	#Recorre el array de posibilidades y crea un boton por cada una (esto solo para el usuario)
	def crear_botones_player(self, posibilidades):
		marco=pygame.image.load('pix/marco.png')

		#self.interfaz.b1
		i=1
		for pos in posibilidades:
			self.create_buttons(i,pos[0],pos[1])
			i=i+1

		#pinta el tablero encima de los botones para que no se vean
		self.interfaz.pintar_escenario()
		for pos in posibilidades:
			self.interfaz.ventana.blit(marco,(int(pos[0])*60 , int(pos[1])*60))

		pygame.display.update()	
		
	#Pinta los botones que muestran al usuario sus opciones
	#CORREGIR: Los botones deben ser transparentes... para que no tape la interfaz (NO SUPE XD)
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

	#Recibe como parametro una coordenada que sera aquella que escogio el usuario o el pc y una
	#variable booleana que permite saber de quien es el movimiento (user=1)(pc=0)
	def moves(self,coord,turn):

		if turn == True:
			self.negro.append(coord)
		else:
			self.blanco.append(coord)
		
		print coord,self.interfaz.manzanas

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

	#Se encarga de actualizar el marcador segun la cantidad de items que tengan los array que cuentan la cantidad
	#de manzanas que tiene cada jugador
	def update_marker(self):
		manzana_m=pygame.image.load('pix/manzana_m.png')
		x_n=420
		y_n=150
		x_b=420
		y_b=230
		
		i=0
		for pos in self.user_items:
			if i<=7:
				self.interfaz.ventana.blit(manzana_m,( x_n , y_n))
				if i==7:
					x_n=390
			else:
				self.interfaz.ventana.blit(manzana_m,( x_n , y_n+30))

			i=i+1
			x_n=x_n+30

		i=0
		for pos in self.pc_items:
			if i<=7:
				self.interfaz.ventana.blit(manzana_m,( x_b , y_b))
				if i==7:
					x_b=390
			else:
				self.interfaz.ventana.blit(manzana_m,( x_b , y_b+30))
			i=i+1
			x_b=x_b+30

	#Funcion temporal, es para que la CPU escoja una opcion aleatoria entre sus opciones
	#Esta sera la que construya el arbol y retorne la mejor eleccion
	def move_pc(self,posibilidades):
		sel=randint(0, len(posibilidades)-1)
		self.moves(posibilidades[sel],0)

	def pintar_ganador(self):
		capa=pygame.image.load('pix/capa.jpg')
		self.interfaz.ventana.blit(capa,( 370 , 155))
		self.interfaz.ventana.blit(capa,( 370 , 195))
		#Ganador
		font = pygame.font.SysFont("comicsansms", 30)
		if len(self.user_items)>len(self.pc_items):
			ganador = font.render("Gano Usuario", True, (107, 107, 107))
			self.interfaz.ventana.blit(ganador,(460,105))

		else:
			ganador = font.render("Gano IA, Llorelo papa", True, (107, 107, 107))
			self.interfaz.ventana.blit(ganador,(425,105))
		
		print "mov caballo negro",self.negro
		print "mov caballo blanco",self.blanco
		pygame.display.update()


