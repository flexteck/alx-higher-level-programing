#!/usr/bin/python3
def multiple_returns(sentence):
    length= len(sentence)

    if length == 0: 
        return tuple([length, None])
    else:
        return tuple([length, sentence[0]])

