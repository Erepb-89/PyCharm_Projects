num = int(input("Введите целое положительное число n: "))
big_num = 0

while num > 0:
	next_num = num % 10
	if next_num > big_num:
		big_num = next_num
	num = num // 10

print(f"Наибольшее число из введенных: {big_num}")
