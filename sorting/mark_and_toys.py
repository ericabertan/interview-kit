#!/bin/python3

import math
import os
import random
import re
import sys

  # Timsort - nlogn
def cheapSorting(prices):
  return sorted(prices)

# Insertion Sort - n^2
def xpensiveSorting(prices):
    size = len(prices)
    for i in range(1, size):                
        pivot = prices[i]
        j = i - 1
        while(j > 0 and pivot < prices[j]):
            prices[j+1] = prices[j]
            j -= 1
        prices[j+1] = pivot
    
    return prices


def maximumToys(prices, k):
    totalCash = 0
    countToys = 0

    orderedPrices = cheapSorting(prices)

    for unit in orderedPrices:
        if unit + totalCash <= k:
            totalCash += unit
            countToys += 1

    return countToys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
