#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   doublelink_main.py
@Time    :   2020/05/08 22:48:51
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    测试doublelink
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-
import doublelink

if __name__ == "__main__":
    dlink = doublelink.doubleLink()
    dlink.addFromHead(12)
    dlink.printdata()
    for i in range(4):
        dlink.append(i)
    print("dlink length : ",dlink.length())

    dlink.insert(0,19)
    dlink.insert(6,44)
    dlink.insert(100,99)
    print("\n")
    dlink.printdata()
    print("\nsearch  item: ",dlink.search(109))
    #print("delete item: ",dlink.delete(44))
    dlink.printdata()