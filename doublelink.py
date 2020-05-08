#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   doublelink.py
@Time    :   2020/05/08 22:46:06
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    测试双向链表功能
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-
class node(object):
    def __init__(self,item):
        self.__head = None
        self.__tail = None
        self.__data = item

class doubleLink(object):
    def __init__(self):
        self.__head = None
        self.__tail = None
        
