#!/usr/bin/python

# Given a matrix, find out the maximum of sum of all elements in any possible 
# submatrix(including the entire matrix itself).
# Note: It can contain negative numbers as well so taking the sum of entire 
#       matrix is not the correct answer



#def maxsum(mat):
#    """Returns of maximum of sum of all elements in any possible submatrix
#
#    :param matrix: Given matrix
#    """
#    rows = len(mat)
#    cols = len(mat[0])
#
#    # Start with [0,0] as max sum
#    max_sum = mat[0][0]
#
#    # Generator function returning all points in a matrix
#    def all_points():
#        for i in range(0, rows):
#            for j in range(0, cols):
#                if mat[i][j] > max_sum:
#                    max_sum = mat[i][j]
#                yield (i, j)
#
#    # Start at each point and find out all possible submatrixes from there
#    # Sub-matrixes are 1x1, 2x2, 3x3, ... MxN from each point
#    # 1x1 values are already covered in above generated so we do not have to
#    # check them again.
#    for (r, c) in all_points:
#        
#
#    for i in range(0, len(mat)):
#        for j in range(0, len(mat[0])):
#

def maxsum(mat, start=0, end=0):
    for i in range(start, len(mat)):
        for j n range(start            
