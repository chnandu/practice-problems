#/usr/bin/python

# Bubblesort
# Bubble the max to the end of the list every pass
#
# Time: O(n^2)
# Average case: O(n^2)
# Best case - O(n) - when implemented a condition to see if all items are in order/nothing to swap

def bubblesort(input_list):
    """Sort the given list using bubblesort method.

    :param input_list: Given list
    """
    ln = len(input_list)
    # Set pivot point to end of the list and reduce it one by one until 0
    # Loop through the list from start to pivot point,
    # compare each item with its previous item and swap if necessary
    for i in range(ln-1, 0, -1):
        for idx in range(i):
            if input_list[idx] > input_list[idx + 1]:
                tmp = input_list[idx]
                input_list[idx] = input_list[idx + 1]
                input_list[idx + 1] = tmp

if __name__ == "__main__":
    input_str = raw_input("Enter comma separated numbers: ").strip()
    given_list = map(lambda x: int(x.strip()), input_str.split(','))
    bubblesort(given_list)
    print(given_list)
