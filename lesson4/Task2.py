my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

print([el for el in my_list[1:] if my_list[my_list.index(el)] > my_list[my_list.index(el) - 1]])
