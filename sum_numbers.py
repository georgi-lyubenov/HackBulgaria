import sys
from types import *


def sum_numbers(filename):
    sum = 0
    f1 = open(filename, "r")
    line = f1.read()
    for i in line.split():
        for j in i:
            sum += int(j)
    return sum
    f1.close()


def main():
    print(sum_numbers(sys.argv[1]))
if __name__ == '__main__':
    main()
