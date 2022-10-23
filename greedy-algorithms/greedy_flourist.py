#!/bin/python3

import math
import os
import random
import re
import sys

def getMinimumCost(k, c):
  reverseC = sorted(c, reverse=True)
  fm = 1
  resultado = 0
  i = 0 # i + k

  while i < len(c):
    valores = c[i:i+k]
    resultado += fm * sum(valores)
    fm += 1
    i += k

  return resultado


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)
    print(minimumCost)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
