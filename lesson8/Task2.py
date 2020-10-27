import traceback

class OwnError(Exception):
	def __init__(self, txt):
		self.txt = txt

inp_data1 = input("Введите число: ")
inp_data2 = input("Введите число: ")

try:
	inp_data1 = float(inp_data1)
	inp_data2 = float(inp_data2)
	res = inp_data1 / inp_data2
	if inp_data2 == 0:
		raise OwnError("Вы ввели 0! На 0 делить нельзя")
except (ZeroDivisionError, OwnError) as err:
	print(err)
else:
	print(f"Все хорошо. Ваш результат: {round(res, 2)}")
