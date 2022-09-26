#!/bin/python3

import math
import os
import random
import re
import sys

def is_array_sorted(arr):
    for i in range(0, len(arr)):
        if arr[i] != i+1:
            return False
    return True

    
def minimumSwaps(arr, n):
    numberSwaps = 0

    while not is_array_sorted(arr):
        for i in range(0, len(arr)):

            # If it's equal, the number is in the right position
            if arr[i] != i+1:
                # If the number is big, then we position at the end
                j = arr[i] - 1

                # When i is smaller than j, it means arr[i] probably has to go to one of 
                # the last positions in the vector
                if i < j and arr[i] > arr[j]:
                    aux = arr[i]
                    arr[i] = arr[j]
                    arr[j] = aux

                    numberSwaps += 1
                # When i is greater than j, it means arr[i] has to go to one of the firsts positions
                # in the vector
                elif i > j and arr[i] < arr[j]:
                    aux = arr[i]
                    arr[i] = arr[j]
                    arr[j] = aux
                    
                    numberSwaps += 1
    
    return numberSwaps
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr, n)

    fptr.write(str(res) + '\n')

    fptr.close()
