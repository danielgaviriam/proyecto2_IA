import sys
import math

class Nodo:

	def __init__(self,intefaz):
		#False/Max 
		#True/Min
		self.type=False
		self.profundidad=0
		self.utilidad=(-1*math.inf)

