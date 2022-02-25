#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    
    for index_i  in range(1,n):
        
        index_p = index_i -1
        
        while arr[index_i] < arr[index_p] and index_p >= 0:
            index_p -=1
        
        if index_p < index_i -1:
            
            aux = arr[index_i]
            
            for index_j in range(index_i, index_p, -1):
            
               arr[index_j] = arr[index_j -1]
                       
            arr[index_p+1] = aux
       
        print(' '.join(map(str, arr)))               
         
            
def insertionSort2_simpler_version(n, arr):
    # Write your code here
    
    for index_i in range(1,n):
        aux = arr[index_i]
        
        index_p = index_i -1
        
        while aux < arr[index_p] and index_p >= 0:
            arr[index_p +1] = arr[index_p]
            index_p -=1
        
        arr[index_p +1] = aux
       
        print(' '.join(map(str, arr)))               
         
        

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
