#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
	a = len(my_list)
	if idx < 0:
		return None
	if idx > a:
		return my_list
	for i in range(a):
		if idx == i:
			my_list[i] = element
	return my_list
