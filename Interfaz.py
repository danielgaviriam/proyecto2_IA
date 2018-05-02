import sys
import pygame
import time as t
from pygame.locals import *
from random import randint
from Partida import *

class Interfaz:

	def __init__(self):
		self.manzanas=[]
		self.pos_cb=[]
		self.pos_cn=[]
		self.num_items=0
		self.cantidad_items()
		self.manzana=pygame.image.load('pix/manzana.png')
		self.caballob=pygame.image.load('pix/blanco.png')
		self.caballon=pygame.image.load('pix/negro.png')			

	def cantidad_items(self):
		while int(self.num_items)%2==0:
			self.num_items = raw_input("Numero de items(impar): ")
			self.coordenadas_aleatorias(int(self.num_items))
		
	#Se encarga de pintar el ambiente inicial (Ambiente y menu principal)
	def ambInicial(self):

		pygame.init()
		#variables iniciales para creacion de grilla
		color=(160,160,160)#gris
		fondo=(255,255,255)#blanco
		colorDos=pygame.Color(224,224,224)#blanco
		#dimensiones para la grilla
		largo=60
		alto=60
		margen=2
		x=0
		y=0
		#lienzo
		self.ventana=pygame.display.set_mode((700, 360))
		#titulo para el lienzo
		pygame.display.set_caption("Proyecto#2-Inteligencia Artificial")


		#Dibujando Interfaz Inicial
		self.ventana.fill(fondo)
		i=0
		for fila in range(0,6):
			for columna in range(0,6):
				if i%2==0:
					pygame.draw.rect(self.ventana, color, (x,y,alto,largo))	
				else:
					pygame.draw.rect(self.ventana, colorDos, (x,y,alto,largo))	
					
				i=i+1
				x=x+60
			i=i+1
			y=y+60
			x=0


		#Pinta las manzanas y caballos
		self.pintar_escenario()

		#Pinta el menu ppal
		b_start = pygame.Rect(410,300,100,30)
		b_reset = pygame.Rect(550,300,100,30)
		self.menu_principal(b_start,b_reset)

		while True:
			
			for evento in pygame.event.get():
				if evento.type == QUIT:
					pygame.quit()
					sys.exit()
			if evento.type == pygame.MOUSEBUTTONDOWN:

				mouse_pos = evento.pos  # gets mouse position

				if b_start.collidepoint(mouse_pos):
					partida=Partida(self)

			pygame.display.update()

	#Crea una lista para las posiciones iniciales
	def coordenadas_aleatorias(self,cant_items):

		while len(self.manzanas)<int(cant_items):
			x=randint(0, 5)
			y=randint(0, 5)
			coord=[x,y]
			if coord not in self.manzanas:
				self.manzanas.append(coord)

		while self.pos_cb==[] or self.pos_cn==[]:
			coord_cb=[randint(0, 5),randint(0, 5)]
			coord_cn=[randint(0, 5),randint(0, 5)]

			if coord_cb not in self.manzanas and coord_cn not in self.manzanas and coord_cb != coord_cn:
				self.pos_cb=coord_cb
				self.pos_cn=coord_cn

	def pintar_escenario(self):
		#Pintar Manzanas y caballos
		for pos in self.manzanas:
			self.ventana.blit(self.manzana,( int(pos[0])*60 , int(pos[1])*60 ))

		self.ventana.blit(self.caballob,( int(self.pos_cb[0])*60 , int(self.pos_cb[1])*60 ))
		self.ventana.blit(self.caballon,( int(self.pos_cn[0])*60 , int(self.pos_cn[1])*60 ))


	def menu_principal(self,b_s,b_r):
		#Cargar Imagenes
		self.manzanam=pygame.image.load('pix/manzana_m.png')
		self.caballobm=pygame.image.load('pix/blanco_m.png')
		self.caballonm=pygame.image.load('pix/negro_m.png')
		#Titulo
		font = pygame.font.SysFont("comicsansms", 40)
		title = font.render("Proyecto #2", True, (107, 107, 107))
		self.ventana.blit(title,(360+(title.get_width()/2),5))
		#------------------------------------------------------
		#Nombres
		font = pygame.font.SysFont("comicsansms", 25)
		name1 = font.render("Hernan Arango-1710060", True, (0, 0, 0))
		name2 = font.render("Daniel Gaviria-1710145", True, (0, 0, 0))
		self.ventana.blit(name1,(360,50))
		self.ventana.blit(name2,(360,75))
		#------------------------------------------------------
		#Marcador-subtitulo
		font = pygame.font.SysFont("comicsansms", 30)
		resumen_title = font.render("Resumen", True, (107, 107, 107))
		self.ventana.blit(resumen_title,(360,120))
		#Marcador-resumen
		font = pygame.font.SysFont("comicsansms", 30)
		#user=font.render("Usuario", True, (0, 0, 0))
		#pc=font.render("PC", True, (0, 0, 0))
		self.ventana.blit(self.caballonm,(390,150))
		#ventana.blit(user,(420,155))
		self.ventana.blit(self.caballobm,(390,190))
		#ventana.blit(pc,(420,195))
		#------------------------------------------------------
		#Botones
		font = pygame.font.SysFont("comicsansms", 25)
		text_bs=font.render("Empezar", True, (0, 0, 0))
		pygame.draw.rect(self.ventana, [170, 170, 170], b_s)
		self.ventana.blit(text_bs,(422,305))
		text_br=font.render("Reiniciar", True, (0, 0, 0))
		pygame.draw.rect(self.ventana, [170, 170, 170], b_r)
		self.ventana.blit(text_br,(562,305))

		"""
		#Busqueda No Informada
		subtitle1 = font.render("Busqueda No Informada", True, (170, 170, 170))
		ventana.blit(subtitle1,(650+(subtitle1.get_width()/6),160))
		#Botones
		font = pygame.font.SysFont("comicsansms", 20)
		text_b1=font.render("Amplitud", True, (0, 0, 0))
		text_b2=font.render("Costo U.", True, (0, 0, 0))
		text_b3=font.render("Profundidad", True, (0, 0, 0))
		pygame.draw.rect(ventana, [170, 170, 170], b_1)
		pygame.draw.rect(ventana, [170, 170, 170], b_2)
		pygame.draw.rect(ventana, [170, 170, 170], b_3)
		ventana.blit(text_b1,(645+(text_b1.get_width()/3),207))
		ventana.blit(text_b2,(755+(text_b2.get_width()/3),207))
		ventana.blit(text_b3,(860+(text_b3.get_width()/6),207))
		#------------------------------------------------------
		#Busqueda Informada
		font = pygame.font.SysFont("comicsansms", 30)
		subtitle2 = font.render("Busqueda Informada", True, (170, 170, 170))
		ventana.blit(subtitle2,(650+(subtitle2.get_width()/4),250))
		#Botones
		font = pygame.font.SysFont("comicsansms", 20)
		text_b4=font.render("Avara", True, (0, 0, 0))
		text_b5=font.render("A*", True, (0, 0, 0))
		pygame.draw.rect(ventana, [170, 170, 170], b_4)
		pygame.draw.rect(ventana, [170, 170, 170], b_5)
		ventana.blit(text_b4,(720,288))
		ventana.blit(text_b5,(840,288))
		#------------------------------------------------------
		#Informes de Busqueda
		font = pygame.font.SysFont("comicsansms", 40)
		subtitle3 = font.render("Resumen", True, (170, 170, 170))
		ventana.blit(subtitle3,(650+(subtitle3.get_width()/1.5),320))
		font = pygame.font.SysFont("comicsansms", 20)
		subtitle4=font.render("# Nodos Expandidos:", True, (170, 170, 170))
		subtitle5=font.render("Profundidad del arbol:", True, (170, 170, 170))
		subtitle6=font.render("Tiempo de Ejecucion:", True, (170, 170, 170))
		ventana.blit(subtitle4,(660,360))
		ventana.blit(subtitle5,(660,420))
		ventana.blit(subtitle6,(660,480))
		#Boton de reset Interfaz
		text_b6=font.render("Reset", True, (0, 0, 0))
		text_b7=font.render("Cambiar Entrada", True, (0, 0, 0))
		pygame.draw.rect(ventana, [170, 170, 170], b_6)
		pygame.draw.rect(ventana, [170, 170, 170], b_7)
		ventana.blit(text_b6,(780,557))
		ventana.blit(text_b7,(878,557))
		"""