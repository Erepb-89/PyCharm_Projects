class Road():
	"""Дорога."""

	def __init__(self, length, width):
		"""Инициализирует атрибуты length, width """
		self._length = length
		self._width = width
		self.mass = 25
		self.cm = 5

	def square(self):
		print(f"{self._length * self._width * self.mass * self.cm / 1000} т")

my_road = Road(2500, 20)
my_road.square()
