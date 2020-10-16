with open("out_file_3.txt", "r", encoding='utf-8') as out_f:
	low_list = []
	summ = 0
	zp = 20000.0
	count_lines = 0
	for line in out_f:
		count_lines += 1
		print(line.rstrip())
		if float(line.split()[1]) < zp:
			low_list.append(line.split()[0])
		summ += float(line.split()[1])
	print(f"Список сотрудников с зп ниже ${zp}: {low_list}")
	print(f"Средняя зп, $: {round((summ / count_lines), 2)}")
