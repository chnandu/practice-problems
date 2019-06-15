#!/usr/bin/python

# reverse_a_string.py
# Reverses given string without using any built-in functions and prints the
# result to stdout

from collections import deque

def reverse_string(str_):
    """Reverses given string without using any built-in functions

    :param str_: Given string
    """
    def reverse_chars(s):
        char_queue = deque()
        for ch in s:
            char_queue.append(ch)
        while char_queue:
            yield char_queue.pop()
    return "".join(reverse_chars(str_))

def main(given_str):
    print(reverse_string(given_str))

if __name__ == "__main__":
    input_str = raw_input("Enter a string: ").strip()
    main(input_str)
