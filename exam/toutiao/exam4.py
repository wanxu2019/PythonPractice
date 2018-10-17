# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 20:14
# @Author  : Json Wan
# @Description : 
# @File    : exam4.py


from Queue import PriorityQueue


class T:
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label
        self.all_cost = 0
        self.visited = False

    def __cmp__(self, other):
        return cmp(self.all_cost, other.all_cost)


import sys


def main():
    k = int(raw_input())
    matrix = []
    # for s in sys.stdin:
    #     if s!="":
    #         matrix.append(map(int, s.split(",")))
    #     else:
    #         break

    s = raw_input()
    while s:
        matrix.append(map(int, s.split(",")))
        s = raw_input()

    def copy(matrix):
        new_matrix = []
        for x in matrix:
            new_matrix.append(x[:])
        return new_matrix

    def get(matrix, x, y):
        N = len(matrix)
        M = len(matrix[0])
        for i in range(N):
            for j in range(M):
                matrix[i][j] = T(i, j, matrix[i][j])
        queue = PriorityQueue()
        queue.put(matrix[x][y])
        dirs = [
            # 上
            [0, 1],
            # 右
            [1, 0],
            # 下
            [0, -1],
            # 左
            [-1, 0],
        ]
        while not queue.empty():
            t = queue.get()
            if t.label == 1:
                return t.all_cost
            t.visited = True
            # 搜索临近点
            for dir in dirs:
                new_x = t.x + dir[0]
                new_y = t.y + dir[1]
                if 0 <= new_x < N and 0 <= new_y < M:
                    new_t = matrix[new_x][new_y]
                    # 若未曾访问过且不是障碍
                    if not new_t.visited and new_t.label != -1:
                        new_t.visited = True
                        new_t.all_cost = t.all_cost + 1
                        queue.put(new_t)
        return 99999

    N = len(matrix)
    M = len(matrix[0])
    result = []
    for i in range(N):
        sub_result = []
        for j in range(M):
            d = get(copy(matrix), i, j)
            if d > k:
                sub_result.append(1)
            else:
                sub_result.append(0)
        result.append(sub_result)
    for arr in result:
        print(",".join(map(str, arr)))


'''
3
0,-1,1,0
0,0,0,-1
0,-1,0,-1
1,-1,0,0
####
0,0,0,0
0,0,0,0
0,0,0,0
0,0,0,1
'''
if __name__ == '__main__':
    main()
