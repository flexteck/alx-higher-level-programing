#!/usr/bin/python3
def read_file(filename=""):
    """
    read a file and prints it to standard output
        Arg: 
            filename: the file to be read

        return: void

    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
