with open("out_file.txt", "a", encoding='utf-8') as out_f:
	i = input('Введите и нажмите Enter: \n')
	out_f.write(f"{i}\n")
	while i != '':
		i = input('Введите и нажмите Enter: \n')
		out_f.write(f"{i}\n")

with open("out_file.txt", "r") as out_f:
	for line in out_f:
		print(line.rstrip())
