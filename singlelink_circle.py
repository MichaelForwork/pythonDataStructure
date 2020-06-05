#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   singlelink_circle.py
@Time    :   2020/05/15 22:34:29
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    single link with circle strucutre // 
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-
import inspect
import singleLink as ct

class SingleLinkCircleNode(object):
    
    def __init__(self,data = None):
        self.__next = None  # circle 
        self.__data = data
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self,value:int ):
        self.__data = value
        return 0

    @property
    def next(self, ):
        return self.__next  

    @next.setter
    def next(self,value):
        self.__next = value
        return 0

class SingleSinkCircle(ct.Singlelink):

    
    def __init__(self,node = None):
        self.__head = node
        if node:    # 
            self.__head.next = self.__head
        
    def isempty(self, ):
        return self.__head == None

    def length(self, )->int:
        """get length"""
        if self.isempty():
            return 0
        count = 1
        cursor = self.__head
        while cursor.next != self.__head:
            count += 1
            cursor = cursor.next
        return count 

    def printdata(self,):

        if self.isempty():
            print("is empty!")
            return

        cursor = self.__head
        while cursor.next != self.__head:
            print('data: ',cursor.data)
            cursor = cursor.next
        print('data: ',cursor.data)
        return 

    def addFromHead(self,item:int):
        """需要更改尾部节点的next指向，"""
        if self.isempty():
            new_node = SingleLinkCircleNode(item)
            self.__head = new_node
            new_node.next = self.__head
        return

        new_node = SingleLinkCircleNode(item)
        new_node.next = self.__head
        self.__head = new_node
        """需要遍历到结尾，把结尾节点的next 指向新节点"""
        cursor = self.__head
        while cursor.next != new_node.next: # 注意这里的判断条件
            cursor = cursor.next
        cursor.next = self.__head
        return

    def append(self,item:int):
        """难度要略微低于addfromhead"""

        if self.isempty():
            new_node = SingleLinkCircleNode(item)
            self.__head = new_node
            new_node.next = self.__head
        
        cursor = self.__head
        while cursor.next != self.__head:
            cursor = cursor.next
        new_node = SingleLinkCircleNode(item)
        cursor.next = new_node
        new_node.next = self.__head
        return

    def insert(self,position:int,item:int):
        """ insert behind the position ; 和非循环单链表是一样的, offset=position-1"""
        if isinstance(item,int):
            raise ValueError("type of input must be int!")
        if (position-1) <= 0:
            self.addFromHead(item)
        if position >= self.length:
            self.append(item)
        count = 0
        cursor = self.__head
        while count < (position-1):
            cursor = cursor.next
        new_node = SingleLinkCircleNode(item)
        new_node.next = cursor.next
        cursor.next = new_node
        return             
        
    def deleteByItem(self,item:int):
        pass

    def deleteByPosition(self,position:int):
        pass

    def Search(self,item:int):
        
        if isinstance(item,int):
            raise ValueError("type of input must be int!")
        cursor = self.__head
        
        while 