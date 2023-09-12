#!/usr/bin/python3
""" Function append_write """


def append_write(filename="", text=""):
    """ Function appends 'filename' with 'text' """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
