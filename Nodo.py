import sys
import math

class Nodo:

	def __init__(self):
		self.x = 0
		self.y = 0
		#False/Max 
		#True/Min
		self.type = "Max"
		self.profundidad = 0
		self.utilidad = 0
		self.padre = 0
		self.manzanas_disponibles = []
		self.user_items = []
		self.pc_items = []
		self.pos_cn = []
		self.pos_cb = []