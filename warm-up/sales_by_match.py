#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    i = 0;
    number_of_pairs = 0
    while i < n:
        j = i + 1

        if ar[i] != -1:
            while j < n:
                if ar[i] == ar[j]:
                    number_of_pairs += 1
                    ar[i] = -1
                    ar[j] = -1
                    break
                else:
                    j += 1
        i += 1
    
    return number_of_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
