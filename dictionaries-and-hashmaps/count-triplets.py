#!/bin/python3

import math
import os
import random
import re
import sys

# O(n3) - bad solution
def countTriplets(arr, r):
    size = len(arr)
    tripletsCount = 0

    for i in range(0, size):
        for j in range(i+1, size):
            for k in range(j+1, size):
                if (arr[i] * r == arr[j]) and (arr[j] * r == arr[k]):
                    #   print(i, j, k)
                    tripletsCount += 1

    return tripletsCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
