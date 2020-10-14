count_lines = 0
count_words = 0

with open("out_file_2.txt", "r", encoding='utf-8') as out_f:
	for line in out_f:
		count_words = 0
		count_lines += 1

		for i in line.split():
			count_words += 1
		print(f"Слов в {count_lines} строке: {count_words}")
print(f"Всего строк: {count_lines}")
