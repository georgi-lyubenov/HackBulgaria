def count_words(arr):
    def helper(count_elem, str):
        count = 0
        for i in str:
            if i == count_elem:
                count += 1
        return count
    diction = {}
    for i in arr:
        diction[i] = helper(i, arr)
    return diction
#print(count_words(["apple", "banana", "apple", "pie"]))


def unique_words_count(arr):
    count = 0

    def helper(elem, lst):
        for i in lst:
            if i == elem:
                return True
        return False
    arr2 = []
    for i in arr:
        if (helper(i, arr2) is False):
            count += 1
            arr2.append(i)
    return count
#print(unique_words_count(["apple", "banana", "apple", "pie"]))


def groupby(func, seq):
    result = {}
    for item in seq:
        key = func(item)
        if key in result:
            result[key].append(item)
        else:
            result[key] = [item]
    return result
#print(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10, 12])


def prepare_meal(number):
    max = 0
    result = ""
    for i in range(1, number):
        if number % (3 ** i) == 0:
            result += ("spam ")
            if i > max:
                max = i
    if number % 5 == 0:
        result += "and eggs "
    return result
#print(prepare_meal(15))


def reduce_file_path(path):
    result = ""
    for i in path:
        result += i
        if path[i + 1] == '/' or path[i] == '.':
            result -= i
        if path[i] == '.' and path[i + 1] == '.':
            while path[i - 1] != '/':
                result -= path[i]
        if path[len[path] - 1] == '/':
            result -= path[i]
    return result
#not working


def is_an_bn(word):
    counter = 0
    i = 0
    while word[i] == 'a':
        counter += 1
        i += 1
    while word[i] == 'b' and i < len(word) - 1:
        counter -= 1
        i += 1
    if counter == 1:
        return True
    return False
#print(is_an_bn("aabbaabb"))


def simplify_fraction(fraction):
    def find_gcd(x, y):
        while y != 0:
            (x, y) = (y, x % y)
        return x
    return (fraction[0] // find_gcd(fraction[0], fraction[1]), fraction[1] // find_gcd(fraction[0], fraction[1]))
#print (simplify_fraction((63, 462)))


def nth_fib_lists(listA, listB, n):
    if n == 1:
        return listA
    if n == 2:
        return listB
    return listA + listB
print(nth_fib_lists([], [1, 2, 3], 4))

