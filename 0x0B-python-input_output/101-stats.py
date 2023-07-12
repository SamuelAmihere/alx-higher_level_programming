#!/usr/bin/python3
"""A module that computes metrics
by reading from standard input.

Prints the following metrics after every ten lines or the
input of a keyboard interruption (CTRL + C):
    Total file size up to that point.
    Total Count of read status codes up to that point.
"""


import sys

def print_metrics(total_file_size, valid_codes):
    """Prints the metrics"""
    print("File size: {}".format(total_file_size))
    for key in sorted(valid_codes.keys()):
        if valid_codes[key] > 0:
            print("{}: {}".format(key, valid_codes[key]))

valid_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for line in sys.stdin:
        data = line.split()
        if len(data) > 2:
            status_code = int(data[-2])
            file_size = int(data[-1])
            if status_code in valid_codes:
                valid_codes[status_code] += 1
            print("File size: {}".format(file_size))
            print("Status code: {}".format(status_code))
except KeyboardInterrupt:
    print_metrics(file_size, valid_codes)
    raise
