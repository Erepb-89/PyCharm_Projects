from functools import reduce

with open("out_file_6.txt", "r", encoding='utf-8') as in_f:
    my_list = []
    my_dict = dict()
    content = in_f.readline()
    current_list = []
    print(content)
    for line in content.split():
        i = 0
        while i < len(line):
            num = ''
            a = line[i]
            while '0' <= line[i] < '9':
                num += line[i]
                i += 1
                if i < len(line):
                    a = line[i]
                else:
                    break
            i += 1
            if num != '':
                current_list.append(int(num))

    print(current_list)
