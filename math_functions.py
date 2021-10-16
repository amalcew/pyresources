def median(array):
    sorted_array = sorted(array)
    index = (len(array) - 1) // 2
    if len(array) % 2:
        return sorted_array[index]
    else:
        return (sorted_array[index] + sorted_array[index + 1])/2.0


def greatest_common_divisor(a, b):
    if b > a:
        return greatest_common_divisor(b, a)
    r = a % b
    if r == 0:
        return b
    return greatest_common_divisor(r, b)


def greatest_common_divisor_recursion(a, b):
    # using Euclid's algorithm
    if b == 0:
        return a
    else:
        return greatest_common_divisor_recursion(b, a % b)


def gcd_for_list(lst):
    max_divisor = lst[0]
    for x in lst[1:]:
        max_divisor = greatest_common_divisor(max_divisor, x)
    return max_divisor


def number_converter(system_before, system_after, number):
    number_after, i = 0, 0
    while number != 0:
        index = number % system_after
        number_after = number_after + index * pow(system_before, i)
        number = number // system_after
        i += 1
    return number_after


def dec_to_hex_converter(number):
    hex_str = ''
    digits = "0123456789ABCDEF"
    if number == 0:
        return '0'
    while number != 0:
        hex_str += digits[number % 16]
        number = number // 16
    return hex_str[::-1]


def is_prime(number):
    num = number
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def permutation(n):
    if n == 0:
        return 1
    else:
        return n * permutation(n-1)


def k_permutation(n, k):
    # wariacja bez powtórzeń
    if n >= k:
        return int(permutation(n)/permutation(n-k))


def combination(n, k):
    if n >= k:
        result = permutation(n)/(permutation(k)*permutation(n-k))
        return int(result)


def stirling_2(n, k):
    """ Recursive function calculating Stirling numbers of the second kind """
    if k > n:
        return None
    if n == k:
        return 1
    if k == 0:
        return 0
    else:
        return stirling_2(n-1, k-1) + k * stirling_2(n-1, k)
