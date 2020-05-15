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
    # change private attribute 
    def __init__(self,item:int):
        """all attribute are private """
        self.__head = None
        self.__tail = None    
        self.__data = item
        
    def gethead(self):
        return self.__head

    def gettail(self):
        return self.__tail
    
    def getdata(self):
        return self.__data

    def sethead(self, head):
        self.__head = head 
        return 0
    
    def settail(self,tail):
        self.__tail = tail
        return 0

    def setdata(self,data):
        self.__data = data


class doubleLink(classtest.Singlelink):
    """继承来自single link """"
    
    def length(self)->int:

        cursor = self._head
        count = 0
        while cursor is not None:
            count += 1
            cursor = cursor.gettail()
        return count

    def printdata(self):
        cursor = self._head
        while cursor is not None:
            print(cursor.getdata(),end=" ")
            cursor = cursor.gettail() 
        return 0

    def addFromHead(self,item:int):
        
        if self.isempty():
            self._head = doubleNode(item)
            return 0
        else:
            new_node = doubleNode(item)
            self._head.sethead(new_node) 
            new_node.settail(self._head)
            self._head = new_node
        return 0
    
    def append(self,item:int):
        
        if self.isempty(): 
            self._head = doubleNode(item)
            return 0
        else:
            cursor = self._head
            while not cursor.gettail() is None:
                cursor = cursor.gettail()
            new_node = doubleNode(item)
            new_node.sethead(cursor) 
            cursor.settail(new_node)
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
            cursor = cursor.gettail()
            count += 1
        new_node = doubleNode(item)
        new_node.settail(cursor.gettail())  
        new_node.sethead(cursor)
        cursor.settail(new_node)  
        new_node.gettail().sethead(new_node) 
        return 0

    def delete(self,position:int):
        if
        pass
    
