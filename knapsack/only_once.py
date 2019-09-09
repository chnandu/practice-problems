#!/usr/bin/python

# Knapsack problem - items should be added only once

def knapsack(w, n, vals, wts):
    """Find the maximum value possible using n weights up to 'w' -- include weight only once

    :param w: Given weight
    :param n: Number of weights/values
    :param vals: List of values of n items
    :param wts: List of weights of n items
    :returns: Maximum value possible
    """
    if w == 0 or n == 0:
        return 0

    if wts[n-1] > w:
        return knapsack(w, n-1, vals, wts)
    else:
        return max(vals[n-1] + knapsack(w-wts[n-1], n-1, vals, wts), knapsack(w, n-1, vals, wts))

if __name__ == "__main__":
    wts =  [3,2,5,6,7,9,1]
    vals = [3,1,4,5,4,5,7]
    w = 20
    print(knapsack(w, len(wts), vals, wts))    
