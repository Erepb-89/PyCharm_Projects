import json

with open("out_file_77.json", "w", encoding='utf-8') as wr_f:
    with open("out_file_7.txt", "r", encoding='utf-8') as in_f:
        summary_list = []
        count_dict = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in in_f}
        print(count_dict)
        plus_dict = {key: val for key, val in count_dict.items() if val > 0}
        summary_list = [plus_dict,
                        {"average": sum(plus_dict.values()) / len(plus_dict.values())},
                        {key: val for key, val in count_dict.items() if val < 0},
                        ]
        print(summary_list)

    json.dump(summary_list, wr_f, ensure_ascii=False, indent=4)
