def nth_fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return nth_fibonacci(n-1)+nth_fibonacci(n-2)
#print (nth_fibonacci(5))


def sum_of_digits(n):
    if n < 0:
        sum_of_digits(-n)
    result = 0

    while (n > 10):
        last_digit = n % 10
        result += last_digit
        n = n//10
    return result + n
#print (sum_of_digits(1325132435356))


def sum_of_devisors(n):
    result = 0
    for i in range(1, n):
        if (n % i) == 0:
            result += i
    return result + n
#print(sum_of_devisors(1000))


def is_prime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True
#print (is_prime(8))


def prime_number_of_devisors(n):

    def helper(n):
        number_of_devisors = 0
        for i in range(1, n):
            if (n % i) == 0:
                number_of_devisors += 1
        return number_of_devisors
    if is_prime(helper(n)):
        return True
    return False
#print (prime_number_of_devisors(7))


def sevens_in_a_row(arr, n):
    counter = 0
    for i in range(0, len(arr) - 1):
        if (arr[i] == arr[i+1]):
            counter += 1
            if (counter == n):
                return True
        else:
            counter = 0
    return False
#print (sevens_in_a_row([7, 7, 7, 1, 1, 1, 7, 7, 7, 7], 3))


def is_int_palindrom(n):
    temp = n
    p = 0
    while (temp):
        p *= 10
        p += (temp % 10)
        temp = temp // 10
    if (n == p):
        return True
    else:
        return False
#print (is_int_palindrom(4224))


def contains_digit(number, digit):
    while (number > 0):
        if (number % 10) == digit:
            return True
        else:
            number = number // 10
    return False
#print (contains_digit(1000, 1))


def contains_digits(number, digits):
    for i in digits:
        if (contains_digit(number, i) is False):
            return False
    return True
#print (contains_digits(402123, [0, 3, 4]))


def is_number_balanced(n):
    import math
    if n < 10:
        return True
    count1 = 0
    count2 = 0
    arr = []
    while (n > 0):
        arr.append(n % 10)
        n = n // 10
    arr.reverse()
    length_of_arr = len(arr) - 1
    mid = length_of_arr / 2
    for i in range(0, math.floor(mid) + 1):
        count1 += arr[i]
    for i in range(math.ceil(mid), length_of_arr + 1):
        count2 += arr[i]
    if (count1 == count2):
        return True
    else:
        return False
#print (is_number_balanced(1238033))

#def count_substrings(haystack, needle):


def count_vowels(str):
    count = 0

    def is_vowel(c):
        if (c == "a" or
                c == "e" or c == "i" or c == "o" or c == "u" or c == "y"):
            return True
        return False
    for i in str:
        if is_vowel(i):
            count += 1
    return count
#print (count_vowels("Theistareykjarbunga"))


def number_to_list(n):
    arr = []
    while (n > 0):
        arr.append(n % 10)
        n = n // 10
    arr.reverse()
    return arr
#print(number_to_list(12435423))


def list_to_number(digits):
    number = digits[0]
    i = 1
    while (i < len(digits)):
        number = number * 10 + digits[i]
        i += 1
    return number
#print(list_to_number([1, 2, 3, 4]))


def biggest_difference(arr):
    min = 0

    def helper(num, arr):
        min = 0
        for i in arr:
            if num - i < min:
                min = num - i
        return min
    for i in arr:
        if helper(i, arr) < min:
            min = helper(i, arr)
    return min
#print(biggest_difference((range(100))))


def increasing_sequence(seq):
    for i in range(0, len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            return False
    return True
#print(increasing_sequence([1, 2, 3, 4, 2]))

#def decreasing_sequence(seq):


def zero_insertion(n):
    arr = number_to_list(n)
    for i in range(0, len(arr) - 1):
        if arr[i] == arr[i + 1] or (arr[i] + arr[i + 1]) % 10 == 0:
            print("ok")
            arr.insert(i, 0)
    return list_to_number(arr)
#print(zero_insertion(116457))
