my_list = [0, 1, 'f', 3, 4, 5, 6, "e"]
new_list = []
print(f"Исходный список: {my_list}")

while True:
	phrase = input("Введите следующий элемент списка. Для выхода и "
		"печати итоговых списков нажмите q ")
	if phrase == 'q':
		break
	else:
		my_list.append(phrase)

ind_count = 0
for item in my_list[:]:
	if ind_count % 2 == 0:
		new_list.insert(ind_count, item)
		ind_count += 1
	elif ind_count % 2 == 1:
		new_list.insert((ind_count - 1), item)
		ind_count += 1

print(f"Старый список:		{my_list}")
print(f"Измененный список:  {new_list}")
