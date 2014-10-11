import sys
from random import randint


def generate_numbers(filename, n):
    f1 = open(filename, "w")
    for i in range(int(n)):
        f1.write(str(randint(1, 10)))
        f1.write(" ")
    f1.close()


def main():
    generate_numbers(sys.argv[1], sys.argv[2])
if __name__ == '__main__':
    main()
