from googletrans import Translator
translator = Translator()

with open("out_file_4.txt", "r", encoding='utf-8') as out_f:

	for line in out_f:
		result = translator.translate(line, dest='ru')
		print(result.text)

		with open("new_file.txt", "a", encoding='utf-8') as new_f:
			new_f.write(f"{result.text}\n")
