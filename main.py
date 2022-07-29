#https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#



def nonDivisibleSubset(k, s):
    max_subset = 0
    for i in range(len(s)-1):
        divisible_count = s[i] % k
        count = 0
        for j in range(i+1, len(s)):
            if (divisible_count + s[j] % k) % k:
                divisible_count += s[j] % k
                count += 1
        if divisible_count % k != 0:
            if count > max_subset:
                max_subset = count

    print(max_subset)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(4%3)

    print(nonDivisibleSubset(4, [19,10,12,24,25,22]))

# 278,576,496,727,410,124,338,149,209,702,282,718,771,575,436