#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    score_total = 0
    weight = 0

    for i in my_list:
        j_mul = 1
        for j in i:
            j_mul *= j
        score_total += j_mul
        weight += j

    return score_total/weight
