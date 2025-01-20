#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or None:
        return 0

    roman_numrl = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000,
            }

    length = len(roman_string)
    total = 0

    for i in range(length):
        if i < length - 1 and roman_numrl[roman_string[i]] <\
                roman_numrl[roman_string[i+1]]:
                    total -= roman_numrl[roman_string[i]]
        else:
            total += roman_numrl[roman_string[i]]


    return total
