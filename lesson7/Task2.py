from abc import ABC, abstractmethod

class MyAbstractClothes(ABC):
	@abstractmethod
	def my_method(self):
		pass

class MyJacket(MyAbstractClothes):

	def __init__(self, v):
		self.v = v
		print(f"v = {self.__v}")

	@property
	def v(self):
		return self.__v

	@v.setter
	def v(self, v):
		if v < 40:
			self.__v = 40
		elif v > 60:
			self.__v = 60
		else:
			self.__v = v

	def my_method(self):
		return f"ткани понадобится {round((self.v / 6.5 + 0.5), 2)} м"

	def __del__(self):
		print(f'Удаляем объект {self.v} класса MyJacket')

class MySuit(MyAbstractClothes):

	def __init__(self, h):
		self.h = h
		print(f"h = {self.__h}")

	@property
	def h(self):
		return self.__h

	@h.setter
	def h(self, h):
		if h < 1.4:
			self.__h = 1.4
		elif h > 2.2:
			self.__h = 2.2
		else:
			self.__h = h

	def my_method(self):
		return f"ткани понадобится {round((self.h * 2 + 0.3), 2)} м"

	def __del__(self):
		print(f'Удаляем объект {self.h} класса MySuit')

jacket = MyJacket(48)
print(jacket.my_method())
suit = MySuit(1.8)
print(suit.my_method())
