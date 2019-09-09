#!/usr/bin/python
#
# Check if given string is a palidrome or not
# -- Start from beginning and end and compare the characters one by one until both ends meet.
# -- If all match then it is palindrome

def is_palindrome(str_):
    """Returns True if given string is palindrome, else False

    :param str_: Given string
    :returns: True if given string is palindrome else False
    """
    start = 0
    end = len(str_) - 1
    while start < end:
        if str_[start] != str_[end]:
            break
        start += 1
        end -= 1
    else:
        return True

    return False

if __name__ == "__main__":
    inputs = ["abc", "ab", "aa", "aaa", "abcdabcd", "carerac", "cattac"]
    for s in inputs:
        print("%s ---> %s" % (s, is_palindrome(s)))

