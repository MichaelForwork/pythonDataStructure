#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   pythonData.py
@Time    :   2020/04/03 22:05:31
@Author  :   Mo Linli 
@Version :   1.0
@Contact :   Search username = MichaelForwork at github
@Desc    :   Wheel main function: this file is for me to study data structure.

'''

# here is the beginning of this wheel





'''
    时间复杂度  
        机器执行的基本运算 数量是相同的
        机器 总共执行了多少 步骤 = 时间复杂度

    python 内置模块 
        list.append 封装了基本步骤
    
    文件名用序号来区分
    
    python 文件自定义模板

'''


import timeit
import tornado


class Timeline(object):
    
    timeit.Timer()
    def timeline1(self):
        li = []
        for i in range(10000):
            li.append()
        
    def timeline2(self):
        li = []
        for i in range(10000):
            li += li[i]
            
    def timeline3(self):
        li = [i for i in range(10000)]

    def timeline4(self):
        lis = []
        lis = lis(range(10000)) 
        #'py3 range 返回可迭代的对象; py2 直接返回list'
        
    def showtime(self):
        

        


    