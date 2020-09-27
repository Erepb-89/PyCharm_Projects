plus = float(input("Введите значение выручки: "))
minus = float(input("Введите значение издержек: "))

if plus < minus:
	print(f"Фирма сработала в убыток: -{minus - plus}")
elif plus == minus:
	print(f"Фирма сработала в ноль.")
else:
	print(f"Поздравляем! Фирма сработала в прибыль: +{plus - minus}")
	print(f"Рентабельность: {(plus - minus) / plus}")
	empl = int(input("Введите количество сотрудников: "))
	print(f"Прибыль фирмы в расчете на одного сотрудника: {(plus - minus) / empl}")