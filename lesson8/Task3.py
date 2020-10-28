import traceback

class OwnError(Exception):
	def __init__(self, txt):
		self.txt = txt

inp_data = ''
res = []
while inp_data != "stop":
	inp_data = input("Для выхода введите 'stop'. Введите число: ")
	if inp_data == "stop":
		print(f"Все хорошо. Ваш результат: {res}")
		break
	try:
		if not inp_data.isdigit():
			raise OwnError("Вы ввели не число")
		res.append(int(inp_data))
	except (TypeError, OwnError) as err:
		print(err)
