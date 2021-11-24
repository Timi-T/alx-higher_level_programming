#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    new_list = [replace if num == search else num for num in new_list]
    return new_list
