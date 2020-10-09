from functools import reduce
# в одну строку
print(reduce(lambda el_before, el: el_before * el, [el for el in range(100, 1001) if el % 2 == 0]))

# классический вариант
my_list = [el for el in range(100, 1001) if el % 2 == 0]

def f_mult(el_before, el):
    return el_before * el

print(reduce(f_mult, my_list))
