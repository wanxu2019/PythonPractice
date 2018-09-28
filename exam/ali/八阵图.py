# -*- coding: utf-8 -*-
#  @Time        :    2018/5/12 8:40
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    八阵图.py
#  @Place       :    dormitory
#  原作者：尹斗俊喊你学习了啊
#  链接：https://www.nowcoder.com/discuss/80764
#  来源：牛客网
import sys


def main():
    # rows = int(raw_input())
    # cols = int(raw_input())
    # matrix = [[0 for j in range(cols)] for i in range(cols)]
    # for i in range(rows):
    #     line = raw_input().split()
    #     for j in range(cols):
    #         matrix[i][j] = int(line[j])
    rows = 10
    cols = 10
    matrix = [
        [1, 0, 0, 0, 0, 2, 3, 4, 0, 0],
        [0, 2, 4, 0, 0, 0, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 0, 0, 0, 2, 4],
        [0, 0, 0, 0, 2, 0, 0, 0, 0, 3],
        [0, 0, 0, 4, 5, 3, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 1, 6, 0],
        [1, 0, 0, 0, 0, 0, 0, 2, 4, 8],
        [1, 0, 2, 2, 2, 3, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],

    ]
    disvisited = [[True for j in range(cols)] for i in range(rows)]
    min_ = sys.maxint
    max_ = -sys.maxint

    def dfs(x, y):
        dx = [0, 0, 1, 1, 1, -1, -1, -1]
        dy = [1, -1, 0, -1, 1, 0, -1, 1]

        tmp = matrix[x][y]
        disvisited[x][y] = False

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < rows and 0 <= ny < cols and disvisited[nx][ny] and matrix[nx][ny]:
                tmp += dfs(nx, ny)
        return tmp

    for i in range(rows):
        for j in range(cols):
            if disvisited[i][j] and matrix[i][j]:
                ans = dfs(i, j)
                min_ = min(min_, ans)
                max_ = max(max_, ans)
    print max_
    print min_


if __name__ == '__main__':
    main()
