class MyData:

	def __init__(self, data):
		self.data = data

	@classmethod
	def m_1(cls, data):
		new_list = []
		my_list = data.split('-')
		for el in my_list:
			new_list.append(int(el))
		cls.data = new_list
		return cls.data

	@staticmethod
	def m_2(obj):
		res = []
		next_list = []
		next_list = MyData.m_1(obj.data)
		if 1 <= next_list[0] <= 31 and 1 <= next_list[1] <= 12 and 1900 <= next_list[2] <= 2100:
			obj.data = next_list
			return obj.data
		else:
			print('Введите день в диапазоне от 1 до 31, месяц в диапазоне от 1 до 12, год в диапазоне от 1900 до 2100')

	def __str__(self):
		res = self.m_2()
		return f'{res}'

my_data = MyData('03-05-1989')
print(my_data)
print(MyData.m_2(my_data))
