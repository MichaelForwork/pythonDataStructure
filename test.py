import numbers
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2020/04/28 21:33:19
@Author  :   Mo Linli 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    单链表的实现
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-

class node(object):
    """节点类型"""
    def __init__(self):
        pass
    

class my_link(object):
    """
    单项链表内部数据结构
    """

    def __init__(self, parameter_list):
        self._head = None    # 不可随便访问变量
        self._next = None   # 不可随便访问变量
        
    
    @staticmethod
    def isEmpty(self):
        return self._head == None

    def getLength(self,):
        """ get length of current link """
        count = 0
        cursor = self._head
        while : 
            pass
    
    
if __name__ == "__main__":
    link = my_link()
    