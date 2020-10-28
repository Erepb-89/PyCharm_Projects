def real_type(x, i=False):
	real = str(x) if x > 0 or x < 0 else ''
	if i == True:
		if x > 0:
			real = f"+{real}i"
		elif x < 0:
			real = real + 'i'
	return real


class ComplexOperations:
	"""Комплексные числа"""

	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2
		self.my_list = []

	def __add__(self, other):
		sum = real_type(self.num1 + other.num1) + real_type(self.num2 + other.num2, True)
		if sum == '':
			sum = '0i'
		return sum

	def __mul__(self, other):
		el1 = real_type(self.num1 * other.num1 - self.num2 * other.num2)
		el2 = real_type(self.num2 * other.num1 + self.num1 * other.num2, True)

		mul = el1 + el2
		if mul == '':
			mul = '0i'
		return mul

	def __str__(self):
		return real_type(self.num1) + real_type(self.num2, True)

number1 = ComplexOperations(-1, 2)
number2 = ComplexOperations(5, -1)

print(number1 + number2)
print(number1 * number2)
