def fact(n):
    for el in range(1, n + 1):
        yield el

g = fact(4)
num = 1

for el in g:
    num *= el

print(num)

# рекурсия

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)

print(fact(4))
