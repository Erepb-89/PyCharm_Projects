def my_func(num1, num2, num3):
    my_list = [num1, num2, num3]
    my_list.remove(min(my_list))
    return sum(my_list)

print(f"Результат: {my_func(3, 5, 6)}")
