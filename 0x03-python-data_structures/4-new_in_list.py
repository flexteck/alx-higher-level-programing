#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list[:]
    if idx < 0:
        return copy_list
    if idx > (len(my_list) - 1):
        return copy_list

    new_list = my_list[:]
    new_list[idx] = element

    return new_list
