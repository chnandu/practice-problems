#!/usr/bin/python

# Check if given string has all unique characters or not

def check_uniqueness(str_):
    """Check if given string has all unique characters and return True

    :param str_: Given string
    :returns: True, if all characters are unique. Else, False.
    """
    char_dict = {}
    for c in str_:
        if char_dict.get(c) is None:
            char_dict[c] = 1
        else:
            print("Duplicate character: %s" % c)
            return False
    return True

if __name__ == "__main__":
    inputs = ["abcdfhefef", "abcdefgh", "1234", "foo"]
    for i in inputs:
        print("%s --> %s" % (i, check_uniqueness(i)))
