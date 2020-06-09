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
import singleLink


class doubleNode(object):
    """ADT: double link node """
    # change private attribute

    def __init__(self, item: int):
        """all attribute are private """
        self.__head = None
        self.__tail = None
        self.__data = item

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, item):
        self.__head = item

    @property
    def tail(self):
        return self.__tail

    @tail.setter
    def tail(self, item):
        self.__tail = item

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, item):
        self.__data = item


class doubleLink(singleLink.Singlelink):
    """继承来自single link """

    def length(self) -> int:

        cursor = self._head
        count = 0
        while cursor is not None:
            count += 1
            cursor = cursor.tail
        return count

    def printdata(self):
        cursor = self._head
        while cursor is not None:
            print(cursor.data, end=" ")
            cursor = cursor.tail
        return 0

    def addFromHead(self, item: int):

        if self.isempty():  #
            self._head = doubleNode(item)
            return 0
        else:
            new_node = doubleNode(item)
            self._head.head = (new_node)
            new_node.tail = (self._head)
            self._head = new_node
        return 0

    def append(self, item: int):

        if self.isempty():
            self._head = doubleNode(item)
            return 0
        else:
            cursor = self._head
            while not cursor.tail is None:
                cursor = cursor.tail
            new_node = doubleNode(item)
            new_node.head = (cursor)
            cursor.tail = (new_node)
            return 0

    def insert(self, position: int, item: int):
        "insert behind the position ; offset = position-1"
        if not isinstance(item, int):
            raise ValueError("inouttype error!")
        if position <= 0:
            self.addFromHead(item)
            return 0
        if position >= self.length():
            self.append(item)
            return 0
        cursor = self._head
        count = 0
        while count < position-1:  # 定位到offset 在cursor 之后插入
            cursor = cursor.tail
            count += 1
        new_node = doubleNode(item)
        # update four link
        new_node.tail = (cursor.tail)
        new_node.head = (cursor)
        cursor.tail = (new_node)
        new_node.tail.head = (new_node)
        return 0

    def search(self, item: int) -> bool:
        cursor = self._head
        while cursor is not None:
            if cursor.data is item:
                return True
            cursor = cursor.tail
        return False

    def delete(self, item: int) -> bool:
        """delete element ; offset=position-1"""
        if self._head is None:
            return False

        curosr = self._head
        while curosr is not None:
            if curosr.data is item:
                if curosr.head is None:    # 删除头节点
                    self._head = curosr.tail
                    if self._head is not None:  # 头节点只有一个node
                        self._head.head = (None)
                else:
                    curosr.head.tail = (curosr.tail)
                if curosr.tail is not None:    # 为节点特殊情况
                    curosr.tail.head = (curosr.head)
                break
            curosr = curosr.tail
        return False
