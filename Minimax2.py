from Nodo import *
import sys
from math import *
from copy import copy, deepcopy

#Permita hacer un mayor numero de llamados recursivos


class Minimax2:

	def __init__(self,pos_cn,pos_cb,user_items,pc_items,manzanas_disponibles):
		self.lista_nodos = []
		self.nodos_expandidos = []

		self.pos_cn = pos_cn
		self.pos_cb = pos_cb
		self.user_items = user_items
		self.pc_items = pc_items

		#creamos el nodo inicial
		nodo=Nodo()
		nodo.x = pos_cb[0]
		nodo.y = pos_cb[1]
		nodo.type = "Max"
		nodo.utilidad = -1 * float("inf")
		nodo.manzanas_disponibles = manzanas_disponibles
		nodo.user_items = user_items
		nodo.pc_items = pc_items
		nodo.pos_cb = pos_cb
		nodo.pos_cn = pos_cn
		self.lista_nodos.append(nodo)

		self.calcular()


	#funcionamiento similar al de amplitud
	def calcular(self):
		
		i=0
		while True:
			if self.lista_nodos[0].profundidad==9:
				break		

			print "---------------------profundidad : ",self.lista_nodos[0].profundidad,"-------------------------"
			
			if self.lista_nodos[0].profundidad == 1:
				break
		

			#Evalua si es un ciclo, sino lo es, lo expande
			if self.nodo_fue_expandido(self.lista_nodos[0].padre,self.lista_nodos[0]) == False:
				print "nodo a expandir",self.lista_nodos[0].x," ",self.lista_nodos[0].y
				print "manzanas cb blanco",len(self.lista_nodos[0].pc_items)
				print "manzanas cb negro",len(self.lista_nodos[0].user_items)
				
				expandidos = self.expandir_nodo(self.lista_nodos[0])
				
				for nodo in expandidos:
					#agrega cada nodo hijo al final de la lista
					self.lista_nodos.append(nodo)
				#sumarlo a la lista de expandidos
				self.nodos_expandidos.append(self.lista_nodos[0])
				#eliminarlo de la lista a recorrer
				self.lista_nodos.pop(0)
			#si ya lo expandio lo borra
			else:
				self.lista_nodos.pop(0)

			i=i+1
			if i == 2:
				break
				#pass
		#self.resumen_mini_max()
		#self.salida()


		#evita ciclos
	def nodo_fue_expandido(self,nodo_padre,nodo_a_verificar):
		#llego a la raiz
		if isinstance(nodo_padre, int) is True:
			print "expande es el nodo raiz"
			return False
		
		#si es igual a algun nodo padre 
		elif nodo_a_verificar.pos_cb == nodo_padre.pos_cb and nodo_a_verificar.pos_cn == nodo_padre.pos_cn and nodo_a_verificar.manzanas_disponibles == nodo_padre.manzanas_disponibles and nodo_padre.user_items==nodo_a_verificar.user_items and nodo_padre.pc_items==nodo_a_verificar.pc_items:	
			print "ya se ha expandido no expande"
			#self.print_nodo(nodo_a_verificar)
			#self.print_nodo(nodo_padre)
			return True
		else:
			print "ciclo"
			return self.nodo_fue_expandido(nodo_padre.padre,nodo_a_verificar)

	
	def expandir_nodo(self,nodo):
		nodos=[]
		
		if nodo.manzanas_disponibles != 0:
			
			posibilidades = self.movimientos_posibles(nodo)

			for pos in posibilidades:
				nodos.append(self.crear_nodo(pos[0],pos[1],nodo))

		return nodos


	#Posibles Jugadas que tendra quien se encuentre jugando, es decir
	#Recibe como parametro la posicion del caballo negro o blanco
	#Retornar un array con las coordenadas de posibles opciones que tiene segun la posicion
	def movimientos_posibles(self,nodo_a_expandir):
		posibilidades=[]
		if nodo_a_expandir.type==False:
			x = int(nodo_a_expandir.pos_cb[0])
			y = int(nodo_a_expandir.pos_cb[1])
		else:
			x = int(nodo_a_expandir.pos_cn[0])
			y = int(nodo_a_expandir.pos_cn[1])


		if(x+1)<6 and (y+2)<6:
			if self.misma_posicion((x+1),(y+2),nodo_a_expandir):
				posibilidades.append([(x+1),(y+2)])
		if(x+1)<6 and (y-2)>=0:
			if self.misma_posicion((x+1),(y-2),nodo_a_expandir):
				posibilidades.append([(x+1),(y-2)])
		if(x+2)<6 and (y+1)<6:
			if self.misma_posicion((x+2),(y+1),nodo_a_expandir):
				posibilidades.append([(x+2),(y+1)])
		if(x+2)<6 and (y-1)>=0:
			if self.misma_posicion((x+2),(y-1),nodo_a_expandir):
				posibilidades.append([(x+2),(y-1)])
		if(x-1)>=0 and (y-2)>=0:
			if self.misma_posicion((x-1),(y-2),nodo_a_expandir):
				posibilidades.append([(x-1),(y-2)])
		if(x-1)>=0 and (y+2)<6:
			if self.misma_posicion((x-1),(y+2),nodo_a_expandir):
				posibilidades.append([(x-1),(y+2)])
		if(x-2)>=0 and (y-1)>=0:
			if self.misma_posicion((x-2),(y-1),nodo_a_expandir):
				posibilidades.append([(x-2),(y-1)])
		if(x-2)>=0 and (y+1)<6:
			if self.misma_posicion((x-2),(y+1),nodo_a_expandir):
				posibilidades.append([(x-2),(y+1)])

		return posibilidades

	#Evita que ambos caballos no caigan en la misma posicion
	def misma_posicion(self,x,y,nodo_a_expandir):
		if nodo_a_expandir.type==True:
			if int(x)==int(nodo_a_expandir.pos_cb[0]) and int(y)==int(nodo_a_expandir.pos_cb[1]):
				return False
		if nodo_a_expandir.type==False:
			if int(x)==int(nodo_a_expandir.pos_cn[0]) and int(y)==int(nodo_a_expandir.pos_cn[1]):
				return False

		return True


	#Crea una instancia de la clase nodo y lo returna
	def crear_nodo(self,x,y,nodo_padre):
		
		#esta copia se hace solo para guardar los datos en el hijo, sin alterar la referencia al padre.
		copia_nodo_padre=deepcopy(nodo_padre)

		nodo=Nodo()
		nodo.x=x
		nodo.y=y
		nodo.padre=nodo_padre
		nodo.profundidad = copia_nodo_padre.profundidad + 1
		if copia_nodo_padre.type=="Max":
			nodo.type="Min"
			nodo.utilidad=float("inf")
			nodo.pos_cb=[x,y]
			nodo.pos_cn=copia_nodo_padre.pos_cn
		else:
			nodo.type="Max"
			nodo.utilidad=-1 * float("inf")
			nodo.pos_cn=[x,y]
			nodo.pos_cb=copia_nodo_padre.pos_cb

		# si en el movimiento coge una manzana
		if [x,y] in copia_nodo_padre.manzanas_disponibles:
			print "coge manzana"
			copia_nodo_padre.manzanas_disponibles.remove([x,y])
			manzanas = copia_nodo_padre.manzanas_disponibles
			nodo.manzanas_disponibles = manzanas
			

			if copia_nodo_padre.type == "Max":
				items_pc = copia_nodo_padre.pc_items
				items_pc.append([x,y])
				nodo.pc_items = items_pc
				nodo.user_items = copia_nodo_padre.user_items
			else:
				items_user = copia_nodo_padre.user_items
				items_user.append([x,y])
				nodo.user_items = items_user
				nodo.pc_items = copia_nodo_padre.pc_items
					
		else:
			nodo.manzanas_disponibles = copia_nodo_padre.manzanas_disponibles
			nodo.pc_items = copia_nodo_padre.pc_items
			nodo.user_items = copia_nodo_padre.user_items

		return nodo


	def resumen_mini_max(self):
		print "ptes"
		print len(self.lista_nodos)
		
		print "expandidos"
		print len(self.nodos_expandidos)
		
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
			print "utilidad",nodo.utilidad
			print type(nodo.padre)
			print "--------------------"
		

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