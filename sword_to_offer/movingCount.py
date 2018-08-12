# -*- coding: utf-8 -*-
#  @Time        :    2018/8/12 1:25
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    movingCount.py
#  @Place       :    dormitory
'''
题目描述
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
思路：
先找出障碍物，再BFS即可；
其实不用先找出障碍物，边走边找即可，判断合格条件时多加一个条件即可
'''


class Solution:
    def bitSum(self, i, j):
        s = 0
        while i > 0:
            s += i % 10
            i = i / 10
        while j > 0:
            s += j % 10
            j = j / 10
        return s

    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold<0:
            return 0
        from Queue import Queue
        visited = [[False for j in range(cols)] for i in range(rows)]
        num = 0
        queue = Queue()
        queue.put((0, 0))
        while not queue.empty():
            point = queue.get()
            if not visited[point[0]][point[1]]:
                visited[point[0]][point[1]] = True
            else:
                continue
            num += 1
            # 探索它周围的点
            for dirX, dirY in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                newX = point[0] + dirX
                newY = point[1] + dirY
                if 0 <= newX < rows and 0 <= newY < cols and self.bitSum(newX, newY) <= threshold and not visited[newX][
                    newY]:
                    queue.put((newX, newY))
        return num


def main():
    print(Solution().movingCount(1, 2, 2))
    print(Solution().movingCount(1, 3, 3))
    print(Solution().movingCount(2, 3, 3))
    pass


if __name__ == '__main__':
    main()
