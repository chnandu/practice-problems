# Insertion Sort
# Inserts the elements one by one in to its correct place there by sorting the
# entire list

# Time: O(n) Best
#   Avg/Worst: O(n^2)
# Space: O(1)

def insertion_sort(given_list):
    """Sorts the given list using insertion sort technique

    :param given_list: Given input list
    """
    for i in range(1, len(given_list)):
        j = i - 1
        nxt_elem = given_list[i]
        while (given_list[j] > nxt_elem) and (j >= 0):
            given_list[j + 1] = given_list[j]
            j = j - 1
        given_list[j + 1] = nxt_elem

if __name__ == "__main__":
    list_ = [4,3,2,6,23,13,1,5,5]
    insertion_sort(list_)
    print(list_)
    list_ = [23,5,23,1,5,8,78]
    insertion_sort(list_)
    print(list_)

