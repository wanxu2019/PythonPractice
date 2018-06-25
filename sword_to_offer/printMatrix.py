# -*- coding: utf-8 -*-
#  @Time        :    2018/6/22 3:33
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    printMatrix.py
#  @Place       :    dormitory
'''
题目描述
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
思路：一步步试探着往前走，碰壁或者遇到访问过的就转弯直到连续转两次弯或者扫描完毕计数达到。
最佳思路：用左上与右下坐标定位，分四段分别处理，然后往里各走一步，循环直至左上右下重合。
'''


class Solution:
    # matrix类型为一维维列表，需要返回列表
    def printMatrix1D(self, matrix):
        # matrix = reduce(lambda x, y: x + y, matrix)
        # write code here
        import math
        l = int(math.sqrt(len(matrix) + 1))
        dirs = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        x, y = 0, 0
        dir_index = 0
        visited = [False for i in range(len(matrix))]
        count = 0
        i = 0
        result = []
        while count < len(matrix):
            print matrix[i],
            visited[i] = True
            result.append(matrix[i])
            if dir_index == 0:
                i += 1
            elif dir_index == 1:
                i += l
            elif dir_index == 2:
                i += -1
            else:
                i += -l
            new_x = i % l
            new_y = i / l
            if new_x < 0 or new_x > l - 1 or new_y < 0 or new_y > l - 1 or not (
                                x + dirs[dir_index][0] == new_x and y + dirs[dir_index][1] == new_y) or visited[i]:
                # 需要换方向
                dir_index += 1
                dir_index = dir_index % 4
                x += dirs[dir_index][0]
                y += dirs[dir_index][1]
                i = y * l + x
            else:
                x = new_x
                y = new_y
            count += 1
        return result

    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        import math
        rows = len(matrix)
        cols = len(matrix[0])
        dirs = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]
        x, y = 0, 0
        dir_index = 0
        visited = [[False for j in range(len(matrix[0]))] for i in range(len(matrix))]
        count = 0
        result = []
        while count < rows * cols:
            print matrix[y][x],
            visited[y][x] = True
            result.append(matrix[y][x])
            if dir_index == 0:
                new_x = x + 1
                new_y = y
            elif dir_index == 1:
                new_x = x
                new_y = y + 1
            elif dir_index == 2:
                new_x = x - 1
                new_y = y
            else:
                new_x = x
                new_y = y - 1
            if new_x < 0 or new_x > cols - 1 or new_y < 0 or new_y > rows - 1 or visited[new_y][new_x]:
                # 需要换方向
                dir_index += 1
                dir_index = dir_index % 4
                x += dirs[dir_index][0]
                y += dirs[dir_index][1]
            else:
                x = new_x
                y = new_y
            count += 1
        return result


def main():
    # Solution().printMatrix([[i] for i in range(1, 6)])
    Solution().printMatrix([[1+j+i*10 for j in range(10)] for i in range(10)])
    pass


if __name__ == '__main__':
    main()
