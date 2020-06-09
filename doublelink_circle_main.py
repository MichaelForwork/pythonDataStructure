#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   doublelink_circle_main.py
@Time    :   2020/06/09 22:55:49
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    测试双向循环链表功能 // 很可惜没有一次通过
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-

import doublelink_circle as dl_circle

if __name__ == "__main__":
    dl = dl_circle.DoubleLinkCircle(dl_circle.DoubleLinkCircleNode(12))
    print(dl.length())
    dl.addFromHead(11)
    dl.append(113)
    dl.insert(14,9)
    dl.printData()
    dl.deleteByItem(14)
    dl.deleteByPosition(-9)
    print("删除某些元素：",dl.searchByItem(12))
    dl.printData()