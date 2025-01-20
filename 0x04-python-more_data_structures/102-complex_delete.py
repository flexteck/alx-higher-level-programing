#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys= list(a_dictionary.keys())
    i = 0

    while i < len(keys):
        key = keys[i]
        if a_dictionary[key] == value:
            del a_dictionary[key]
            keys = list(a_dictionary.keys())
        else:
            i +=1

    return a_dictionary
