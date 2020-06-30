/* -*- encoding: utf-8 -*-
'''
@File    :   dfad.cpp
@Time    :   2020/06/27 18:12:39
@Author  :   Michael 
@Version :   1.0
@Contact :   Search username of MichaelForwork at github
@Doc    :    递归算法的求解
'''
# -*-*-*-*- here is the beginning of this script -*-*-*-*- */

int getSum(int a[],int n){
   // 分治策略 
    return (n<1) ? 0 : getSum(a,n-1) + a[n-1] ;
    //递归跟踪 funciton stack O(n) 线性复杂度  
}

int main(){
    int arrary[100] = {1,2};
    return 0;
}