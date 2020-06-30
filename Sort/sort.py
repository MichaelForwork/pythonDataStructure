#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   sort.py
@Time    :   2020/06/25 18:39:08
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    集成一些排序算法
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-

# 预计时间：3天
#  冒泡排序 / 选择排序 /  插入排序 / 希尔排序 / 快速排序 / 归并排序 / 桶排序 / 堆排序

def bubble(array:list)->None :
    """
    如果list是无序的序列，则一定存在至少一对元素彼此之间是存在一种逆序关系的，只需要把list中所有逆序对给扭转即可实现sorted-list;
    如果在一遍扫描中发生任何反转说明已经有序，不需要再迭代
    O（n^）
    稳定性强"""
    length = len(array)
    bias = 0
    flag = False            # 判断list 是否存在逆序对
    while not flag:
        for j in range(1,length-bias):
            if array[j-1] > array[j]:
                array[j-1],array[j] = array[j],array[j-1]
                flag = True
        bias += 1
        flag = not flag 

def selectionSort(array:list)->None:
    """有点像冒泡排序的逆过程；
    每次假设min_index 是当前循环的起始位置,在遍历list中如果有比min_index元素还小的存在，则修改min_index;
    选择环节复杂度很高，交换（插入）环节复杂度很低；
    O(n^2)复杂度
    稳定性低"""
    length = len(array)
    for i in range(length-1):           # 0~n-1
        minIndex = i
        for j in range(i+1,length):         # 1~n find minIndex in unsorted-list
            if array[minIndex] > array[j]:
                minIndex = j
        if i != minIndex:
            array[minIndex],array[i] = array[i],array[minIndex]

def insert(array:list,item,index:int,end:int)->None:
    """
    arrary: list that you want to change \n
    item: element that you want to insert \n
    index: index of the element \n
    end: index of the array"""
    while end > index :             # move emelents back by one step
        array[end] = array[end-1]
        end -= 1
    array[index] = item


def inserationSort(array:list)->None:
    """
    每次从后面unsorted-list 中选择第一个元素插入到前面的有序列表中，point向后移动一位；选择复杂度不高，难在插入部分；
    时间复杂度：
    稳定性"""
    if not isinstance(array,list):
        raise ValueError("input must be a list!")
    
    lengthOfArray = len(array)
    for i in range(1,lengthOfArray):            # 1~n select 
        j = i-1
        while j >= 0:                           # 0~n-1 insert 
            if array[i] > array[j]:
                insert(array,array[i],j+1,i)
                break
            j -= 1


def binaryInserationSort(arrary:list)->None:
    """todo
    每次从后面unsorted-list 中选择第一个元素插入到前面的有序列表中，point向后移动一位；选择复杂度不高，难在插入部分； 
    每次都用二分查找sorted-list 的每个元素进行比较"""
    pass

def mergeSort(parameter_list):
    """todo 
    稳定性高，时间复杂度高 merge 的过程时间复杂度是n, 二分divise的过程复杂度是log n
    """
    pass  

if __name__ == "__main__":
    li = [1,3,4543,546,34232,2342,23424,234]
    #selectionSort(li)
    bubble(li)
    for i in range(len(li)) :
        print("current time",i,li[i])