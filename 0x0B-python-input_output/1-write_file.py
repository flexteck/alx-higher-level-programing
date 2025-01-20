#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    writes a string to a text file
        Arg: 
            filename: the file to be read

        return: void

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
