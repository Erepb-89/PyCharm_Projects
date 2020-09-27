# Калькулятор
while True:
	a = float(input("Введите число a: "))
	b = float(input("Введите число b: "))
	c = input("Введите операцию (+, -, *, /, //, %. **, для выхода введите 'q' ")
	if c == "q":
		break
	elif c == "+":
		print(a + b)
	elif c == "-":
		print(a - b)
	elif c == "*":
		print(a * b)
	elif c == "/":
		print(a / b)
	elif c == "**":
		print(a ** b)
	elif c == "//":
		print(a // b)
	elif c == "%":
		print(a % b)
	else:
		print("Введите операцию из списка доступных")
		input("Введите операцию (+, -, *, /, //, %. **, для выхода введите 'q' ")

print("end")