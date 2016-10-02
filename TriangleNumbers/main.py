######################################################################################################
########################################### ALGORITHM ################################################
######################################################################################################
# 1. On computing the the first few rows of the triangle , we notice a pattern that the first even
#    number is at the position 2, 3, 2, 4, 2, 3, 2, 4, 2, 3, 2, 4..... (starting from row 3). 
#    So basically the position of the first even number repeats after an interval of 4 in the above fashion.
# 2. Use this property to quickly and efficiently find the answer.
######################################################################################################

from types import *

patternArray = [2, 3, 2, 4]

def GetEvenNumberIndex(rowNumber):
    # Default index
    index = 0
    if (rowNumber==0 or rowNumber==1): return index

    index = patternArray[(rowNumber-2)%4]
    return index

if __name__=="__main__":
    # Get input from STDIN
    T = int(raw_input())
    N = []
    for tc in xrange(T): N.append(int(raw_input()))

    # Iterate over the test case list and print the result
    for rowNumber in N: print GetEvenNumberIndex(rowNumber-1)
