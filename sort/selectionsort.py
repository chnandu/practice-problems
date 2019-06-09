# Selection sort
# Select minimum element of the list and bring it to the front of the list
#
# Time: O(n^2) Best
#    Avr/Worst: O(n^2)
# Space = O(1)

def selectionsort(input_list):
    """Sorts given list using selection sort technique

    :param input_list: Given input list
    """
    for idx in range(len(input_list)):
        min_idx = idx
        for j in range(idx+1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]

if __name__ == "__main__":
     list_= [34,23,45,23,67,23,4,1,9,3]
     selectionsort(list_)
     print(list_)
     list_ = [1,2,3,4,5,6]
     selectionsort(list_)
     print(list_)
