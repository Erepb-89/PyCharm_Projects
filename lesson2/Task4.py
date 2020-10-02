words = input("Введите слова, разделенные пробелами: ").split()

for ind, el in enumerate(words):
    print(ind, el[:10])