# -*- coding: utf-8 -*-
#  @Time        :    2018/6/10 8:51
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    A-star.py
#  @Place       :    dormitory
'''
题目描述：
problem statement

A friend of you is doing research on the Traveling Knight Problem (TKP) where you are to find the shortest closed tour of knight moves that visits each square of a given set of n squares on a chessboard exactly once. He thinks that the most difficult part of the problem is determining the smallest number of knight moves between two given squares and that, once you have accomplished this, finding the tour would be easy.
Of course you know that it is vice versa. So you offer him to write a program that solves the "difficult" part.
Your job is to write a program that takes two squares a and b as input and then determines the number of knight moves on a shortest route from a to b.
Input Specification
The input file will contain one or more test cases. Each test case consists of one line containing two squares separated by one space. A square is a string consisting of a letter (a-h) representing the column and a digit (1-8) representing the row on the chessboard.
Output Specification
For each test case, print one line saying "To get from xx to yy takes n knight moves.".
Sample Input
e2 e4
a1 b2
b2 c3
a1 h8
a1 h7
h8 a1
b1 c3
f6 f6
Sample Output
To get from e2 to e4 takes 2 knight moves.
To get from a1 to b2 takes 4 knight moves.
To get from b2 to c3 takes 2 knight moves.
To get from a1 to h8 takes 6 knight moves.
To get from a1 to h7 takes 5 knight moves.
To get from h8 to a1 takes 6 knight moves.
To get from b1 to c3 takes 1 knight moves.
To get from f6 to f6 takes 0 knight moves.
题目的意思大概是说：在国际象棋的棋盘上，一匹马共有8个可能的跳跃方向，求从起点到目标点之间的最少跳跃次数。
'''
'''
个人理解：
A-star算法就是启发式的广度优先搜索，在选择下一步时考虑了优先级，但是这样找出来的路径不一定是最优的，只能说是较优的，若想得到最优解，还是得遍历，或者用Dijkstra算法的思想。


'''

from Queue import PriorityQueue, Queue
import pygame, sys
from pygame.locals import *
import gevent
import copy


class Knight(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.step = 0
        self.g = 0
        self.h = 0

    @property
    def f(self):
        return self.g + self.h

    def __cmp__(self, other):
        return cmp(self.f, other.f)


# 已访问标记(关闭列表)
visited = [[False for j in range(8)] for i in range(8)]
# 起点(x1,y1),终点(x2,y2),最少移动次数ans
x1 = 0
y1 = 0
x2 = 0
y2 = 0
ans = 0
# 8个移动方向
dirs = [
    [-2, -1],
    [-2, 1],
    [2, -1],
    [2, 1],
    [-1, -2],
    [-1, 2],
    [1, -2],
    [1, 2],
]

# 开启列表
que = PriorityQueue()

from random import randint


# for i in range(10):
#     k = Knight()
#     k.f = randint(0, 100)
#     que.put(k)
# for i in range(10):
#     print que.qsize(), ":", que.get().f


# 判断knight是否在棋盘内
def isInTable(a):
    if a.x < 0 or a.y < 0 or a.x >= 8 or a.y >= 8:
        return False
    return True


# manhattan估价函数
def heuristic(a):
    return (abs(a.x - x2) + abs(a.y - y2)) * 10


def Astar():
    global x1, y1, x2, y2, visited, ans
    while not que.empty():
        # t为当前格
        t = que.get()
        visited[t.x][t.y] = True
        if t.x == x2 and t.y == y2:
            ans = t.step
            break
        for i in range(8):
            s = Knight()
            s.x = t.x + dirs[i][0]
            s.y = t.y + dirs[i][1]
            if isInTable(s) and not visited[s.x][s.y]:
                s.g = t.g + 23
                s.h = heuristic(s)
                s.f = s.g + s.h
                s.step = t.step + 1
                que.put(s)


def demo1():
    global x1, y1, x2, y2, visited
    while True:
        s = raw_input()
        x1 = ord(s[0]) - ord('a')
        y1 = ord(s[1]) - ord('1')
        x2 = ord(s[3]) - ord('a')
        y2 = ord(s[4]) - ord('1')
        visited = [[False for j in range(8)] for i in range(8)]
        k = Knight()
        k.x = x1
        k.y = y1
        k.g = k.step = 0
        k.h = heuristic(k)
        k.f = k.g + k.h
        while not que.empty():
            que.get()
        que.put(k)
        Astar()
        print("To get from %s%s to %s%s takes %d knight moves.\n" % (s[0], s[1], s[3], s[4], ans))


screen = None
SCREEN_SIZE = (800, 800)


def game_loop():
    global screen
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    screen.fill((255, 255, 255))
    pygame.display.set_caption('Routing')
    pygame.draw.rect(screen, (0, 255, 0), [0, 0, 300, 200], 0)
    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()
        gevent.sleep(0)
    pass


def my_demo():
    TYPE_BLANK = 0
    TYPE_BARRIER = 1
    TYPE_START = 2
    TYPE_END = 3
    TYPE_SEARCH = 4
    TYPE_ROUTE = 5

    def draw(screen, color, rect, width):
        pygame.draw.rect(screen, color, rect, width)

    def show(arr):
        global screen
        screen.fill((255, 255, 255))
        cell_width = SCREEN_SIZE[0] / len(arr[0])
        cell_height = SCREEN_SIZE[1] / len(arr)
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                # 空路径
                if arr[i][j] == TYPE_BLANK:
                    color = [255, 255, 255]
                # 障碍物
                elif arr[i][j] == TYPE_BARRIER:
                    color = [0, 0, 255]
                # 起始点
                elif arr[i][j] == TYPE_START:
                    color = [255, 255, 0]
                # 目标点
                elif arr[i][j] == TYPE_END:
                    color = [255, 0, 0]
                # 路径点
                elif arr[i][j] == TYPE_SEARCH:
                    color = [0, 255, 255]
                elif arr[i][j] == TYPE_ROUTE:
                    color = [0, 255, 0]
                draw(screen, color, [j * cell_width, i * cell_height, cell_width, cell_height], 0)
        pygame.display.update()

    def test():
        arr = [[randint(0, 3) for j in range(8)] for i in range(8)]
        show(arr)

    def calcH(table, startNode, endNode):
        return (startNode.x - endNode.x) * (startNode.x - endNode.x) + (startNode.y - endNode.y) * (
        startNode.y - endNode.y)

    # test()
    # 初始矩阵
    # table = [
    #     [0, TYPE_BARRIER, 0,            0, 0, TYPE_BARRIER, 0, 0],
    #     [0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],
    #     [0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],
    #     [0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],
    #     [0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],
    #     [0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],
    #     [0,            0, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],
    #     [0, TYPE_BARRIER, 0, TYPE_BARRIER, 0,            0, 0, 0],
    # ]
    table = [
        [0, TYPE_BARRIER,            0, TYPE_BARRIER,            0,            0, TYPE_BARRIER, 0],
        [0, TYPE_BARRIER,            0, TYPE_BARRIER,            0, TYPE_BARRIER, TYPE_BARRIER, 0],
        [0, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, 0],
        [0, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER,            0, 0],
        [0, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, 0],
        [0, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER,            0, 0],
        [0,            0, TYPE_BARRIER, TYPE_BARRIER,            0, TYPE_BARRIER, TYPE_BARRIER, 0],
        [0, TYPE_BARRIER, TYPE_BARRIER,            0,            0, TYPE_BARRIER,            0, 0],
    ]
    # table = [
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, TYPE_BARRIER, 0, 0, 0],
    #     [0, 0, 0, 0, TYPE_BARRIER, 0, 0, 0],
    #     [0, 0, 0, 0, TYPE_BARRIER, 0, 0, 0],
    #     [0, 0, 0, 0, TYPE_BARRIER, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0],
    # ]

    def isInTable(a):
        if a.x < 0 or a.y < 0 or a.x >= len(table[0]) or a.y >= len(table):
            return False
        return True

    start = [3, 0]
    end = [3, 7]
    table[start[0]][start[1]] = TYPE_START
    table[end[0]][end[1]] = TYPE_END

    show(table)
    visited = copy.deepcopy(table)
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            visited[i][j] = False
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
    searchList = PriorityQueue()
    endNode = Knight()
    endNode.x = end[0]
    endNode.y = end[1]
    startNode = Knight()
    startNode.x = start[0]
    startNode.y = start[1]
    startNode.step = 0
    startNode.g = 0
    startNode.h = calcH(table, startNode, endNode)
    # A-star算法
    searchList.put(startNode)
    ans=65535
    time_interval=0.2
    while not searchList.empty():
        t = searchList.get()
        visited[t.x][t.y] = True
        table[t.x][t.y] = TYPE_ROUTE
        show(table)
        gevent.sleep(time_interval)
        if t.x == endNode.x and t.y == endNode.y:
            ans=t.step
            break
        # 搜索临近点
        for dir in dirs:
            newNode = Knight()
            newNode.x = t.x + dir[0]
            newNode.y = t.y + dir[1]
            # 若未曾访问过且不是障碍
            if isInTable(newNode) and not visited[newNode.x][newNode.y] and table[newNode.x][newNode.y] != TYPE_BARRIER:
                newNode.step = t.step + 1
                newNode.g = t.g + 1
                newNode.h = calcH(table, newNode, endNode)
                searchList.put(newNode)
                table[newNode.x][newNode.y] = TYPE_SEARCH
                show(table)
                gevent.sleep(time_interval)
    print "ans=", ans


def main():
    gevent.joinall([
        gevent.spawn(game_loop),
        gevent.spawn_later(1, my_demo)
    ])
    pass


if __name__ == '__main__':
    main()
