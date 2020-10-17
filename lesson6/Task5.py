class Stationery():
	"""канцелярская принадлежность."""

	def __init__(self, title):
		"""Инициализирует атрибут title"""
		self.title = title

	def draw(self):
		print("Запуск отрисовки.")


class Pen():
	"""Ручка."""

	def __init__(self, title):
		"""Инициализирует атрибуты класса-родителя"""
		self.title = title

	def draw(self):
		print("Ручка рисует.")

class Pencil():
	"""Карандаш."""

	def __init__(self, title):
		"""Инициализирует атрибуты класса-родителя"""
		self.title = title

	def draw(self):
		print(f"{self.title} рисует.")


class Handle():
	"""Маркер."""

	def __init__(self, title):
		"""Инициализирует атрибуты класса-родителя"""
		self.title = title

	def draw(self):
		print(f"{self.title} рисует жирно и красиво.")

stationery = Stationery('Канцелярская принадлежность')
stationery.draw()
pen = Pen('Шариковая ручка')
pen.draw()
pencil = Pencil('Красный карандаш')
pencil.draw()
handle_bl = Handle('Синий маркер')
handle_bl.draw()
handle_gr = Handle('Зеленый маркер')
handle_gr.draw()
