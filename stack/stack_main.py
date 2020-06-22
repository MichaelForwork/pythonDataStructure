#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   stack_main.py
@Time    :   2020/06/22 00:00:53
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    测试栈
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-
import stack as st

if __name__ == "__main__":
    s = st.Stack()
    for i in range(5):
        s.push(i)

    while not s.isEmpty():
        print(s.pop(),"+",s.size())
