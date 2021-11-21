#!/usr/bin/python3
import sys
len_of_args = len(sys.argv) - 1
total = 0
if __name__ == "__main__":
    for i in range(1, len_of_args + 1):
        total += int(sys.argv[i])
    print("{:d}".format(total))
