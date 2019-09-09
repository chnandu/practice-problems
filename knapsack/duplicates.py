#!/usr/bin/python

# Knapsack problem with duplicate items allowed

def knapsack(w, n, vals, wts):
    """Find the maximum value possible with n weights upto given weight in given list

    Duplicates are allowed
    :param w: Given weight
    :param n: Number of weights
    :param vals: List of values of each weight
    :param wts: List of n weights
    :returns: Return the maximum value
    """
    dp = [0 for _ in range(0, w + 1)]
    for i in range(w + 1):
        for j in range(n):
            if wts[j] <= i:
                dp[i] = max(dp[i], dp[i-wts[j]] + vals[j])
    return dp[w]

if __name__ == "__main__":
    wts =  [3,2,5,6,7,9,1]
    vals = [3,1,4,5,4,5,7]
    w = 20
    print(knapsack(w, len(wts), vals, wts))
