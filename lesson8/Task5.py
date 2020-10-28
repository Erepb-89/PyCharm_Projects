from Task4 import Orgtechnic, Printer, Scanner, Xerox
from Task6 import OwnError

class Sklad:
	def __init__(self, name):
		self.all_goods = {}
		self.goods = []
		self.num = 1
		self.name = name

	def take(self, obj):
		self.goods = []
		#num = int(len(self.all_goods.keys()))
		self.obj = obj
		self.goods = self.obj.product
		while self.num in self.all_goods.keys():
			self.num += 1
		self.all_goods[self.num] = self.obj.product
		print(f"Создан объект {self.goods} и добавлен на склад")

		self.sklad_contain()

	def sklad_contain(self):
		print(f"Содержимое склада {self.name}:")
		for key, val in sorted(self.all_goods.items()):
			print(f"{key}: {val}")
		print('*' * 50)

	def delete_product(self, num):
		self.num = num
		print(f"Со склада удален объект {self.all_goods[self.num]}")
		del(self.all_goods[self.num])
		self.sklad_contain()

	def move_product(self, num, other):
		self.num = num
		other.num = num
		print(f"Со склада перемещен объект {self.all_goods[self.num]}")
		other.all_goods[other.num] = self.all_goods[self.num]
		del(self.all_goods[self.num])
		self.sklad_contain()
		other.sklad_contain()
		other.num += 1

	def check_contain(self, obj):
		contain = False
		for val in self.all_goods.copy().values():
			if obj.name == val[0] and obj.number == val[2] and obj.price == val[1]:
				print(f'Товар {val} уже есть на складе')
				contain = True
				print('*' * 50)
				break
			else:
				contain = False
		if not contain:
			self.take(obj)

	@staticmethod
	def func_print():
		print(f"1 - Добавить товар на склад\n"
			  f"2 - Переместить товар со склада\n"
			  f"3 - Удалить товар со склада\n"
			  f"4 - Просмотреть содержимое Склада")
		if all_departments[1] in all_sklad:
			print(f"5 - Просмотреть содержимое склада {all_departments[1]}\n"
			  f"6 - Переместить товар со склада {all_departments[1]}")
		if all_departments[2] in all_sklad:
			print(f"7 - Просмотреть содержимое склада {all_departments[2]}\n"
			  f"8 - Переместить товар со склада {all_departments[2]}")
		if all_departments[3] in all_sklad:
			print(f"9 - Просмотреть содержимое склада {all_departments[3]}\n"
			  f"10 - Переместить товар со склада {all_departments[3]}")

	@staticmethod
	def define_attr(obj_class):
		error = True
		while error:
			name = input("Введите наименование: ")
			price = input("Введите цену: ")
			try:
				price = int(price)
			except (ValueError, OwnError) as err1:
				error = True
				print(err1)
			else:
				error = False
			number = input("Введите количество: ")
			try:
				number = int(number)
			except (ValueError, OwnError) as err2:
				error = True
				print(err2)
			else:
				error = False
			units = input("Введите единицы измерения: ")
			attr = ''
			if obj_class == Printer:
				attr = input("Введите цвет тонера: ")
			elif obj_class == Scanner:
				attr = input("Введите точность в mpi: ")
			elif obj_class == Xerox:
				attr = input("Введите тип подачи: ")
			obj = obj_class(name, price, number, units, attr)
			print('*' * 50)
			if error == False:
				return obj
			else:
				print('Повторите ввод')

all_sklad = []
all_departments = {1: 'Метрология', 2: 'Отдел БТИ', 3: 'Отдел АХО'}
sklad = Sklad('Склад')
aho = Sklad('Отдел АХО')
print(all_departments)
kyocera = Printer('Kyocera', 340, 23, 'шт', 'черный тонер')
sklad.take(kyocera)
hp = Printer('HP', 670, 2, 'шт', 'с автоподатчиком')
sklad.take(hp)

while True:
	Sklad.func_print()
	enter = input('Для выхода из программы нажмите "Q", для продолжения выберите действие: ')
	if enter.upper() == 'Q':
		break
	elif enter == '1':
		print('*' * 50)
		print(f"1 - Добавить Принтер на склад\n2 - Добавить Сканер на склад\n3 - Добавить Ксерокс на склад")
		step1 = input('Для выхода из программы нажмите "Q", для продолжения выберите действие: ')
		if step1.upper() == 'Q':
			break
		elif step1 == '1':
			new_printer = sklad.define_attr(Printer)
			sklad.check_contain(new_printer)
			continue
		elif step1 == '2':
			new_scanner = sklad.define_attr(Scanner)
			sklad.check_contain(new_scanner)
			continue
		elif step1 == '3':
			new_xerox = sklad.define_attr(Xerox)
			sklad.check_contain(new_xerox)
			continue
	elif enter == '2':
		sklad.sklad_contain()
		step3 = input('Для выхода из программы нажмите "Q". Введите номер элемента, '
					  'который хотите переместить со склада: ')
		if step3.upper() == 'Q':
			break
		elif step3.isdigit():
			step5 = input('Для выхода из программы нажмите "Q". '
						  f'Куда вы хотите переместить товар: {all_departments}: ')
			if step5.upper() == 'Q':
				break
			elif step5 == '1':
				metrol = Sklad(all_departments[1])
				all_sklad.append(all_departments[1])
				sklad.move_product(int(step3), metrol)
			elif step5 == '2':
				bti = Sklad(all_departments[2])
				all_sklad.append(all_departments[2])
				sklad.move_product(int(step3), bti)
			elif step5 == '3':
				aho = Sklad(all_departments[3])
				all_sklad.append(all_departments[3])
				print(all_sklad)
				sklad.move_product(int(step3), aho)
			#sklad.move_product(int(step3), aho)
		continue
	elif enter == '3':
		sklad.sklad_contain()
		step2 = input('Для выхода из программы нажмите "Q". Введите номер элемента, который хотите удалить со склада: ')
		if step2.upper() == 'Q':
			break
		elif step2.isdigit():
			sklad.delete_product(int(step2))
		continue
	elif enter == "4":
		print(all_departments)
		sklad.sklad_contain()
	elif enter == "5":
		metrol.sklad_contain()
	elif enter == '6':
		metrol.sklad_contain()
		step4 = input('Для выхода из программы нажмите "Q". Введите номер элемента, '
					  'который хотите переместить: ')
		if step4.upper() == 'Q':
			break
		elif step4.isdigit():
			metrol.move_product(int(step4), sklad)
		continue
	elif enter == "7":
		bti.sklad_contain()
	elif enter == '8':
		bti.sklad_contain()
		step4 = input('Для выхода из программы нажмите "Q". Введите номер элемента, '
					  'который хотите переместить: ')
		if step4.upper() == 'Q':
			break
		elif step4.isdigit():
			bti.move_product(int(step4), sklad)
		continue
	elif enter == "9":
		aho.sklad_contain()
	elif enter == '10':
		aho.sklad_contain()
		step4 = input('Для выхода из программы нажмите "Q". Введите номер элемента, '
					  'который хотите переместить: ')
		if step4.upper() == 'Q':
			break
		elif step4.isdigit():
			aho.move_product(int(step4), sklad)
		continue
