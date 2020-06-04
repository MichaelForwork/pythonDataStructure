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
import classtest as ct

class SingleLinkCircleNode(object,):
    
    def __init__(self,data = None):
        self.__next = self  # circle 
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

    
    @property
    def head(self):
        return self.__head
    
    @head.setter
    def head(self,value):
        self.__head = value 
        return 0

    def isempty(self, )->bool:
        return  self.__head is None

    def __init__(self, ):
        self.__head = None
    
    def length(self, )->int:
        ""
        if self.isempty():
            return 0
        
        count = 1
        cursor = self.head
        
        while cursor.next != self.head:
            count += 1
            cursor = cursor.next
        return count 

    def printdata(self):
        "遍历+ 打印"
        if self.isempty():
            return 0
        
        cursor = self.head
        count = 1 
        while cursor.next != self.head:
            print ("data number: ",count,"data value: ",cursor.data)
        return 0

    def addFromHead(self,item:int):
        if self.isempty():
            self.head = SingleLinkCircleNode(item)
        return