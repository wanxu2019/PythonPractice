# -*- coding: utf-8 -*-
'''
3 3
0 1 2
2 3 -1
1 3 1
'''

from Queue import PriorityQueue


class T:
    def __init__(self, x, y, cost):
        self.x = x
        self.y = y
        self.cost = cost
        self.all_cost = 0
        self.visited = False

    def __cmp__(self, other):
        return cmp(self.all_cost, other.all_cost)


def main():
    N, M = map(int, raw_input().split())
    matrix = []
    for i in range(N):
        matrix.append(map(int, raw_input().split()))
    for i in range(N):
        for j in range(M):
            matrix[i][j] = T(i, j, matrix[i][j])
    queue = PriorityQueue()
    queue.put(matrix[0][0])
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
        if t.x == N - 1 and t.y == M - 1:
            break
        t.visited = True
        # 搜索临近点
        for dir in dirs:
            new_x = t.x + dir[0]
            new_y = t.y + dir[1]
            if 0 <= new_x < N and 0 <= new_y < M:
                new_t = matrix[new_x][new_y]
                # 若未曾访问过且不是障碍
                if not new_t.visited and new_t.cost != -1:
                    new_t.visited = True
                    new_t.all_cost = t.all_cost + new_t.cost
                    queue.put(new_t)
    print(matrix[N - 1][M - 1].all_cost)


if __name__ == '__main__':
    main()
