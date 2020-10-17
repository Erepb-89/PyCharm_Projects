from time import sleep
from itertools import cycle

class TrafficLight():
	"""Светофор."""

	def __init__(self):
		"""Инициализирует атрибут color"""
		self.__color = []

	def running(self):
		self.__color = ['red', 'green']
		iter = cycle(self.__color)
		times = 3
		while times > 0:
			print("\033[31m\033[40m {}" .format(next(iter)))
			sleep(7)
			print("\033[33m {}" .format('yellow'))
			sleep(2)
			print("\033[32m {}".format(next(iter)))
			sleep(7)
			print("\033[33m {}".format('yellow'))
			sleep(2)
			times -= 1
my_svetofor = TrafficLight()
my_svetofor.running()
