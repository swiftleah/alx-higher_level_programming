#!/usr/bin/python3
""" read_file function """


def read_file(filename=""):
    """ Define function
    reads text in file & prints to stdout """
    with open(filename, encoding='utf-8') as my_file:
        my_file_contents = my_file.read()

    print(my_file_contents, end="")
