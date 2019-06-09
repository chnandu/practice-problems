#!/usr/bin/python

# Quicksort
# Quicksort sorts the list by choosing a random pivot point and sort the lists 
# before and after that point individually until entire list is sorted.
# Time: O(n^2) (Worst)
#   Avg/Best: O(n*logn)
# Space: O(1)
#   Worst: (n*log n)

def swap(list_, id1, id2):
    """Swap the items in positions id1 & id2 in given list

    :param list_: Given list
    :param id1: Index of one item
    :param id2: Index of another item
    """
    tmp = list_[id1]
    list_[id1] = list_[id2]
    list_[id2] = tmp


def quicksort(given_list):
    """Pick a random pivot point and sort the lists before and after that point

    :param given_list: Given input list
    :returns: Sorted list
    """
    last = len(given_list) - 1
    pivot = last
    i = 0
    if last <= 0:
        return given_list

    if last == 1:
        if given_list[0] > given_list[1]:
            swap(given_list, 0, 1)
        return given_list

    while i < pivot:
        if given_list[i] > given_list[pivot]:
            if i == pivot - 1:
                swap(given_list, i, pivot)
            else:
                tmp = given_list[pivot - 1]
                given_list[pivot - 1] = given_list[pivot]
                given_list[pivot] = given_list[i]
                given_list[i] = tmp
            pivot -= 1
        else:
            i += 1

    ll = quicksort(given_list[:pivot])
    rl = quicksort(given_list[pivot+1:])
    ll.append(given_list[pivot])
    return ll + rl

if __name__ == "__main__":
    print(quicksort([5,2,7,1,9,3,8,6,4]))
    print(quicksort([56,13, 467, 23, 46, 1, 12, 23, 45]))
