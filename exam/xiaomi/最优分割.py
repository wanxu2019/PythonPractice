# -*- coding: utf-8 -*-
#  @Time        :    2018/9/20 22:07
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    最优分割.py
#  @Place       :    dormitory
'''
题目描述
依次给出n个正整数A1，A2， …，An，将n个数分割成m段，每一段内的所有数的和记为这一段的权重，m段权重的最大值记为本次分割的权重。问所有分割方案中分割权重的最小值是多少？

输入
第一行依次给出正整数n，m，单空格切分；（n<=10000，m<=10000，m<=n）
第二行依次给出n个正整数单空格切分A1，A2，…，An（Ai<=10000）

输出
分割权重的最小值

样例输入
5 3
1 4 2 3 5

样例输出
5

Hint
分割成 14 | 2 3 | 5 的时候，3段的权重都为5，得到分割权重的最小值。
'''


def splitArrays(arrays, m):
    top = sum(arrays)  # 确定上界
    down = top // m  # 确定下界 （下取整）
    size = len(arrays)
    while down <= top:
        mid = (down + top) // 2  # （下取整）
        n = m
        cnt = 0
        flag = True
        for x in range(size):
            if arrays[x] > mid:  # 如果发现数列里面有一个大于目标解的，说明真正的解在右区间，即继续搜索右区间
                flag = False
                break
            if cnt + arrays[x] > mid:  # 进行一次分割， 并初始化 n, cnt
                n -= 1
                cnt = 0
            cnt += arrays[x]  # 统计每次分割的小区间的和，
            if n == 0:  # n == 0 说明划分的段数超过了 m，说明真正的解在右区间，即继续搜索右区间
                flag = False
                break
        if flag:  # 确定下一个要搜索的区间范围
            top = mid - 1  # flag == True 说明最优解还可以再小，即在左区间里面
        else:
            down = mid + 1
    return down


def main():
    m_n = list(map(int, raw_input("").split()))
    n, m = m_n[0], m_n[1]
    arrays = list(map(int, raw_input("").split()))
    print(splitArrays(arrays, m))


if __name__ == '__main__':
    main()
