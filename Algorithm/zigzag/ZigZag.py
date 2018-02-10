#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 09:59:01 2018

@author: wangzhuoyao
"""
from timeit import timeit

def convert1(s, numRows):
    """
        :type s: str
        :type numRows: int
        :rtype: str
    """
    ans = ""
    a = {}
    for i in range(numRows):
        a[i] = ""
    
    if numRows >1: 
        for i, x in enumerate(s):
            ind1 = i // (numRows - 1)
            ind2 = i % (numRows-1)
            
            if ind1 % 2 == 0: #the ind11 is odd,the straight line
                a[ind2] += x
            else:#the ind1 is even ,the zigziag line
                a[numRows - ind2 -1] += x    
            
        for i in range(numRows):
            ans += a[i]
    else:
        ans = s
        
    return ans

def convert2(s, numRows):
    """
        :type s: str
        :type numRows: int
        :rtype: str
    """
    if numRows == 1:
        return s
    
    a = [''] * numRows
    index = 0 
    step = 1
    
    for x in s:
        a[index] += x
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step
        
    ans = ''.join(a)

    return ans


def main(s, numRows):

    ans1 = timeit('convert1(s, numRows)','from __main__ import convert1, s, numRows')
    ans2 = timeit('convert2(s, numRows)','from __main__ import convert2, s, numRows')
    print(ans1, ans2)
    #if ans1 == ans2:
     #   print(ans1)
    #else:
    #    print('error, the two answers are different!')
            
if __name__ == '__main__':
    s = "l;qjcopjdoaf;loqwnc"
    numRows = 3
    main(s,numRows)
        