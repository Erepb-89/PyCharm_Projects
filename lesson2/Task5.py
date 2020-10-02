my_list = [7, 6, 5, 4, 3, 3, 2]
new_list = my_list[:]
#num = 3
print(my_list)
num = int(input("Введите целое число: "))

while True:
	if num not in my_list and num > my_list[0]:
		new_list.insert(0, num)
		print(f"Индекс нового элемента: {new_list.index(num)}]")
		break
	elif num in my_list:
		list_index = new_list.index(num)
		if my_list.count(num) >= 1:
			counts = my_list.count(num)
			while counts:
				list_index = list_index + 1
				counts -= 1
		print(f"Индекс нового элемента: {list_index}")
		new_list.insert(list_index, num)
		break
	elif num not in my_list and num < my_list[-1]:
		new_list.append(num)
		print(f"Индекс нового элемента: {new_list.index(num)}]")
		break

print(new_list)