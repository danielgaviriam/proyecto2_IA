from Nodo import *
import sys
from math import *

class Minimax:

	def __init__(self,Partida):
		self.partida=Partida
		self.lista_nodos=[]
		self.nodos_expandidos=[]


	def crear_nodo_inicial(self):
		nodo=Nodo()
		nodo.x=self.partida.interfaz.pos_cb[0]
		nodo.y=self.partida.interfaz.pos_cb[1]
		nodo.type=False
		nodo.utilidad=-1 * float("inf")
		manzanas_copy=self.partida.interfaz.manzanas
		nodo.manzanas_disponibles=manzanas_copy
		nodo.user_items=self.partida.user_items
		nodo.pc_items=self.partida.pc_items
		nodo.pos_cb=self.partida.interfaz.pos_cb
		nodo.pos_cn=self.partida.interfaz.pos_cn
		self.lista_nodos.append(nodo)

	#Crea una instancia de la clase nodo y lo returna
	def crear_nodo(self,x,y,nodo_padre):
		
		n=Nodo()
		n.x=x
		n.y=y
		n.padre=nodo_padre
		n.profundidad = nodo_padre.profundidad + 1
		if nodo_padre.type==False:
			n.type=True
			n.utilidad=float("inf")
			n.pos_cn=[x,y]
			n.pos_cb=nodo_padre.pos_cb
		else:
			n.type=False
			n.utilidad=-1 * float("inf")
			n.pos_cb=[x,y]
			n.pos_cn=nodo_padre.pos_cn

		if [x,y] in nodo_padre.manzanas_disponibles:
				manzanas=nodo_padre.manzanas_disponibles.remove([x,y])
				n.manzanas_disponibles=manzanas

				if nodo_padre.type==False:
					items_user=nodo_padre.user_items
					items_user.append([x,y])
					n.user_items=items_user
					n.pc_items=nodo_padre.pc_items
				else:
					items_pc=nodo_padre.pc_items
					items_pc.append([x,y])
					n.pc_items=items_pc
					n.user_items=nodo_padre.user_items
		else:
			n.manzanas_disponibles=nodo_padre.manzanas_disponibles
			n.pc_items=nodo_padre.pc_items
			n.user_items=nodo_padre.user_items

		return n

	def expandir_nodo(self,nodo):
		nodos=[]
		if nodo.type==False:
			posibilidades=next([nodo.pos_cn[0],nodo.pos_cn[1]])
		else:
			posibilidades=next([nodo.pos_cb[0],nodo.pos_cb[1]])

		for pos in posibilidades:
			nodos.append(self.crear_nodo(pos[0],pos[1],nodo))

		return nodos

	#funcionamiento similar al de amplitud
	def calcular(self):
		self.crear_nodo_inicial()
		i=0
		while True:
			#print len(self.partida.interfaz.manzanas),"|hola"
			#if i==200:
			if self.lista_nodos[0].manzanas_disponibles==[]:
				print "termino"
				break

			print "nodo a expandir",self.lista_nodos[0].x," ",self.lista_nodos[0].y

			expandidos=self.expandir_nodo(self.lista_nodos[0])

			for nodo in expandidos:
				#agrega cada nodo hijo al final de la lista
				self.lista_nodos.append(nodo)

			#sumarlo a la lista de expandidos
			self.nodos_expandidos.append(self.lista_nodos[0])
			#eliminarlo de la lista a recorrer
			self.lista_nodos.pop(0)

			#i=i+1

		self.resumen_mini_max()

	def resumen_mini_max(self):
		for nodo in self.nodos_expandidos:
			print "coord_x ",nodo.x
			print "coord_y ",nodo.y
			print "prof ",nodo.profundidad
			print "manz ",nodo.manzanas_disponibles
			print "user ",nodo.user_items
			print "pc ",nodo.pc_items
			print "type ",nodo.type
			print "pos_user ",nodo.pos_cn
			print "pos_pc ",nodo.pos_cb
			print "--------------------"