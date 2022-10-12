#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(n, c):
    jumpRec = []
    i = 0
    
    jumpRec.append(i)
    while i < n - 1:
            
        if i < n - 2 and c[i + 1] == 0 and c[i + 2] == 0:
            jumpRec.append(i + 2)
            i += 2
        
        elif c[i + 1] == 0:
            jumpRec.append(i + 1) 
            i += 1
        
        else:
            jumpRec.append(i + 2)
            i += 2
            
    return len(jumpRec) - 1
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
