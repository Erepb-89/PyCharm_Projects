my_dict = {12: 'зима',
            1: 'зима',
            2: 'зима',
            3: 'весна',
            4: 'весна',
            5: 'весна',
            6: 'лето',
            7: 'лето',
            8: 'лето',
            9: 'осень',
            10: 'осень',
            11: 'осень'}

#num = 2
num = input("Введите целое число от 1 до 12, обозначающее месяц: ")

while num < '0':
    print("Введенное число должно быть положительным")
    num = input("Введите целое положительное число: ")

if int(num) in list(my_dict.keys()):
    print(f"Сезон: {my_dict.get(int(num))}")

