#!/usr/bin/python3
""" printst a text with 2 new lines after each of these
    characters: ., ? and :
"""

def text_indentation(text):
    """
    Arg:
        text(string)

    Return:
        nothing

    Raise:
        raise TypeError is text not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text[:]

    for i in ".?:":
        list_text = s.split(i)
        s = ""

        for ch in list_text:
            ch = ch.strip(" ")
            s = ch + i if s == "" else s + "\n\n" + ch + i

    print(s[:-3],end="")
