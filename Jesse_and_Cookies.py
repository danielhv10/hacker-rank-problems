#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    
    num_operations = 0
    heapq.heapify(A)
    
    cookie1 = heapq.heappop(A)
    while cookie1 < k:
        
        if(len(A) == 0):
            return -1
        else: 
            cookie2 = heapq.heappop(A)
            heapq.heappush(A, cookie1 + (cookie2 * 2))
            num_operations +=1
            cookie1 = heapq.heappop(A)

    return num_operations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
