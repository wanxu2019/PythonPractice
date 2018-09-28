# -*- coding: utf-8 -*-
#  @Time        :    2018/3/27 23:20
#  @Author      :    Json Wan
#  @Description :    网易2018实习生笔试题目1           Base solution OK
#                    计算重叠最多的区域，输出重叠次数
#  @File        :    recognize_overlap.py
#  @Place       :    dormitory
import sys


def show(matrix):
    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix[0])):
            print matrix[i][j]," ",
        print("")
    print("")


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    p_arr = []
    for i in range(4):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = map(int, line.split())
        p_arr.append(values)
    min_x = min(p_arr[0])
    min_y = min(p_arr[1])
    p_arr[0] = map(lambda x: x - min_x, p_arr[0])
    p_arr[2] = map(lambda x: x - min_x, p_arr[2])
    p_arr[1] = map(lambda y: y - min_y, p_arr[1])
    p_arr[3] = map(lambda y: y - min_y, p_arr[3])
    max_x = max(p_arr[2])
    max_y = max(p_arr[3])
    matrix = [[0 for i in range(max_y)] for j in range(max_x)]
    for i in range(n):
        x1, y1, x2, y2 = p_arr[0][i], p_arr[1][i], p_arr[2][i], p_arr[3][i]
        for j in range(x1, x2):
            for k in range(y1, y2):
                matrix[j][k] += 1
        show(matrix)
    ans = reduce(lambda x, y: max(x, y), map(lambda x: max(x), matrix))
    print ans
