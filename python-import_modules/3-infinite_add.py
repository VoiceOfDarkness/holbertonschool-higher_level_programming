#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    sum = 0
    for num in range(1, len(argv)):
        sum += int(argv[num])
    print("{}".format(sum))
