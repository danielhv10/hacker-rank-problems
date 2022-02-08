#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    for index in range(len(s)//2):
        
        if s[index] != s[len(s) -1 -index]:
            
            if s[index +1: len(s) -index] == s[len(s) -1 -index: index: -1]:
                return index
            else:
                return len(s) -1 -index
            
    return -1
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
