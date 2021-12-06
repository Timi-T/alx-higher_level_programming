#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    a = 0
    new_list = []
    while (list_length != 0):
        try:
            a = my_list_1[i] / my_list_2[i]
            new_list.append(a)
        except TypeError:
            print("{:s}".format('wrong type'))
            new_list.append(0)
        except ZeroDivisionError:
            print("{:s}".format('division by 0'))
            new_list.append(0)
        except IndexError:
            print("{:s}".format('out of range'))
            new_list.append(0)
        finally:
            i = i + 1
            list_length = list_length - 1
    return new_list
