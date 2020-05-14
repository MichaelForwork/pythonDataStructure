#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   doublelink.py
@Time    :   2020/05/08 22:46:06
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    编辑双向链表的所有功能
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-
import classtest

class doubleNode(object):
    """ADT: double link node """
    def __init__(self,item:int):
        self.__head = None
        self.__tail = None    
        self.__data = item

class doubleLink(classtest.Singlelink):
    
    def printdata(self):
        cursor = self._head
        while cursor is not None:
            print(cursor.__data,end=" ")
            cursor = cursor.__tail 
            return 0

    def addFromHead(self,item:int):
        
        if self.isempty():
            self._head = doubleNode(item)
            return 0
        else:
            new_node = doubleNode(item)
            self._head.__head = new_node
            new_node.__tail = self._head
            self._head = new_node
        return 0
    
    def append(self,item:int):
        
        if self.isempty(): 
            self._head = doubleNode(item)
            return 0
        else:
            cursor = self._head
            while not cursor.__tail is None:
                cursor = cursor.__tail
            new_node = doubleNode(item)
            new_node.__head = cursor
            cursor.__tail = new_node
            return 0    
    
    def insert(self, position:int, item:int):
        "insert behind the position;position=offset-1"
        if not isinstance(item,int):
            raise ValueError("inouttype error!")
        if position <= 0:
            self.addFromHead(item)  
            return 0
        if position >= self.length():
            self.append(item)
            return 0
        cursor = self._head
        count = 0
        while count <= position-1:
            cursor = cursor.__tail
            count += 1
        new_node = doubleNode(item)
        new_node.__tail = cursor.__tail
        new_node.__head = cursor
        cursor.__tail = new_node
        new_node.__tail.__head = new_node
        return 0

    def delete(self,position:int):
        
        pass
    