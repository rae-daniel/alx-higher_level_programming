#!/usr/bin/python3
""" Module that contains a function that reads from a file """


def read_file(filename=""):
    """Reads a file and prints to stdout.

    Args:
        filename (str, optional): name of file to read. Defaults to "".
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
