my_list = []
itogo = 0

while True:
	my_list = input("Введите числа через пробелы, введите 'q' для выхода: ").split()
	try:
		summa = 0
		for item in my_list:
			if item != 'q':
				summa = summa + int(item)
			elif item == 'q':
				break
		print(f"Промежуточная сумма равна: {summa}")
	except ValueError:
		print("Вы должны ввести число")
	else:
		itogo = itogo + summa
		print(f"Общая сумма равна: {itogo}")
		if item == 'q':
			break
