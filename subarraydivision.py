#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#
def birthday(s, d, m):
    # Write your code here
    bars=0
    for i in range(0,len(s)):
        sum=0
        count=0
        for j in range(i,len(s)):
            sum+=s[j]
            count=count+1
            if sum==d and count==m:
                bars=bars+1
    return(bars) 

if __name__ == '__main__':


    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)
    print(result)