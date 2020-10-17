class Worker():
	"""Работник."""

	def __init__(self, name, surname, position):
		"""Инициализирует атрибуты name, surname, position"""
		self.name = name
		self.surname = surname
		self.position = position
		self._income = 0
		self.my_dict = {"wage": 15000, "bonus": 60000}

class Position(Worker):
	"""Измененный класс Работник."""

	def __init__(self, name, surname, position):
		"""Инициализирует атрибуты класса-родителя Работник."""
		super().__init__(name, surname, position)

	def get_full_name(self):
		print(f"{self.name.title()} {self.surname.title()}")
	def get_total_income(self):
		self._income = self.my_dict['wage'] + self.my_dict['bonus']
		print(f"{self.position}: {self._income}")

worker = Worker('Petya', 'Vasechkin', 'constructor')
print(worker.name)
print(worker.surname)
print(worker.position)

vasyas_position = Position('vasya', 'Pupkin', 'cop')
my_position = Position('egor', 'varlamov', 'engineer')
my_position.get_full_name()
my_position.get_total_income()

vasyas_position.get_full_name()
vasyas_position.get_total_income()
vasyas_position.position = 'doctor'
vasyas_position.get_full_name()
vasyas_position.get_total_income()
