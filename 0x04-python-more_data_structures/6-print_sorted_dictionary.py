#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    key_list = sorted(a_dictionary)
    for i in range(len(key_list)):
        print("{:s}: ".format(key_list[i]), end='')
        print(a_dictionary[key_list[i]])
    return
