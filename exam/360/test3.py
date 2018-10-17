# -*- coding: utf-8 -*-
#  @Time        :    2018/9/17 20:46
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test3.py
#  @Place       :    dormitory

'''
众所周知，集合{1 2 3 … N}有N!种不同的排列，假设第i个排列为Pi且Pi,j是该排列的第j个数。将N个点放置在x轴上，第i个点的坐标为xi且所有点的坐标两两不同。对于每个排列（以Pi为例），可以将其视为对上述N个点的一种遍历顺序，即从第Pi,1个点出发，沿直线距离到达第Pi,2个点，再沿直线距离到达第Pi,3个点，以此类推，最后到达第Pi,N个点，将该路线的总长度定义为L(Pi)，那么所有N!种路线的总长度之和是多少，即L(P1)+L(P2)+L(P3)+...+L(PN!)的结果是多少？
输出L(P1)+L(P2)+L(P3)+...+L(PN!)对109+7取模后的结果。


第一行包含一个整数N，1≤N≤105。
第二行包含N个空格隔开的整数x1到xN，0≤x1<x2<x3<...<xN≤109。

3
0 1 3
24

P1={1 2 3}，P2={1 3 2}，P3={2 1 3}，P4={2 3 1}，P5={3 1 2}，P6={3 2 1}；
L(P1)=3，L(P2)=5，L(P3)=4，L(P4)=5，L(P5)=4，L(P6)=3。
'''


def main():
    pass


if __name__ == '__main__':
    main()