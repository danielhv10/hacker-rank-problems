#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import permutations
#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    # Write your code here
    
    min_cost = 9 * 9 + 1
    
    l = list(permutations(range(1, 10)))
    
    for item in l:
        item_list = list(item)
        matrix = [item_list[0:3], item_list[3:6], item_list[6:9]]
        
        if is_solution(matrix):
            current_cost = get_cost(matrix, s)
            if(current_cost < min_cost):
                min_cost = current_cost
                
    return min_cost

def is_solution(matrix):
    
    row1_sum = matrix[0][0] + matrix[0][1] + matrix[0][2]
    row2_sum = matrix[1][0] + matrix[1][1] + matrix[1][2]
    row3_sum = matrix[2][0] + matrix[2][1] + matrix[2][2]
    
    col1_sum = matrix[0][0] + matrix[1][0] + matrix[2][0]
    col2_sum = matrix[0][1] + matrix[1][1] + matrix[2][1]
    col3_sum = matrix[0][2] + matrix[1][2] + matrix[2][2]
    
    diag1_sum = matrix[0][0] + matrix[1][1] + matrix [2][2]
    diag2_sum = matrix[2][0] + matrix [1][1] + matrix[0][2]

    return row1_sum == row2_sum == row3_sum == col1_sum == col2_sum == col3_sum == diag1_sum == diag2_sum

def get_cost(original_matrix, new_matrix):
    
    total_cost = 0
    
    for row in range(len(original_matrix)):
        for column in range(len(original_matrix)):
            total_cost += abs(original_matrix[row][column] - new_matrix[row][column])
    
    return total_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
