num = int(input("Введите число n: "))

result = int(num + int(str(f"{num}{num}")) + int(str(f"{num}{num}{num}")))

print(result)