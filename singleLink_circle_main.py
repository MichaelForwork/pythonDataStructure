#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   singleLink_circle_main.py
@Time    :   2020/06/04 23:17:51
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    test for singlelink_circle
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-
import singlelink_circle as sc
if __name__ == "__main__":
    s = sc.SingleSinkCircle(sc.SingleLinkCircleNode(100))
    s.addFromHead(200)
    s.addFromHead(200)
    s.append(3000)
    s.insert(0,365)
    s.printdata() 
    print("then start deleting")
    #s.deleteByItem(200)
    s.deleteByPosition(0)
    print("length : ",s.length())
    s.printdata()
    print(s.search(100))