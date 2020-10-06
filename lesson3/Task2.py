#имя, фамилия, год рождения, город проживания, email, телефон
def f_parameters(first_name, second_name, year, city, email, tel):
	my_list = [first_name, second_name, year, city, email, tel]
	print(f"имя: {first_name}, фамилия: {second_name}, год рождения: {year}, "
		  f"город проживания: {city}, email: {email}, телефон: {tel}")

f_parameters("Вася", "Пупкин", "1989", "Ухта", "erepb-89@...", "3-60-95")
