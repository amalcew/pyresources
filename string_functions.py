# Module with various utilities to help with string manipulations
def palindrome(word):
    if str(word) == reverse_word(word):
        print("palindrome = true")
    else:
        print("palindrome = false")


def reverse_word(string):
    reversed_word = ''
    index = len(string)
    while index:
        index -= 1
        reversed_word += string[index]
    return reversed_word


def slice_left(string, slice_length):
    word_left = ''
    while slice_length:
        slice_length -= 1
        word_left += string[slice_length]
    return reverse_word(word_left)


def slice_right(string, slice_length):
    word_right = ''
    while slice_length:
        slice_length -= 1
        word_right += string[-slice_length - 1]
    return word_right


def replace_letter(string, character_number):
    mod = list(string)
    mod[character_number - 1] = '*'
    after_mod = "".join(mod)
    return after_mod
