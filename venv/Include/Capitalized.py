#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    r = s.split(' ')
    for i in range(len(r)):
         r[i] = r[i].capitalize()
    p = ' '.join(r)
    return p



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    #fptr.write(result + '\n')

    #fptr.close()
