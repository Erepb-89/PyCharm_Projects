from functools import reduce

with open("out_file_6.txt", "r", encoding='utf-8') as in_f:
	my_list = []
	my_dict = dict()
	line = list(in_f.readline().split())
	print(line)
	summ = 0
	for i in line:
		my_list.append(i.split('('))

	for el in my_list[1:]:
		summ += int(el[0])
	print(summ)
	my_dict[str(my_list[0])] = summ

print(my_dict)
