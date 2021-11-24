#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    i = 0
    new_dict = a_dictionary.copy()
    new_list = list(map(lambda y: y * 2, (new_dict[key] for key in new_dict)))
    for key in new_dict:
        new_dict[key] = new_list[i]
        i += 1
    return new_dict
