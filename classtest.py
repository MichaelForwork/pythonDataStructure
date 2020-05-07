#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   wappper.py
@Time    :   2020/04/30 23:04:22
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    实现 class 的基本功能
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-
import inspect


class node(object):
    """ 链表内部节点"""

    def __init__(self, data):
    
        self._data = data
        self._next = None


class Singlelink(object):
    """ 单链表 """    
    def __init__(self,node=None):
        """"""
        self._head = node

    def isempty(self,):

        return self._head == None

    def printdata(self, ):
        "不要擅自改动link head"
        cursor = self._head
        while not cursor == None:
            print (cursor._data, end=",")
            cursor = cursor._next

    def length(self)->int:

        cur = self._head    
        count = 0
        while not cur == None:
            count += 1 
            cur = cur._next
        return count

    def addFromHead(self, item):

        new_node = node(item)
        new_node._next = self._head
        self._head = new_node
        return 0
                
    def append(self, parameter_list):
        
        if not isinstance(parameter_list, int):
            raise ValueError("input is not a integer !")
        new_node = node(parameter_list)
        cursor = self._head
        if cursor == None:
            self._head = new_node
            new_node._next = None
            return 0

        while not cursor._next == None:
            cursor = cursor._next
        cursor._next = new_node
        new_node._next = None
        return 0

    def insert(self, position:int,item:int):
        cursor = self._head
        count = 0
        if not isinstance(item,int):
            raise ValueError("input is not integer !")
        if position <=0:    # 头部插入
            self.addFromHead(item)
            return 0
        if position >= (self.length()):
            self.append(item)
            return 0
        while count < position-1:
            cursor = cursor._next
            count += 1

        new_node = node(item)
        new_node._next = cursor._next 
        cursor._next = new_node
        return 0 
        
        pass






class CCC(object):

    data = None 
    
    def __init__(self,data:int ):
        self.data = data
        



class cccobj(CCC):

    def __init__(self, parameter_list):
        self.name = parameter_list


    @property
    def birth(self):
        return self.birth

    @birth.setter
    def birth(self, parameter_list):
        if not isinstance(parameter_list, int):
            raise ValueError("input type must be int!")
        else:
            self.birth = parameter_list
