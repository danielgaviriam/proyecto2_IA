from Nodo import *
import sys
from math import *
from copy import copy, deepcopy
from datetime import datetime


class Minimax:

	def __init__(self,pos_cn,pos_cb,user_items,pc_items,manzanas_disponibles):
		self.lista_nodos = []
		self.nodos_expandidos = []

		
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

		self.iniciar_super_matriz()
		self.calcular()


	#funcionamiento similar al de amplitud eliminando nodos
	
	def calcular(self):
		
		i=0
		while True:
			#Si va a expandir nodos de mayor profundidad
			if self.lista_nodos ==[]:
				break				
			#si va a expandir un nodo de prof 5
			if self.lista_nodos[0].profundidad==7:
				#si ningun jugador a tomado manzanas
				if len(self.lista_nodos[0].pc_items)==0 and len(self.lista_nodos[0].user_items)==0:
					#No hay solucion-Empate
					self.lista_nodos[0].utilidad=0
				else:
					self.lista_nodos[0].utilidad=len(self.lista_nodos[0].pc_items)-len(self.lista_nodos[0].user_items)

				self.nodos_expandidos.append(self.lista_nodos[0])
				self.lista_nodos.pop(0)


			#Evalua si es un ciclo, sino lo es, lo expande
			elif self.nodo_fue_expandido(self.lista_nodos[0].padre,self.lista_nodos[0]) == False:
				
				expandidos = self.expandir_nodo(self.lista_nodos[0])

				if len(expandidos)==0:
					if len(self.lista_nodos[0].pc_items)==0 and len(self.lista_nodos[0].user_items)==0:
						#No hay solucion-Empate
						self.lista_nodos[0].utilidad=0
					else:
						self.lista_nodos[0].utilidad=len(self.lista_nodos[0].pc_items)-len(self.lista_nodos[0].user_items)

				
				for nodo in expandidos:
					#agrega cada nodo hijo al final de la lista
					self.lista_nodos.append(nodo)
				#sumarlo a la lista de expandidos
				self.nodos_expandidos.append(self.lista_nodos[0])
				#eliminarlo de la lista a recorrer
				self.lista_nodos.pop(0)
			#si ya lo expandio lo borra
			else:
				self.lista_nodos[0].utilidad=len(self.lista_nodos[0].pc_items)-len(self.lista_nodos[0].user_items)
				self.nodos_expandidos.append(self.lista_nodos[0])
				self.lista_nodos.pop(0)

			i=i+1
			if i == 2:
				#break
				pass

		#self.resumen_mini_max()
		#self.salida()
		print "termino-expandir"
		self.actualizar_utilidades()
	

	#funcionamiento similar al de amplitud sin eliminar
	"""
	def calcular2(self):
		
		i=0
		while i < len(self.lista_nodos):
			#si va a expandir un nodo de prof 5
			if self.lista_nodos[i].profundidad==7:
				#si ningun jugador a tomado manzanas
				if len(self.lista_nodos[i].pc_items)==0 and len(self.lista_nodos[i].user_items)==0:
					#No hay solucion-Empate
					self.lista_nodos[i].utilidad=0
				else:
					self.lista_nodos[i].utilidad=len(self.lista_nodos[i].pc_items)-len(self.lista_nodos[i].user_items)

				self.nodos_expandidos.append(self.lista_nodos[i])


			#Evalua si es un ciclo, sino lo es, lo expande
			elif self.nodo_fue_expandido(self.lista_nodos[i].padre,self.lista_nodos[i]) == False:
				
				
				expandidos = self.expandir_nodo(self.lista_nodos[i])

				#Evalua si es una hoja
				if len(expandidos)==0:
					if len(self.lista_nodos[i].pc_items)==0 and len(self.lista_nodos[i].user_items)==0:
						#No hay solucion-Empate
						self.lista_nodos[i].utilidad=0
					else:
						self.lista_nodos[i].utilidad=len(self.lista_nodos[i].pc_items)-len(self.lista_nodos[i].user_items)

				else:
					for nodo in expandidos:
						#agrega cada nodo hijo al final de la lista
						self.lista_nodos.append(nodo)
				
				#sumarlo a la lista de expandidos
				self.nodos_expandidos.append(self.lista_nodos[i])

			i=i+1
		
		print "termino-expandir"
		self.actualizar_utilidades()
	"""
	def iniciar_super_matriz(self):
		self.super_matriz = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
		matriz_cn = [[0]*5,[0]*5,[0]*5,[0]*5,[0]*5]
		

		for i in range(5):
			for j in range(5):
				#items_pc y items_user
				list_items = [[0]*33,[0]*33]

				matriz_cn[i][j] = list_items


		for i in range(5):
			for j in range(5):
				self.super_matriz[i][j] = deepcopy(matriz_cn)

	def set_in_super_matriz(self,nodo):
		

		sub_matriz = self.super_matriz[nodo.pos_cb[0]-1][nodo.pos_cb[1]-1] 
		
		list_items = sub_matriz[nodo.pos_cn[0]-1][nodo.pos_cn[1]-1]

		pc_items = list_items[0]
		user_items = list_items[1] 
		pc_items[len(nodo.pc_items)] = sorted(nodo.pc_items)
		user_items[len(nodo.user_items)] = sorted(nodo.user_items)

	def nodo_fue_expandido(self,nodo_padre,nodo_a_verificar):
		sub_matriz = self.super_matriz[nodo_a_verificar.pos_cb[0]-1][nodo_a_verificar.pos_cb[1]-1] 
		list_items = sub_matriz[nodo_a_verificar.pos_cn[0]-1][nodo_a_verificar.pos_cn[1]-1]

		pc_items = list_items[0]
		user_items = list_items[1] 

		if (pc_items[len(nodo_a_verificar.pc_items)] == 0 or pc_items[len(nodo_a_verificar.pc_items)] == [] ) and (user_items[len(nodo_a_verificar.user_items)] == 0 or user_items[len(nodo_a_verificar.user_items)] == []):
			print "expanda"
			self.set_in_super_matriz(nodo_a_verificar)
			return False
		else:
			if user_items[len(nodo_a_verificar.user_items)] == 0:
				user_items[len(nodo_a_verificar.user_items)] = []

			if pc_items[len(nodo_a_verificar.pc_items)] == 0:
				pc_items[len(nodo_a_verificar.pc_items)] = []

			if pc_items[len(nodo_a_verificar.pc_items)] == nodo_a_verificar.pc_items and user_items[len(nodo_a_verificar.user_items)] == nodo_a_verificar.user_items:
				return True
			else:
				print "toca verificar bien si puede expandir"
				return self.nodo_fue_expandido_original(nodo_padre,nodo_a_verificar)
			#return False

	#evita ciclos
	def nodo_fue_expandido_original(self,nodo_padre,nodo_a_verificar):
		#llego a la raiz
		if isinstance(nodo_padre, int) is True:
			print "expande es el nodo raiz"
			return False
		
		if len(nodo_padre.user_items) < len(nodo_a_verificar.user_items) or len(nodo_padre.pc_items) < len(nodo_a_verificar.pc_items):
			print "nueva verificacion"
			return False

		#si es igual a algun nodo padre 
		elif nodo_a_verificar.pos_cb == nodo_padre.pos_cb and nodo_a_verificar.pos_cn == nodo_padre.pos_cn and sorted(nodo_padre.user_items)==sorted(nodo_a_verificar.user_items) and sorted(nodo_padre.pc_items)==sorted(nodo_a_verificar.pc_items):	
			print "ya se ha expandido no expande"
			#self.print_nodo(nodo_a_verificar)
			#self.print_nodo(nodo_padre)
			return True
		else:
			print "ciclo"
			return self.nodo_fue_expandido_original(nodo_padre.padre,nodo_a_verificar)

	def expandir_nodo(self,nodo):
		nodos=[]
		
		if nodo.manzanas_disponibles != []:
			
			posibilidades = self.movimientos_posibles(nodo)

			for pos in posibilidades:
				nodos.append(self.crear_nodo(pos[0],pos[1],nodo))

		return nodos


	#Posibles Jugadas que tendra quien se encuentre jugando, es decir
	#Recibe como parametro la posicion del caballo negro o blanco
	#Retornar un array con las coordenadas de posibles opciones que tiene segun la posicion
	def movimientos_posibles(self,nodo_a_expandir):
		posibilidades=[]
		if nodo_a_expandir.type=="Max":
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
		if nodo_a_expandir.type=="Min":
			if int(x)==int(nodo_a_expandir.pos_cb[0]) and int(y)==int(nodo_a_expandir.pos_cb[1]):
				return False
		if nodo_a_expandir.type=="Max":
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
				nodo.pc_items = sorted(items_pc)
				nodo.user_items = sorted(copia_nodo_padre.user_items)
			else:
				items_user = copia_nodo_padre.user_items
				items_user.append([x,y])
				nodo.user_items = sorted(items_user)
				nodo.pc_items = sorted(copia_nodo_padre.pc_items)
					
		else:
			nodo.manzanas_disponibles = copia_nodo_padre.manzanas_disponibles
			nodo.pc_items = sorted(copia_nodo_padre.pc_items)
			nodo.user_items = sorted(copia_nodo_padre.user_items)

		return nodo

	def actualizar_utilidades(self):
		print "--------------actualizando utilidades-------------"
		print "tamano a recorrer",len(self.nodos_expandidos)

		start = datetime.now()
		
		
		for hoja in reversed(self.nodos_expandidos):

			#print "------", hoja.profundidad,"-",hoja.utilidad,"------"

			if isinstance(hoja.padre, int) is True:
				print "llegue al raiz,no hay mas hojas"
				print "utilidad",hoja.utilidad
				print "utilidad",hoja.pos_cb
				self.pos_cb = hoja.pos_cb
				return hoja.pos_cb

			if hoja.type == "Max":
				#si min tiene mas utilidad que max entonces ponemos menor utilidad
				if hoja.padre.utilidad >= hoja.utilidad:
					hoja.padre.utilidad = hoja.utilidad
					#si la profundidad del padre es cero actualizamos la posicion para saber donde mover
					if hoja.padre.profundidad == 0:
						hoja.padre.pos_cb = hoja.pos_cb			
			else:
				#si max tiene menor utilidad que min ponemos la de mayor utilidad
				if hoja.padre.utilidad <= hoja.utilidad:
					hoja.padre.utilidad = hoja.utilidad
					#si la profundidad del padre es cero actualizamos la posicion para saber donde mover
					if hoja.padre.profundidad == 0:
						hoja.padre.pos_cb = hoja.pos_cb			
				
						

			

		print datetime.now()-start


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