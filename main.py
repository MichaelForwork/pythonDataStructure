#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2020/05/03 20:49:28
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-


import classtest as ct
import types

def set_home(self, parameter_list):
    self.home = parameter_list
    

if __name__ == "__main__":
    # student = ct.cccobj("michael")
    # student.age = 18   
    # student2 = ct.cccobj("jason")

    # ct.cccobj.set_home = set_home


    # student2.birth = 1988
    # print(student2.birth)
    # 测试单链表
    link = ct.Singlelink()
    for i in range(6):
        link.append(i)
    link.addFromHead(9)
    link.printdata()
    print('\n 链表的长度',link.length())
    link.insert(5,10)
    link.printdata()
    print('\n 链表的长度',link.length())
    print("是否存在元素",link.search(10))
    link.delete(10)
    print("\n是否存在元素:link.search(10)",link.search(10))
    link.printdata()
    link.delete(9)
    print("\n是否存在元素:link.search(9)",link.search(9))
    link.printdata()
    link.delete(5)
    print("\n是否存在元素:link.search(9)",link.search(5))
    link.printdata()
    