my_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list_seasons = ['зима', 'весна', 'лето', 'осень']
#num = 2
num = input("Введите целое число от 1 до 12, обозначающее месяц: ")

while num < '0':
    print("Введенное число должно быть положительным")
    num = input("Введите целое положительное число: ")

if int(num) in my_list[:3]:
    print(f"Сезон: {list_seasons[0]}")
elif int(num) in my_list[3:6]:
    print(f"Сезон: {list_seasons[1]}")
elif int(num) in my_list[6:9]:
    print(f"Сезон: {list_seasons[2]}")
elif int(num) in my_list[9:]:
    print(f"Сезон: {list_seasons[3]}")

