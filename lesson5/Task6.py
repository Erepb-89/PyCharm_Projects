with open("out_file_6.txt", "r", encoding='utf-8') as in_f:
	my_dict = {}
	my_str = '0123456789'
	for line in in_f:
		key, val = line.split(":")
		my_sum = sum(map(int, "".join([i for i in val if i == ' ' or (i in my_str)]).split()))
		my_dict[key] = my_sum

print(my_dict)
