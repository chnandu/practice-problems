#!/usr/bin/python

# Given two strings, check if one is permutation of another
#
# 1) Sort both the strings and compare each other, both must be equal
# 2) Parse one string and create a map of character and its occurrances.
#    Then parse second string and knock off each char from the map.
#    At the end if the map is empty then one is permutation of another.
#    (Can use collections.Counter to build the char map but here I am doing it myself)

def is_permutation(str1, str2):
    """Check if given strings are permutation of each other

    :param str1: String one
    :param str2: String two
    :returns: True/False accordingly
    """
    # Very first check is to see if they both are equal so we can return True quickly
    if str1 == str2:
        return True

    # We can also check if they both of same length and return True if not.
    if len(str1) != len(str2):
        return False

    # Can also use defaultdict with default value = 0
    char_map = {}
    for c in str1:
        if char_map.get(c) is not None:
            char_map[c] += 1
        else:
            char_map[c] = 1

    for c in str2:
        res = char_map.get(c, 0)
        if res == 0:
            return False
        elif res == 1:
            del(char_map[c])
        else:
            char_map[c] -= 1

    if len(char_map) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    print("(foo, foo) --> %s" % is_permutation("foo", "foo"))
    print("(abc, cba) --> %s" % is_permutation("abc", "cba"))
    print("(abcd, cddd) --> %s" % is_permutation("abcd", "cddd"))
    print("(abcd, abcde) --> %s" % is_permutation("abcd", "abcde"))

