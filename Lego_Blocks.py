#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#
def subset_sum(numbers, target, partial=[], partial_sum=0):

    # check if the partial sum is equals to target
    if partial_sum == target: 
        yield partial
    if partial_sum > target:
        return # if we reach the number why bother to continue
    
    for i in range(len(numbers)):
        n = numbers[i]
        yield from subset_sum(numbers, target, partial + [n], partial_sum + n) 

def legoBlocks(n, m):
    # Write your code here
    
    block_type = [1,2,3]

    elements_list = []
    for item in (subset_sum(block_type,m)):
        elements_list.append(item)

    #print(elements_list)
    
    element_valid_map = {}

    for index ,item in enumerate(elements_list):
        item_list = []
        for item1 in elements_list:
            partial_sum = 0
            
            if item1 == item:
                continue
            
            is_valid = True
            
            for item_element_index in range(len(item)):
                
                if  item_element_index < len(item1):
                    
                    if partial_sum + item[item_element_index] == partial_sum + item1[item_element_index]:
                        is_valid = False
                        break
                    else:
                        partial_sum += item[item_element_index]  
                else:
                    break   
            
            if is_valid:
                item_list.append(item1)
                
                
        element_valid_map[index] = item_list 
    
    
    all_combinations_sum = sum([len(element_valid_map[index]) for index in range (len(elements_list))])

    result = len(elements_list)
    
    result += all_combinations_sum * n
    
    
    return(result % ((10**7) +3))
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
