#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   maxFortowElement.py
@Time    :   2020/07/07 19:37:53
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    find two max elements in the array
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-

def maxfortwoElement(array:list)->tuple:
    """find two max elements in an array 
    """
    LENGTH_ARRAY = len(array)
    if array[0] < array[1]:
        maxIndex1 = 1
        maxIndex2 = 0
    else:
        maxIndex1 = 0
        maxIndex2 = 1
    for i in range(2,LENGTH_ARRAY):
        if array[i] > array[maxIndex2]:
            maxIndex2 = i
            if array[maxIndex2] > array[maxIndex1]:
                maxIndex1,maxIndex2 = maxIndex2,maxIndex1
                
    return array[maxIndex1],array[maxIndex2]


if __name__ == "__main__":
     li = [22334243324,232,213,23,335,2341,12,1214,324234]
     x1, x2 = maxfortwoElement(li,)
     print(x1,x2)
