#!/usr/bin/python

# Merge sort
# Sort the items in given using merge sort technique
# Breakdown the list in to single item lists and merge them back up while sorting 
# the elements in each stage
# (Divide & Conquer)
# Time: O(n*log n)
# Space: O(n)


def merge_sort(given_list):
    """Divide the list in to one item lists and merge them back in to one while sorting.

    :param given_list: Given unsorted list
    :returns: Sorted list
    """
    llen = len(given_list)
    # If list consists of only one item or no items then just return it
    if llen <= 1:
        return given_list

    # Find the middle point and divide it
    m = llen//2
    ll = given_list[:m]
    rl = given_list[m:]

    ll = merge_sort(ll)
    rl = merge_sort(rl)

    return merge(ll, rl)

def merge(ll, rl):
    """Merge given two lists while sorting the items in them together

    :param ll: List one (left list)
    :param rl: List two (right list)
    :returns: Sorted, merged list
    """
    res = []
    while len(ll) != 0 and len(rl) != 0:
        if ll[0] < rl[0]:
            res.append(ll.pop(0))
        else:
            res.append(rl.pop(0))
    if ll:
        res = res + ll
    if rl:
        res = res + rl
    return res

if __name__ == "__main__":
    print(merge_sort([9,3,1,4,2]))
    print(merge_sort([5,10,7,8,6]))

        
