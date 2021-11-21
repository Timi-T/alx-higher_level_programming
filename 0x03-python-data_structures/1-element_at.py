#!/usr/bin/python3
def element_at(my_list, idx):
    a = len(my_list)
    if idx < 0:
        return None
    if idx > a:
        return None
    for i in range(a):
        if idx == i:
            return my_list[i]
