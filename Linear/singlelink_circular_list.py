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


class SingleCircularListNode(object):

    def __init__(self, data=None):
        self.__next = None  
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value: int):
        self.__data = value
        return 0

    @property
    def next(self, ):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value
        return 0


class SingleCircularList(object):

    def __init__(self, node=None):
        self.__head = node
        if node:    #
            self.__head.next = self.__head

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self,head):
        self.__head = head 
    
    def isempty(self, )->bool:
        return self.head == None

    def length(self, ) -> int:
        """get length"""
        if self.isempty():
            return 0
        count = 0
        cursor = self.head
        while cursor.next is not  self.head:
            count += 1
            cursor = cursor.next
        return count+1

    def printdata(self,):

        if self.isempty():
            print("there is empty!")
            return

        cursor = self.head
        while cursor.next != self.head:
            print('data: ', cursor.data)
            cursor = cursor.next
        print('data: ', cursor.data)
        return

    def addFromHead(self, item: int):
        """特殊情况：
        1 空链表
        2 需要更改尾部节点的next指向，"""
        if self.isempty():
            new_node = SingleCircularListNode(item)
            self.head = new_node
            new_node.next = self.head
            return
        new_node = SingleCircularListNode(item)
        cursor = self.head
        while cursor.next is not self.head:
            cursor = cursor.next
        new_node.next = self.head
        self.head = new_node
        cursor.next = self.head
        return

    def append(self, item: int):
        """难度要略微低于addfromhead"""
        if self.isempty():
            self.addFromHead(item)
            return

        cursor = self.head
        while cursor.next != self.head:
            cursor = cursor.next
        new_node = SingleCircularListNode(item)
        cursor.next = new_node
        new_node.next = self.head
        return

    def insert(self, position: int, item: int):
        """ insert behind the position ; 和非循环单链表是一样的, offset=position-1"""
        if not isinstance(item, int):
            raise ValueError("type of input must be int!")
        if (position-1) <= 0:
            self.addFromHead(item)
            return
        if position >= self.length():
            self.append(item)
            return
        count = 0
        cursor = self.head
        while count < (position-1):
            cursor = cursor.next
            count += 1
        new_node = SingleCircularListNode(item)
        new_node.next = cursor.next
        cursor.next = new_node
        return

    def delete(self, item: int):
        """默认使用deleteByItem"""
        self.deleteByItem(item)
        return

    def deleteFromHead(self):
        if self.isempty():
            return 
        else:
            point = self.head
            while point.next is not self.head:
                point = point.next
            self.head = self.head.next
            point.next = self.head
            return

    def deleteFromTail(self):
        if self.isempty():
            return
        else:
            point = self.head
            previous_point = None
            while point.next is not self.head:
                previous_point = point
                point = point.next
            if not previous_point:
                self.head =None
                return
            previous_point.next = self.head
            point.next = None
            return

    def deleteByItem(self, item: int):
        if self.isempty():
            return
        elif self.head.data == item :
                self.deleteFromHead(item)
        else:
            cursor = self.head
            previous_cursor = None
            while cursor.next is not self.head :
                if cursor.data == item :
                    previous_cursor.next = cursor.next
                    cursor.next = None
                previous_cursor = cursor 
                cursor = cursor.next
            if cursor.data == item:
                previous_cursor.next = cursor.next
                cursor.next = None

    def deleteByPosition(self, position: int):
        """根据位置来删除指定元素"""
        if self.isempty():
            return

        if position-1 <= 0:
            # 删除头节点
            self.deleteFromHead()

        if position >= self.length():
            # 删除尾部节点
            self.deleteFromTail()

        # 在中间删除 
        count = 0
        preCursor = None
        cursor = self.head
        while count != position-1:
            preCursor = cursor
            cursor = cursor.next
            count += 1
        preCursor.next = cursor.next
        cursor.next = None
        return

    def search(self, item: int) -> bool:
        if not isinstance(item,int):
            raise ValueError(" input must be an Integer!")
        """根据data查找节点是否存在，并且返回position"""
        if self.isempty():
            print("None,because there is no data.")
            return False

        cursor = self.head
        while cursor.next is not self.head:
            if cursor.data == item:
                return True
            cursor = cursor.next

        if cursor.data == item:
            return True
        else:
            return False
        
        
