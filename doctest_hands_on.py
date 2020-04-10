#!/bin/python3

import math
import os
import random
import re
import sys
import inspect



# Complete the following isPalindrome function:
def isPalindrome(x):
    # Write the doctests:
    """
    >>> isPalindrome(121)
    True
    >>> isPalindrome(344)
    False
    >>> isPalindrome(-121)
    Traceback (most recent call last):
    ValueError: x must be a positive integer
    >>> isPalindrome("hello")
    Traceback (most recent call last):
    TypeError: x must be an integer
    """
    # Write the functionality:
    t, n = x, 0
    while t > 0:
        n, t = (n * 10 + t%10), t//10
    return n == x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = input()
    
    if x.isdigit():
        x = int(x)

    res = isPalindrome(x)
    
    doc = inspect.getdoc(isPalindrome)
    
    func_count = len(re.findall(r'isPalindrome', doc))
    true_count = len(re.findall(r'True', doc))
    false_count = len(re.findall(r'False', doc))
    pp_count = len(re.findall(r'>>>', doc))
    trace_count = len(re.findall(r'Traceback', doc))

    fptr.write(str(res)+'\n')
    fptr.write(str(func_count)+'\n')
    fptr.write(str(true_count)+'\n')
    fptr.write(str(false_count)+'\n')
    fptr.write(str(pp_count) + '\n')
    fptr.write(str(trace_count) + '\n')

    fptr.close()

