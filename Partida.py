import sys
import time as t

class Partida:

	def __init__(self,intefaz):
		self.interfaz=intefaz
		self.user_items=[]
		self.pc_items=[]
		self.start()

	def start(self):
		while self.interfaz.manzanas!=[]:
			pos=self.next(self.interfaz.pos_cb)


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