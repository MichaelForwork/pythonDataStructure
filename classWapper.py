#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   classTest.py
@Time    :   2020/04/29 21:59:43
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    测试class 基本知识点 // 参数检查装饰器已经完成 ，除了类 实例方法self 参数不知道如何检测
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*-

import inspect


def checkAttribute(func):
    """装饰器"""        
    print("check attribute............")
    

    def wapper(*a,**aa):
        sig = inspect.signature(func)   
        parameters = sig.parameters
        value = list(parameters.values())
        # 剩下的没想好怎么实现
        for i,j in enumerate(a):
            if not isinstance(j,value[i].annotation):
                raise TypeError("your parameters are wrong !")
        
        "检测参数类型"

        return func(*a,**aa)


    return wapper

@checkAttribute
def mixint(a:int,b:str)->str:
    return str(a)+b

class classtest(object):
    """ 超类型 是 obj """

    def __init__(self,name,age,school,home):
        """to do : 写一个装饰器函数 检查传参类型 """
 
        self.__name = name  # private 变量
        self._age = age # 不可随便访问变量
        self.__school__ = school    # 特殊变量
        self.home = home    #public 变量
        

    @checkAttribute
    def getname (self,mydata,yourdata:int):
        """ name is a private attribute """
        return self.__name
    


if __name__ == "__main__":
    addf = classtest("young",12,"university","github")
    #print("不可随便访问变量",addf._age)    # 果然只能通过 class 的 public 方法来get 
    #print("private 变量",addf.getname("mydata","your"))     # 无法对class 的实例方法进行参数验证
    #print("public变量",addf.home) 
    #print("特殊变量",addf.__school__)
    print(mixint("23","sdgagg"))
    

