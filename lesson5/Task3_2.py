from functools import reduce

summ = 0
with open("out_file_3.txt", "r", encoding='utf-8') as out_f:
	print(f"Список сотрудников с зп ниже $20000.0: {[line.split()[0] for line in out_f if float(line.split()[1]) < 20000.0]}")

with open("out_file_3.txt", "r", encoding='utf-8') as out_f:

	print(f"Средняя зп, $: {(reduce(lambda summ, y: summ + y, [float(y.split()[1]) for y in out_f]) / 10)}")
