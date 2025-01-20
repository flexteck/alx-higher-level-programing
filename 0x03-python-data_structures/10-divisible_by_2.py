#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bol = []

    for i in range(len(my_list)):
        if i % 2 == 0:
            bol.append(True)
        else:
            bol.append(False)

    return bol
