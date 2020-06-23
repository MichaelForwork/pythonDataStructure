#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   singleLink.py
@Time    :   2020/04/30 23:04:22
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    实现 单链表的基本功能
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-
import inspect


class node(object):
    """ 链表内部节点"""

    def __init__(self, data:int):
        if not isinstance(data,int):
            raise ValueError("input must be an Integer!")
        
        self.__data = data
        self.__next = None
        
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self,data:int):
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self,next):
        self.__next = next

class Singlelink(object):
    """ 单链表 """    
    def __init__(self,node=None):
        """"""
        self.__head = node

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self,head):
        self.__head = head

    def isempty(self,)->bool:
        return self.head is None

    def printdata(self, ):
        "不要擅自改动link head"
        cursor = self.head
        while not cursor == None:
            print ("data= ",cursor._data, end=" ")
            cursor = cursor.next

    def length(self)->int:
        cursor = self.head    
        count = 0
        while not cursor == None:
            count +=1
            cursor = cursor.next
        return count

    def addFromHead(self, item:int):        
        new_node = node(item)
        new_node.next = self.head
        self.head = new_node

    def append(self, item:int):
        if self.head == None:
            self.head = node(item)
            return 0
        
        cursor = self.head
        while not cursor.next == None:
            cursor = cursor.next
        cursor._next = node(item)

    def insert(self, position:int,item:int):
        "insert behind the position; position= offset-1"
        if not isinstance(position,int):
            raise ValueError("input is not integer !")
        if position <=0 or self.isempty():    # 头部插入
            self.addFromHead(item)
        elif position >= (self.length()):
            self.append(item)
        else:
            cursor = self.head
            count = 0
            while count < position-1:
                cursor = cursor.next
                count += 1
            new_node = node(item)
            new_node.next = cursor.next 
            cursor.next = new_node
        
    def deleteByItem(self,item:int):
        """ delete your item if it exsits and only delete one time
        ;需要两个cursor,考虑2种特殊情况：1 link 只有1 节点而且就是删除这个节点；
        ;2 link 有多个节点 而且删除头节点; 
        """
        if not isinstance(item,int):
            raise ValueError("input must be an Integer!")
        if self.head == None : 
            return
        elif self.head.data == item :
            self.head = self.head.next
        else:
            cursor = self.head
            another_Cursor = None
            while not cursor == None:
                if cursor.data == item:# 常规删除
                    another_Cursor.next = cursor.next
                    cursor.next = None
                    break
                another_Cursor = cursor
                cursor = cursor.next

    def deleteByPosition(self,position:int):
        if not isinstance(position,int):
            raise ValueError("input must be an Integer!")
        
        if self.head == None:
            return
        if position <1 :
            self.head = self.head.next
        elif position >= self.length():
            cursor = self.head
            another_Cursor = None
            while cursor.next:
                another_Cursor = cursor
                cursor = cursor.next
            another_Cursor.next = None
        else:
            count = 0
            cursor = self.head
            another_Cursor = None
            while count < position-1 :
                another_Cursor = cursor
                cursor = cursor.next
                count += 1
            another_Cursor.next = cursor.next
            cursor.next = None