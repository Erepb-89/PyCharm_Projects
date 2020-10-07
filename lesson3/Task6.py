#        nice авп ъghj jапро hjjпаро вапрghgh cool

def int_func(x):
    my_list = x.split()
    new_list = str()
    all_correct = False
    for el in my_list:
        for item in el:
            if 97 <= ord(item) <= 122:
                pass
            else:
                all_correct = False
                break
            all_correct = True
        if all_correct:
            new_list = new_list + el.title() + ' '
    return new_list

print(int_func(input("Введите слова, разделенные пробелом: ")))
