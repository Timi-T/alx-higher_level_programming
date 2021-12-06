#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    i = 0;
    count = 0;
    ex = 0;

    while ((x - 1) != -1):
        ex = 0
        ie = 0
        try:
            print("{:d}".format(my_list[i]), end='')
        except IndexError:
            ie = 1
            break
        except Exception:
            ex = 1
        if ex != 1:
            count = count + 1;
        i = i + 1
        x = x - 1
    if ie == 1:
        print("{:d}".format(my_list[i]), end='')
    print()
    return count
