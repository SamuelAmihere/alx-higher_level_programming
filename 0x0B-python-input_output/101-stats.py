#!/usr/bin/python3
"""A module that computes metrics
by reading from standard input.

Prints the following metrics after every ten lines or the
input of a keyboard interruption (CTRL + C):
    Total file size up to that point.
    Total Count of read status codes up to that point.
"""


import sys

total_file_size = 0
status_counts = {}

try:
    for i, line in enumerate(sys.stdin):
        data = line.split()
        if len(data) < 2:
            continue
        status_code = data[-2]
        file_size = int(data[-1])

        total_file_size += file_size

        status_counts[status_code] = status_counts.get(status_code, 0) + 1

        if i % 10 == 0:
            print(f"File size: {total_file_size}")
            for code in sorted(status_counts):
                print(f"{code}: {status_counts[code]}")

except KeyboardInterrupt:
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts):
        print(f"{code}: {status_counts[code]}")
