# -*- coding: utf-8 -*-
#  @Time        :    2018/3/27 21:48
#  @Author      :    Json Wan
#  @Description :    2018春季实习笔试题目3   OK
#                    n份工作，k个人找，最后一行输入每人能力，输出每个人最佳工作（能力范围内工资最高的工作）
#  @File        :    find_jobs.py
#  @Place       :    dormitory

import sys

if __name__ == "__main__":
    # 读取每一行
    print("输入工作数量与找工作的人数量：")
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = map(int, line.split())
    n, k = values[0], values[1]
    work = {}
    for i in range(n):
        print("输入下一项工作信息（能力 回报）：")
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        temp = map(int, line.split())
        work[temp[0]] = temp[1]
    work_items = work.items()
    work_items.sort(lambda x, y: cmp(x[0], y[0]))
    # print(work_items)
    print("输入找工作的人的能力：")
    line = sys.stdin.readline().strip()
    values = map(int, line.split())
    for value in values:
        while value not in work.keys():
            value -= 1
        # print("value="+str(value))
        index = work_items.index((value, work[value]))
        # print(index)

        def f(x, y):
            if x[1] > y[1]:
                return x
            else:
                return y

        print reduce(f, work_items[:index + 1])[1]
