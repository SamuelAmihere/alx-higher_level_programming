#!/usr/bin/python3
"""A module for read_file function"""


def read_file(filename=""):
    """Reads a file to print its contents"""
    if filename:
        with open("filename", 'r') as f:
            print(f.read())
