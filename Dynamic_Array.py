#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here

    last_answr = 0
    get_idx = lambda x,last_answer: ((x ^ last_answer) % n)
    arr = [[] for _ in range(n)]
    last_answer = 0
    result = []
    for item in queries:
        idx = get_idx(item[1], last_answer)
        if item[0] == 1:
            
            arr[idx].append(item[2])
            
        elif item[0] == 2:
            last_answer = arr[idx][item[2] % len(arr[idx])]
            result.append(last_answer)
        else:
            return -1
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
