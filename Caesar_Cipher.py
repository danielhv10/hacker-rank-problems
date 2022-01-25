#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#



def caesarCipher(s, k):
    # Write your code here
    
    original_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rotated = {}
    
    for index, char in enumerate(original_alphabet):

        alphabet_rotated[char] = original_alphabet[int((index + k) % len(original_alphabet))]
        alphabet_rotated[char.upper()] = original_alphabet[int((index + k) % len(original_alphabet))].upper()
        
    
    ciphered_string = ''.join([alphabet_rotated[char] if char in alphabet_rotated else char for char in s])
    
    return ciphered_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
