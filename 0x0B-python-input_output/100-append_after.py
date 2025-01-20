#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text after a search string"""
    with (filename, 'r') as file:
        lines = file.readlines()


    with (filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
