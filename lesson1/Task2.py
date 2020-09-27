time_sec = int(input("Введите время в секундах: "))

hours = time_sec // 3600
minutes = (time_sec % 3600) // 60
seconds = (time_sec % 3600) % 60

result = str(f"{hours}:{minutes}:{seconds}")
print(result)