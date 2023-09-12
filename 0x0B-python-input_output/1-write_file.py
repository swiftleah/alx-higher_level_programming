#!/usr/bin/python3
""" write_file function """


def write_file(filename="", text=""):
    """ Define function
    Args: filename & text
    text is written to file """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
