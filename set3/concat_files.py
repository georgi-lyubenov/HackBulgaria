import sys


def concat_files(args):
    f1 = open("MEGATRON.txt", "a")
    for i in args:
        temp = open(i, "r")
        content = temp.read()
        f1.write(content)
        f1.write('\n')
        temp.close()
        content = ""
    f1.write("\n")
    f1.close()


def main():
    concat_files(sys.argv[1:])
if __name__ == '__main__':
    main()
