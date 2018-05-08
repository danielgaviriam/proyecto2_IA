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
		nodo.manzanas_disponibles=self.partida.interfaz.manzanas
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
		#evitar que expanda nodos hoja
		if nodo.manzanas_disponibles!=None:
			if nodo.type==False:
				posibilidades=self.partida.next([nodo.pos_cb[0],nodo.pos_cb[1]])
				for pos in posibilidades:
					nodos.append(self.crear_nodo(pos[0],pos[1],nodo))
			else:
				posibilidades=self.partida.next([nodo.pos_cn[0],nodo.pos_cn[1]])
			
			for pos in posibilidades:
				nodos.append(self.crear_nodo(pos[0],pos[1],nodo))

		return nodos

	#funcionamiento similar al de amplitud
	def calcular(self):
		self.crear_nodo_inicial()
		i=0
		while True:
			if self.lista_nodos==[]:
				break		
			if self.lista_nodos[0].manzanas_disponibles==None:
				self.lista_nodos[0].utilidad=len(self.lista_nodos[0].user_items)-len(self.lista_nodos[0].pc_items)
				self.nodos_expandidos.append(self.lista_nodos[0])
				self.lista_nodos.pop(0)


			print "nodo a expandir",self.lista_nodos[0].x," ",self.lista_nodos[0].y
			expandidos=[]
			if self.nodo_fue_expandido(self.lista_nodos[0].padre,self.lista_nodos[0]) == False:
				expandidos=self.expandir_nodo(self.lista_nodos[0])
				for nodo in expandidos:
					#agrega cada nodo hijo al final de la lista
					self.lista_nodos.append(nodo)
				#sumarlo a la lista de expandidos
				self.nodos_expandidos.append(self.lista_nodos[0])
				#eliminarlo de la lista a recorrer
				self.lista_nodos.pop(0)
			else:
				self.lista_nodos.pop(0)

			i=i+1

		self.salida()
		#self.resumen_mini_max()

	def salida(self):
		print "utilidades nodos_hoja"
		for nodo in self.nodos_expandidos:
			if nodo.utilidad != float("inf") and nodo.utilidad != (-1*float("inf")):
				print nodo.utilidad
		print "fin nodos_hoja"

	def prof_max(self):
		for nodo in self.nodos_expandidos:
			if flag < nodo.profundidad:
				flag=nodo.profundidad
		return flag

	def resumen_mini_max(self):
		print "ptes"
		print len(self.lista_nodos)
		print "expandidos"
		print len(self.nodos_expandidos)

	def print_nodo(self,nodo):
		print "coord_x ",nodo.x
		print "coord_y ",nodo.y
		print "prof ",nodo.profundidad
		print "manz ",nodo.manzanas_disponibles
		print "user ",nodo.user_items
		print "pc ",nodo.pc_items
		print "type ",nodo.type
		print "pos_user ",nodo.pos_cn
		print "pos_pc ",nodo.pos_cb
		print type(nodo.padre)
		print "--------------------"

	#evita ciclos
	def nodo_fue_expandido(self,nodo_padre,nodo_a_verificar):
		#llego a la raiz
		if isinstance(nodo_padre, int) is True:
			print "expande es el nodo raiz"
			return False
		#si es igual a algun nodo padre 
		elif nodo_a_verificar.pos_cb == nodo_padre.pos_cb and nodo_a_verificar.pos_cn == nodo_padre.pos_cn and nodo_a_verificar.manzanas_disponibles == nodo_padre.manzanas_disponibles and nodo_padre.user_items==nodo_a_verificar.user_items and nodo_padre.pc_items==nodo_a_verificar.pc_items:
			print "ya se ha expandido no expande"
			return True
		else:
			print "ciclo"
			return self.nodo_fue_expandido(nodo_padre.padre,nodo_a_verificar)