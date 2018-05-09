from Nodo import *
import sys
from math import *
from copy import copy, deepcopy

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
		
		#esta copia se hace solo para guardar los datos en el hijo, sin alterar la referencia al padre.
		copia_nodo_padre=deepcopy(nodo_padre)

		n=Nodo()
		n.x=x
		n.y=y
		n.padre=nodo_padre
		n.profundidad = copia_nodo_padre.profundidad + 1
		if copia_nodo_padre.type==False:
			n.type=True
			n.utilidad=float("inf")
			n.pos_cb=[x,y]
			n.pos_cn=copia_nodo_padre.pos_cn
		else:
			n.type=False
			n.utilidad=-1 * float("inf")
			n.pos_cn=[x,y]
			n.pos_cb=copia_nodo_padre.pos_cb

		if [x,y] in copia_nodo_padre.manzanas_disponibles:
			copia_nodo_padre.manzanas_disponibles.remove([x,y])
			manzanas=copia_nodo_padre.manzanas_disponibles
			n.manzanas_disponibles=manzanas
			

			if copia_nodo_padre.type==False:
				items_pc=copia_nodo_padre.pc_items
				items_pc.append([x,y])
				n.pc_items=items_pc
				n.user_items=copia_nodo_padre.user_items
			else:
				items_user=copia_nodo_padre.user_items
				items_user.append([x,y])
				n.user_items=items_user
				n.pc_items=copia_nodo_padre.pc_items
					
		else:
			n.manzanas_disponibles=copia_nodo_padre.manzanas_disponibles
			n.pc_items=copia_nodo_padre.pc_items
			n.user_items=copia_nodo_padre.user_items

		return n

	def expandir_nodo(self,nodo):
		nodos=[]
		#Evitar referencia
		#nodo=deepcopy(nodo)
		#evitar que expanda nodos hoja
		if nodo.manzanas_disponibles!=[]:
			
			posibilidades=self.next(nodo)

			for pos in posibilidades:
				nodos.append(self.crear_nodo(pos[0],pos[1],nodo))

		return nodos

	#funcionamiento similar al de amplitud
	def calcular(self):
		self.crear_nodo_inicial()
		i=0
		while True:
			print "---------------------",len(self.lista_nodos),"-------------------------"
			#si temina
			if self.lista_nodos==[]:
				break		

			#if i==00000:
			#	break

			#si encuentra una hoja
			if self.lista_nodos[0].manzanas_disponibles==[]:
				#calcula la utilidad
				self.lista_nodos[0].utilidad=len(self.lista_nodos[0].pc_items)-len(self.lista_nodos[0].user_items)

				self.nodos_expandidos.append(self.lista_nodos[0])
				self.lista_nodos.pop(0)

			#Evalua si es un ciclo, sino lo es, lo expande
			elif self.nodo_fue_expandido(self.lista_nodos[0].padre,self.lista_nodos[0]) == False:
				print "nodo a expandir",self.lista_nodos[0].x," ",self.lista_nodos[0].y
				expandidos=[]
				expandidos=self.expandir_nodo(self.lista_nodos[0])
				for nodo in expandidos:
					#agrega cada nodo hijo al final de la lista
					self.lista_nodos.append(nodo)
				#sumarlo a la lista de expandidos
				self.nodos_expandidos.append(self.lista_nodos[0])
				#eliminarlo de la lista a recorrer
				self.lista_nodos.pop(0)
			#es un ciclo, lo borra, sin expandir
			else:
				self.lista_nodos.pop(0)

			i=i+1

		self.resumen_mini_max()
		self.salida()

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

	#evita ciclos
	def nodo_fue_expandido(self,nodo_padre,nodo_a_verificar):
		#llego a la raiz
		if isinstance(nodo_padre, int) is True:
			print "expande es el nodo raiz"
			return False
		
		#si es igual a algun nodo padre 
		elif nodo_a_verificar.pos_cb == nodo_padre.pos_cb and nodo_a_verificar.pos_cn == nodo_padre.pos_cn and nodo_a_verificar.manzanas_disponibles == nodo_padre.manzanas_disponibles and nodo_padre.user_items==nodo_a_verificar.user_items and nodo_padre.pc_items==nodo_a_verificar.pc_items:	
			print "ya se ha expandido no expande"
			self.print_nodo(nodo_a_verificar)
			self.print_nodo(nodo_padre)
			return True
		else:
			print "ciclo"
			return self.nodo_fue_expandido(nodo_padre.padre,nodo_a_verificar)

	
	#LA funcion misma_posicion y next, seran redefinidas en minimax, las de la clase partida seran unicamente
	#para las jugadas del usuario, ya que se esta trabajando con las variables de la clase interfaz, miestras que
	#en minimax debemos trabajar con las de los nodos que se van expandiendo

	#Evita que ambos caballos no caigan en la misma posicion
	def misma_posicion(self,x,y,nodo_a_expandir):
		if nodo_a_expandir.type==True:
			if int(x)==int(nodo_a_expandir.pos_cb[0]) and int(y)==int(nodo_a_expandir.pos_cb[1]):
				return False
		if nodo_a_expandir.type==False:
			if int(x)==int(nodo_a_expandir.pos_cn[0]) and int(y)==int(nodo_a_expandir.pos_cn[1]):
				return False

		return True


	#Posibles Jugadas que tendra quien se encuentre jugando, es decir
	#Recibe como parametro la posicion del caballo negro o blanco
	#Retornar un array con las coordenadas de posibles opciones que tiene segun la posicion
	def next(self,nodo_a_expandir):
		posibilidades=[]
		if nodo_a_expandir.type==False	:
			x=int(nodo_a_expandir.pos_cb[0])
			y=int(nodo_a_expandir.pos_cb[1])
		else:
			x=int(nodo_a_expandir.pos_cn[0])
			y=int(nodo_a_expandir.pos_cn[1])


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

	def actualizar_utilidades_arbol(self):
		
		hoja=self.posicion_hoja_mas_profunda()
		if hoja !=0:
			if isinstance(hoja.padre, int) is True:
				print "llegue al raiz,no hay mas hojas"
				#return hoja.utilidad

			else: 
				if hoja.type==False:
					if hoja.padre.utilidad > hoja.utilidad:
						hoja.padre.utilidad=hoja.utilidad
				else:
					if hoja.padre.utilidad < hoja.utilidad:
						hoja.padre.utilidad=hoja.utilidad

				self.nodos_expandidos.remove(hoja)
				self.actualizar_utilidades_arbol()

	
	def posicion_hoja_mas_profunda(self):
		flag=0

		for nodo in self.nodos_expandidos:
			if nodo.utilidad != -1 * float("inf") and nodo.utilidad != float("inf") and flag==0:
				flag=nodo

			if nodo.utilidad != -1 * float("inf") and nodo.utilidad != float("inf") and flag!=0:
				if nodo.profundidad>flag.profundidad:
					flag=nodo

		return flag