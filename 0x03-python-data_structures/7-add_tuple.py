#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 1:
        tuple_a = tuple([tuple_a[0], 0])
    elif len(tuple_a) == 0:
        tuple_a = (0,0)

    if len(tuple_b) == 1:
        tuple_b = tuple([tuple_b[0], 0])
    elif len(tuple_b) == 0:
        tuple_b = (0, 0)

    add_t = tuple([i + j for i, j in zip(tuple_a, tuple_b)])
        
    return add_t
