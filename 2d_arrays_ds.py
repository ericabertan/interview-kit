#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    
    i = 1
    greatestSum = -9999999
    
    while i < 5:
        j = 1
        while j < 5:
            _sum = arr[i-1][j-1] + \
                    arr[i-1][j] + \
                    arr[i-1][j+1] + \
                    arr[i][j] + \
                    arr[i+1][j-1] + \
                    arr[i+1][j] + \
                    arr[i+1][j+1]
            
            if _sum > greatestSum:
                greatestSum = _sum       
            
            j += 1
        
        i += 1
    
    return greatestSum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
