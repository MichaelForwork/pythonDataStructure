#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   singlelink_circle.py
@Time    :   2020/05/15 22:34:29
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    实现单向循环链表的基本功能 // 
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
        """特殊情况：
        1 空链表
        2 需要更改尾部节点的next指向，"""
        if self.isempty():
            new_node = SingleLinkCircleNode(item)
            self.__head = new_node
            new_node.next = self.__head
            return      
        
        """方法1 ： 需要首先遍历到结尾，把结尾节点的next 指向新节点；
        方法2 ： 如果是先添加节点再遍历，那么cursor的起点就不应该从self.head开始"""
        # cursor = self.__head
        # while cursor.next != self.__head: # 注意这里的判断条件
        #     cursor = cursor.next
        # new_node = SingleLinkCircleNode(item)
        # cursor.next = new_node
        # new_node.next = self.__head
        # self.__head = new_node
        # return
        new_node = SingleLinkCircleNode(item)
        new_node.next = self.__head
        self.__head = new_node
        cursor = new_node.next
        while cursor.next is not new_node.next:
            cursor = cursor.next
        cursor.next = new_node
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
        if not isinstance(item,int):
            raise ValueError("type of input must be int!")
        if (position-1) <= 0:
            self.addFromHead(item)
            return
        if position >= self.length():
            self.append(item)
            return
        count = 0
        cursor = self.__head
        while count < (position-1):
            cursor = cursor.next
            count += 1
        new_node = SingleLinkCircleNode(item)
        new_node.next = cursor.next
        cursor.next = new_node
        return             
        
    def delete(self,item:int):
        """默认使用deleteByItem"""
        self.deleteByItem(item)
        return

    def deleteByItem(self,item:int):
        """链表的删除需要双指针;
        特殊情况有3：
        1 链表只有一个节点
        2 删除头节点
        3 删除尾部节点"""
        if self.isempty():
            return
        
        cursor = self.__head
        preCursor = None
        # while 没有考虑删除尾部节点的情况
        while cursor.next is not self.__head:   
            # 2 最复杂情况，需要更改尾部节点的指向
            if cursor.data == item and self.__head == cursor:
                cursor4Tail = cursor
                while cursor4Tail.next is not self.__head:
                    cursor4Tail = cursor4Tail.next
                self.__head = cursor.next
                cursor4Tail.next = self.__head
                return 
            # 常规删除
            elif cursor.data == item:
                preCursor.next = cursor.next
                return
            else:
                preCursor = cursor
                cursor = cursor.next
        # 1
        if cursor.data == item and self.length==1:
            self.__head = None
            return
        # 3 
        if cursor.data == item and cursor.next == self.__head:
            preCursor.next = cursor.next
            cursor.next = None  #释放资源? 
        return 

    def deleteByPosition(self,position:int):
        
        pass

    def Search(self,item:int):
        
        if isinstance(item,int):
            raise ValueError("type of input must be int!")
        cursor = self.__head
        
        pass