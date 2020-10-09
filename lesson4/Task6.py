# Вариант без break
from itertools import count
from itertools import cycle

el = 3
new_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

while el <= 10:
    if el in count(3):
        print(el)
        el += 1

print(new_list)

i = 0
iter = cycle(new_list)
while i < len(new_list):
    print(next(iter))
    i += 1
