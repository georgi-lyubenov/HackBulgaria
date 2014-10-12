import sys


def count_chars(filename):
    count = 0
    f1 = open(filename, "r")
    for i in f1:
        for j in i:
            count += 1
    f1.close()
    return count


def count_words(filename):
    count = 0
    f1 = open(filename, "r")
    for i in f1:
        for j in i:
            if j in [' ', '!', '?', '-', '...']:
                count += 1
    f1.close()
    return count


def count_lines(filename):
    f1 = open(filename, "r")
    count = len(f1.readlines())
    f1.close()
    return count


def wc(command, filename):
    if command == 'chars':
        print(count_chars(filename))
    elif command == 'words':
        print(count_words(filename))
    elif command == 'lines':
        print(count_lines(filename))
    else:
        print ("invalid input")


def main():
    wc(sys.argv[1], sys.argv[2])
if __name__ == '__main__':
    main()
