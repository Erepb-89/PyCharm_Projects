my_list = []
count = int(input("Введите количество товаров: "))
my_dict = {
    "название" : None,
    "цена" : None,
    "количество" : None,
    "eд" : None,
    }
new_dict = {
    "название" : None,
    "цена" : [],
    "количество" : [],
    "eд" : [],
    }
name_list = []
cost_list = []
number_list = []
unit_list = []

i = count
while i > 0:
    print(f"Введите товар номер {i}")
    for key, val in my_dict.items():
        val = input(f"Введите {key}: ")
        my_dict[key] = val

    name_list.append(my_dict["название"])
    cost_list.append(my_dict["цена"])
    number_list.append(my_dict["количество"])
    unit_list.append(my_dict["eд"])

    my_tuple = (i, my_dict.copy())
    my_list.append(my_tuple)
    i -= 1

new_dict["название"] = list(set(name_list))
new_dict["цена"] = list(set(cost_list))
new_dict["количество"] = list(set(number_list))
new_dict["eд"] = list(set(unit_list))

my_list.reverse()
for item in my_list:
    print(item)

print("Выборка:")
for item in new_dict.items():
    print(item)