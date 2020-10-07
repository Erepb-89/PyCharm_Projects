def my_func(x, y):
	step = 1
	try:
		while y > 0:
			step = step * x
			y -= 1
		result = 1 / step
		return round(result, 8)
		# return 1 / (x ** abs(y))
	except ArithmeticError:
		return 0

while True:
	num1 = input("Введите число num1: ")
	try:
		num1 = float(num1)
		abs(num1)
		break
	except ValueError:
		print("Вы должны ввести число!")

while True:
	num2 = input("Введите степень числа, она будет инвертирована в отрицательную: ")
	try:
		num2 = int(num2)
		print(abs(num1))
		print(f"В степени -{num2}")
		break
	except ValueError:
		print("Вы должны ввести число!")

print(f"Результат: {my_func(num1, num2)}")
