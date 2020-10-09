from sys import argv

script_name, hours, stavka, prem = argv

print("Имя скрипта: ", script_name)
print("Часы: ", hours)
print("Ставка: ", stavka)
print("Премия в %: ", prem)

try:
	print(round((float(hours) * float(stavka)) + float(prem)/100 * (float(hours) * float(stavka)), 2))
except ValueError:
	print("Вы должны ввести числа")
