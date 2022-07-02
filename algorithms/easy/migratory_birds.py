#https://www.hackerrank.com/challenges/migratory-birds/problem?isFullScreen=true

import math
import os
import random
import re
import sys
import numpy as np
from collections import OrderedDict

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    dictionary = OrderedDict()
    for index in range(0,9):
        dictionary[index] = 0

    for element in arr:
        if element in dictionary:
            dictionary[element] += 1

    return max(dictionary, key=dictionary.get)