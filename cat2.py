import sys


def my_cat(filename):
    f1 = open(filename, "r")
    content = f1.read()
    print(content)
    f1.close()


def my_cat2(args):
    for i in args:
        print(my_cat(i))


def main():
    my_cat2(sys.argv[1:])
if __name__ == '__main__':
    main()
