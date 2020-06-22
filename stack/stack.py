#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stack.py
@Time    :   2020/06/21 23:38:37
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    测试栈的基本功能  last in first out LIFO 栈可以使用顺序表来实现 
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-
import numpy

class Stack(object):

    def __init__(self, parameter_list=None):
       self.__list =[]  # private list 

    def push(self,item:int):
        '''
        insert an item onto the stack
        '''
        
        self.__list.append(item)    # 尾部添加的时间复杂度是 O 1

    def peek(self,):
        if self.__list:
            return self.__list[-1]
        else:
            return None
            

    def size(self, ):
        return len(self.__list)

    def pop(self, ):
        pop = self.__list[-1]
        self.__list = self.__list[:-1]
        return pop

    def isEmpty(self, parameter_list=None):
        return self.__list==[]  # [] "" 0 {} () == None
