#!/usr/bin/python

# URLify -
# Given a string with spaces in it, replace spaces with %20 and return the updated string
# Example: "Mr John Smith", 13 --> Mr%20John%20Smith
#
# Note - length of the string would also be given

def urlify(a_str, a_len):
    """Urlify given string

    :param a_str: Given string
    :param a_len: Length of the string
    """
    num_spaces = 0
    for c in a_str:
        if c == " ":
            num_spaces += 1

    total_len = a_len + num_spaces * 2
    index = total_len
    i = a_len - 1

    # Take a new list of total_len so we can store the result in there as individual chars first
    # At the end convert that in to string and return it
    b_list = [" " for _ in range(total_len)]
    while i >= 0:
        if a_str[i] == " ":
            b_list[index-1] = '0'
            b_list[index-2] = '2'
            b_list[index-3] = '%'
            index = index - 3
        else:
            b_list[index-1] = a_str[i]
            index -= 1
        i -= 1
    return "".join(b_list)

if __name__ == "__main__":
    inputs = ["Mr Test Str", "ABCD DEF", "ABCD ", "FFFFF"]
    for i in inputs:
        print("(%s, %d) ----> %s" % (i, len(i), urlify(i, len(i))))
