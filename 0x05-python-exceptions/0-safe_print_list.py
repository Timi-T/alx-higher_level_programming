#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0;
    i = 0;
    while ((x - 1) != -1):
        try:
            print(my_list[i], end='')
            count = count + 1
            i = i + 1
            x = x - 1
        except Exception:
            break
    print()
    return count
