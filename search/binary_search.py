#!/usr/bin/python

# Binary search
# Find the middle point and compare the element at middle point with given one.
# If both match then that's the answer.
# Else, find out if the given number if bigger or smaller than the element at middle point.
# And search the left or right part of the list accordingly.

def binary_search(input_list, value):
    s = 0
    e = len(input_list) - 1
    counter = 1
    while s <= e:
        m = (s + e) / 2
        item = input_list[m]
        if item == value:
            return (m, counter)
        elif value > item:
            s = m + 1
        else:
            e = m - 1
        counter += 1
    return (-1, counter)

if __name__ == "__main__":
    in_list = [2,3,5,7,9,10,15,29,30,45,56]
    l = "".join(["---" for _ in range(0, len(in_list))])
    print(l)
    nl = "|"
    for n in in_list:
        nl += "%2s|" % str(n)
    print(nl)
    print(l)
    print("Search %d --- Found at %d, runs %d" % ((1,) + binary_search(in_list, 1)))
    print("Search %d --- Found at %d, runs %d" % ((25,) + binary_search(in_list, 25)))
    print("Search %d --- Found at %d, runs %d" % ((29,) + binary_search(in_list, 29)))
    print("Search %d --- Found at %d, runs %d" % ((10,) + binary_search(in_list, 10)))
    print("Search %d --- Found at %d, runs %d" % ((15,) + binary_search(in_list, 15)))
    print("Search %d --- Found at %d, runs %d" % ((56,) + binary_search(in_list, 56)))
