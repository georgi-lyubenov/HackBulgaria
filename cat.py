import sys


def my_cat(filename):
    f1 = open(filename, "r")
    content = f1.read()
    print(content)
    f1.close()


def main():
    my_cat(sys.argv[1])
if __name__ == '__main__':
    main()
