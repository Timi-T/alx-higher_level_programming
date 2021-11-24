#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    a = sum(n for n in new_list)
    return a
