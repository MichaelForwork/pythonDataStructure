#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   doublelink_circle.py
@Time    :   2020/06/06 20:18:28
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    双向循环链表的基本功能实现;

'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-
import doublelink as DoubleLink


class DoubleLinkCircleNode(DoubleLink.doubleNode):
    pass
    

class DoubleLinkCircle(object):

    def __init__(self, node=None):
        self.__head = node
        if node is not None:
            self.__head.head = self.__head
            self.__head.tail = self.__head
        

    def isempty(self):
        return self.__head is None

    def length(self, ):
        if self.isempty():
            return 0
        else:
            count = 1    # 既然已经排除了空链表的存在，为什么不从1开始
            cursor = self.__head
            while cursor.tail is not self.__head:
                cursor = cursor.tail
                count += 1
            return count

    def printData(self,):
        if self.isempty():
            print("there is no data")
            return
        else:
            count = 1
            cursor = self.__head
            LinkLength = self.length()
            while count <= LinkLength:
                print("data:", count, cursor.data)
                cursor = cursor.tail
                count += 1
            return

    def addFromHead(self, item: int):

        if self.isempty():
            self.__head = DoubleLinkCircleNode(item)
            return
        else:
            new_node = DoubleLinkCircleNode(item)
            # 修改尾部节点
            cursor = self.__head
            while cursor.tail is not self.__head:
                cursor = cursor.tail
            # 修改4条链
            cursor.tail = new_node
            new_node.head = cursor
            new_node.tail = self.__head
            self.__head.head = new_node
            self.__head = new_node  # 重新设置头节点
            return

    def append(self, item: int):
        if self.isempty():
            self.__head = DoubleLinkCircleNode(item)
        else:
            new_node = DoubleLinkCircleNode(item)
            cursor = self.__head
            while cursor.tail is not self.__head:
                cursor = cursor.tail
            cursor.tail = new_node
            new_node.head = cursor
            new_node.tail = self.__head
            self.__head.head = new_node
            return

    def insert(self, parameter_list:int,position:int):
        """
        offset = position-1"""
        item = parameter_list     
        if self.isempty():
            new_node = DoubleLinkCircleNode(item)   
            self.__head = new_node
            return
        else:
            if position <= 1:
                self.addFromHead(item)
            elif position >= self.length():
                self.append(item)
            else:
                count = 1
                cursor = self.__head
                new_node = DoubleLinkCircleNode(item)   
                while count < position :
                    cursor = cursor.tail
                    count += 1
                new_node.head = cursor
                new_node.tail = cursor.tail
                cursor.tail = new_node
                new_node.tail.head = new_node
                return

    def delete(self, item: int):
        """
        自动调用deleteByItem"""
        return self.deleteByItem(item)

    def deleteByItem(self, item:int):
        """
        特殊情况：
        1 只有1个节点
        2 删除头节点
        3 删除尾部节点"""
        if self.isempty():
            raise EOFError("can not delete a null link.")
        else:
            cursor = self.__head
            while cursor.tail is not self.__head:
                if item == cursor.data:
                    cursor.head.tail = cursor.tail
                    cursor.tail.head = cursor.head
                    if cursor == self.__head:   #   2 删除头节点
                        self.__head = cursor.tail
                    cursor.head = None
                    cursor.tail = None
                    return
                cursor = cursor.tail
            # 1
            if item == cursor.data and cursor == self.__head:
                self.__head = None
                return
            # 3 
            if item == cursor.data:
                cursor.head.tail = cursor.tail
                cursor.tail.head = cursor.head
                cursor.head = None
                cursor.tail = None
                return

    def deleteByPosition(self, position:int):
        """特殊情况：
        无 """
        if self.isempty():
            raise EOFError("can not delete a null link.")
        else:
            if position <= 1:    # 删除头节点    
                cursor = self.__head
                while cursor.tail is not self.__head:
                    cursor = cursor.tail
                self.__head = self.__head.tail
                self.__head.head = cursor
                cursor.tail.head =None
                cursor.tail.tail = None
                cursor.tail = self.__head
                return
            elif position >= self.length():     #删除尾部节点
                cursor = self.__head
                while cursor.tail is  not self.__head:
                    cursor = cursor.tail
                cursor.head.tail = cursor.tail
                cursor.tail.head = cursor.head
                cursor.head = None
                cursor.tail = None
                return
            else:
                count = 1
                cursor = self.__head
                while count < position:
                    cursor = cursor.tail
                    count +=1
                cursor.tail.head = cursor.head
                cursor.head.tail = cursor.tail
                cursor.tail = None
                cursor.head = None
                return

    def searchByItem(self,item:int ):
        if self.isempty():
            return False
        else:
            cursor = self.__head
            while cursor.tail is not self.__head:
                if cursor.data == item:
                    return True
                cursor = cursor.tail
            if cursor.data == item:
                return True
            else:
                return False

    def shwo(self, parameter_list):
        
        raise NotImplementedError