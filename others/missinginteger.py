#!/usr/bin/python

# Find the smallest positive integer that is not present in given list
# For example:
#   [0, 1, 4] => 2
#   [-1, -2] => 1
#   [2, 3, 4, 5] => 1
#   [-10000000, 10000000] => 1

def solution(A):
    # write your code in Python 3.6
    # Remove the duplicates
    print(A)
    uniq_set = set()
    
    # First check if all negative numbers in which case it can return 1.
    # Also remove negative numbers because they are not helpful
    positive_nums = False
    for i in A:
        if i > 0:
            positive_nums = True
            uniq_set.add(i)
    
    # if there are no positive numbers, return 1
    if not positive_nums:
        return 1
    
    # There are positive numbers, let's sort the list
    sorted_list = sorted(uniq_set)
    # Set the index to first elem in the list and loop over the entire
    # list to find the first 
    index = sorted_list[0]
    start = 0
    end = len(sorted_list)

    # Special case where if 1 itself is missing then we can just return it
    if sorted_list[0] != 0 and sorted_list[0] != 1:
        return 1

    while start < end:
        if sorted_list[start] != index:
            break
        index += 1
        start += 1
    return index

if __name__ == "__main__":
    print(solution([0, 1,2, 4, 5,5, 9]))
    print(solution([0]))
    print(solution([-1, 0, -2, -3]))
    print(solution([-1, -2, -4, -5]))
    print(solution([-1000000, 1000000]))
    print(solution([2,5,9]))
    print(solution([9]))
