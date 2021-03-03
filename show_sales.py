import sys

len_sys_argv = len(sys.argv)

with open("bakery.csv", "r", encoding="UTF-8") as f:
    if len_sys_argv == 1:
        add_sale = f.read()
        print(add_sale)
    else:
        lst_sale = f.readlines()
        if len_sys_argv == 2:
            for line in lst_sale[int(sys.argv[1]) - 1:]:
                print(line.strip().replace('\n', ''))
        else:
            for line in lst_sale[int(sys.argv[1]) - 1:int(sys.argv[2])]:
                print(line.strip().replace('\n', ''))
