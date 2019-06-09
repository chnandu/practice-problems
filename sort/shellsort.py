#!/usr/bin/python
# Shellsort
# 
# Shell sort sorts elements far away from each other.
# First start a large subset of a given list and go on reducing the size of the
# list until all elemented are sorted
# 
# Time: O(n log(n)) Best
#   Avg/Worst: O(n (log n)^2)
# Space: O(1)

def shellsort(input_list):
    """Sort the given list using shellsort technique.

    :param input_list: Given list of items
    """
    # Find middle point
    gap = len(input_list) / 2
    while gap > 0:
        for i in range(gap, len(input_list)):
            tmp = input_list[i]
            j = i
            while j >= gap and input_list[j-gap] > tmp:
                input_list[i] = input_list[j-gap]
                j = j - gap
            input_list[j] = tmp
        gap = gap//2

if __name__ == "__main__":
     list_= [34,23,45,23,67,23,4,1,9,3]
     shellsort(list_)
     print(list_)
     list_ = [1,2,3,4,5,6]
     shellsort(list_)
     print(list_)
