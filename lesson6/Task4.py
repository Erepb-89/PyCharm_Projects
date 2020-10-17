from random import choice

class Car():
	"""Автомобиль."""

	def __init__(self, speed, color, name, is_police):
		"""Инициализирует атрибуты описания автомобиля."""
		self.speed = speed
		self.color = color
		self.name = name.title()
		self.is_police = is_police
		self.direction = ''

	def go(self):
		print(f"Машина {self.name} поехала")

	def stop(self):
		self.speed = 0
		print(f"Машина {self.name} остановилась")

	def turn(self, direction):
		direct = ['налево', 'направо']
		if direction == "direct":
			self.direction = choice(direct)
		else:
			self.direction = direction
		print(f"Машина {self.name} повернула {self.direction}")

	def show_speed(self):
		print(f"Текущая скорость машины {self.color} {self.name}: {self.speed}")

	def is_police_car(self):
		if self.is_police == True:
			print("Это полицейская машина")
		else:
			print("Это не полицейская машина")


class TownCar(Car):
	"""Городской автомобиль."""
	
	def __init__(self, speed, color, name, is_police):
		"""инициализирует атрибуты класса-родителя Car."""
		super().__init__(speed, color, name, is_police)

	def show_speed(self):
		ogr_speed = 60
		print(f"Текущая скорость машины {self.name}: {self.speed}")
		if self.speed > ogr_speed:
			print(f"Эй, полегче! Ограничение {ogr_speed} км/ч")


class WorkCar(Car):
	"""Грузовой автомобиль."""

	def __init__(self, speed, color, name, is_police):
		"""инициализирует атрибуты класса-родителя Car."""
		super().__init__(speed, color, name, is_police)

	def show_speed(self):
		ogr_speed = 40
		print(f"Текущая скорость машины {self.name}: {self.speed}")
		if self.speed > ogr_speed:
			print(f"Эй, полегче! Для грузовиков ограничение {ogr_speed} км/ч")


class SportCar(Car):
	"""Спортивный автомобиль."""

	def __init__(self, speed, color, name, is_police):
		"""инициализирует атрибуты класса-родителя Car."""
		super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
	"""Полицейский автомобиль."""

	def __init__(self, speed, color, name, is_police):
		"""инициализирует атрибуты класса-родителя Car."""
		super().__init__(speed, color, name, is_police)
		self.is_police = True


car = Car(70, 'красная', 'mazda', False)
car.go()
car.show_speed()
car.is_police_car()
car.turn('направо')
car.turn('direct')
car.stop()
car.show_speed()
car.go()
car.speed = 70
car.show_speed()
car.turn('direct')
print()
my_car = TownCar(65, 'зеленая', 'subaru', False)
my_car.go()
my_car.show_speed()
my_car.speed = 55
my_car.show_speed()
my_car.turn('direct')
print()
town_car = WorkCar(50, 'голубой', 'ЗИЛ', False)
town_car.go()
town_car.show_speed()
town_car.speed = 35
town_car.show_speed()
town_car.turn('direct')
print()
my_car.go()
my_car.speed = 70
my_car.show_speed()
print()
sport_car = SportCar(150, 'черная', 'chevrolet camarro', False)
sport_car.go()
sport_car.show_speed()
sport_car.turn('direct')
sport_car.turn('direct')
sport_car.stop()
sport_car.show_speed()
sport_car.is_police_car()
print()
police_car = PoliceCar(60, 'сине-белый', 'ford focus', False) # не смотря на False при определении
police_car.go()
police_car.show_speed()
police_car.is_police_car()
police_car.turn('direct')
