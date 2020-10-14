from random import randint

with open("out_file_5.txt", "w", encoding='utf-8') as out_f:
	my_str = ''
	my_list = [randint(1, 10) for el in range(10)]
	print(my_list)
	for i in my_list:
		out_f.write(f"{i} ")

summ = 0

with open("out_file_5.txt", "r", encoding='utf-8') as in_f:
	content = in_f.read()
	new_list = content.split()
	for el in new_list:
		summ += int(el)
print(f"Сумма: {summ}")
