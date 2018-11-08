#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    rowCount = 0
    dSum1 = 0
    dSum2 = 0
    rowLen = len(arr[0])
    for i in range(n):
        dSum1 += arr[i][rowCount]
        rowCount +=1

    for _ in range(n):
        dSum2 += arr[_][rowLen-1]
        rowLen -=1
    return (abs(dSum1 - dSum2))


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))
    print(diagonalDifference(arr))
