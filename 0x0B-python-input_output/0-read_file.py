#!/usr/bin/python3
"""This module contains a function to read a file"""


def read_file(filename=""):
    """This function reads a txt file and prints to stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
