def f_div(x1, x2):
	try:
		return x1 / x2
	except ArithmeticError:
		return 0

while True:
	num1 = input("Введите число num1: ")
	try:
		num1 = int(num1)
		break
	except ValueError:
		print("Вы должны ввести число!")

while True:
	num2 = input("Введите число num2: ")
	try:
		num2 = int(num2)
		break
	except ValueError:
		print("Вы должны ввести число!")

print(f"Результат: {f_div(num1, num2)}")
