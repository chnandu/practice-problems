#!/usr/bin/python

# Cut the rod in pieces such that maximum price can be yielded

import sys

def rod_cutting(prices, n):
    """Return the maximum price that can be yielded after cutting the rod in to pieces

    :param prices: List of prices as price at index reflects the price of the rod length of index
    :param n: Length of the rod
    :return: Maximum price to gain
    """
    val = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        max_val = -sys.maxint - 1
        for j in range(i):
            max_val = max(max_val, prices[j]+val[i-j-1])
        val[i] = max_val
    return val[n]

if __name__ == "__main__":
    prices = [2, 5, 1, 3, 4, 6, 2, 9, 5, 10]
    print(rod_cutting(prices, 10))
