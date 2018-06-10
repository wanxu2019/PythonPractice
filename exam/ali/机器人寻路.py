# -*- coding: utf-8 -*-
#  @Time        :    2018/6/10 19:42
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    机器人寻路.py
#  @Place       :    dormitory
'''
题目描述：
在自动化仓库中有若干障碍物，机器人需要从起点出发绕过这些障碍物到终点搬取货柜，现试求机器人从起点运动到终点用时最短的路径。 已知机器人只能沿着东西方向或南北方向移动，移动的速度为1m/s，机器人每转向90度需要花费1s。
 输入： 
第一行：起点位置坐标及机器人朝向，如： 
1 0 EAST
代表机器人初始坐标为x=1,y=0，机器人面朝东方 
第二行：终点位置坐标及机器人朝向，如： 
0 2 WEST
代表机器人需要移动至点x=0,y=2，且面朝西方 
接下来输入的是地图： 
首先是两个数字r,c，代表有地图数据有多少行与多少列，如：
2 3
0 1 0
0 0 0 
其中，左上角为坐标原点，从左向右为x轴增大的方向是东方，从上到下为y轴增大的方向是南方。
地图中1代表有障碍物，机器人不能前往，0代表无障碍物机器人可以前往 地图中相邻的每两个点之间的距离为1m。
0 <= l,w <= 128 
输出： 
机器人从起点移动到终点所需要的最短秒数，当不可达时输出65535

编译器版本: Java 1.8.0_66
请使用标准输入输出(System.in, System.out)；已禁用图形、文件、网络、系统相关的操作，如java.lang.Process , javax.swing.JFrame , Runtime.getRuntime；不要自定义包名称，否则会报错，即不要添加package answer之类的语句；您可以写很多个类，但是必须有一个类名为Main，并且为public属性，并且Main为唯一的public class，Main类的里面必须包含一个名字为'main'的静态方法（函数），这个方法是程序的入口
时间限制: 3S (C/C++以外的语言为: 5 S)   内存限制: 128M (C/C++以外的语言为: 640 M)
输入:
第一行：起点位置坐标及机器人朝向，如： 
1 0 EAST
代表机器人初始坐标为x=1,y=0，机器人面朝东方 
第二行：终点位置坐标及机器人朝向，如： 
0 2 WEST
代表机器人需要移动至点x=0,y=2，且面朝西方 
接下来输入的是地图： 
首先是两个数字r,c，代表有地图数据有多少行与多少列，如：
2 3
0 1 0
0 0 0 
其中，左上角为坐标原点，从左向右为x轴增大的方向是东方，从上到下为y轴增大的方向是南方。
地图中1代表有障碍物，机器人不能前往，0代表无障碍物机器人可以前往 地图中相邻的每两个点之间的距离为1m。
0 <= l,w <= 128
输出:
第一行：起点位置坐标及机器人朝向，如： 
1 0 EAST
代表机器人初始坐标为x=1,y=0，机器人面朝东方 
第二行：终点位置坐标及机器人朝向，如： 
0 2 WEST
代表机器人需要移动至点x=0,y=2，且面朝西方 
接下来输入的是地图： 
首先是两个数字r,c，代表有地图数据有多少行与多少列，如：
2 3
0 1 0
0 0 0 
其中，左上角为坐标原点，从左向右为x轴增大的方向是东方，从上到下为y轴增大的方向是南方。
地图中1代表有障碍物，机器人不能前往，0代表无障碍物机器人可以前往 地图中相邻的每两个点之间的距离为1m。
0 <= l,w <= 128
输入范例:
0 0 NORTH
2 0 SOUTH
2 3
0 1 0
0 0 0
输入范例:
0 0 NORTH
1 1 SOUTH
2 2
0 1
0 0
5
'''
from Queue import PriorityQueue, Queue
import pygame, sys
from pygame.locals import *
import gevent
import copy
from random import randint
import math


class Knight(object):
    DIR_NORTH = 1
    DIR_EAST = 2
    DIR_SOUTH = 3
    DIR_WEST = 4

    def __init__(self):
        self.x = 0
        self.y = 0
        self.step = 0
        self.g = 0
        self.h = 0

    @property
    def f(self):
        return self.g + self.h

    @property
    def dir(self):
        return self._dir

    @dir.setter
    def dir(self, dir_string):
        if dir_string.upper() == "NORTH":
            self._dir = Knight.DIR_NORTH
        elif dir_string.upper() == "EAST":
            self._dir = Knight.DIR_EAST
        elif dir_string.upper() == "SOUTH":
            self._dir = Knight.DIR_SOUTH
        elif dir_string.upper() == "WEST":
            self._dir = Knight.DIR_WEST
        else:
            raise Exception("DIR STRING NOT CORRECT")

    def __cmp__(self, other):
        return cmp(self.f, other.f)


class RouteNode(object):
    def __init__(self):
        self.parent_x = -1
        self.parent_y = -1
        self.g = -1


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


def my_solution():
    TYPE_BLANK = 0
    TYPE_BARRIER = 1
    TYPE_START = 2
    TYPE_END = 3
    TYPE_SEARCH = 4
    TYPE_ROUTE = 5
    TYPE_FINAL_ROUTE = 6

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
                elif arr[i][j] == TYPE_FINAL_ROUTE:
                    color = [255, 0, 255]
                draw(screen, color, [j * cell_width, i * cell_height, cell_width, cell_height], 0)
        pygame.display.update()

    def test():
        arr = [[randint(0, 3) for j in range(8)] for i in range(8)]
        show(arr)

    def calcH(table, startNode, endNode):
        # 简化的曼哈顿函数
        # return (abs(startNode.x - endNode.x) + abs(startNode.y - endNode.y))
        # return (abs(startNode.x - endNode.x) + abs(startNode.y - endNode.y)) * 10
        # return (startNode.x - endNode.x) * (startNode.x - endNode.x) + (startNode.y - endNode.y) * (startNode.y - endNode.y)
        # 曼哈顿函数
        return math.sqrt((startNode.x - endNode.x) * (startNode.x - endNode.x) + (startNode.y - endNode.y) * (startNode.y - endNode.y))

    # test()
    # 初始矩阵
    table = [
        [0, 0, 0, 0, 0, TYPE_BARRIER, 0, 0],  # 0
        [0, 0, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],  # 1
        [0, 0, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],  # 2
        [0, 0, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],  # 3
        [0, 0, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],  # 4
        [0, 0, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],  # 5
        [0, 0, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],  # 6
        [0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0, 0, 0],  # 7
    ]

    # table = [
    #     [0, TYPE_BARRIER, 0, 0, 0, TYPE_BARRIER, 0, 0],
    #     [0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],
    #     [0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],
    #     [0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],
    #     [0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],
    #     [0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],
    #     [0, 0, 0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0],
    #     [0, TYPE_BARRIER, 0, TYPE_BARRIER, 0, 0, 0, 0],
    # ]

    # table = [
    #     [0, TYPE_BARRIER,            0, TYPE_BARRIER,            0,            0, TYPE_BARRIER, 0],
    #     [0, TYPE_BARRIER,            0, TYPE_BARRIER,            0, TYPE_BARRIER, TYPE_BARRIER, 0],
    #     [0, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, 0],
    #     [0, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER,            0, 0],
    #     [0, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, 0],
    #     [0, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER, TYPE_BARRIER,            0, 0],
    #     [0,            0, TYPE_BARRIER, TYPE_BARRIER,            0, TYPE_BARRIER, TYPE_BARRIER, 0],
    #     [0, TYPE_BARRIER, TYPE_BARRIER,            0,            0, TYPE_BARRIER,            0, 0],
    # ]
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

    # 输入起始位置
    # line = raw_input("Input start position:")
    line = "3 0 north"
    ss = line.split()
    start = [int(ss[0]), int(ss[1]), ss[2]]
    # line = raw_input("Input end position:")
    line = "3 7 south"
    ss = line.split()
    end = [int(ss[0]), int(ss[1]), ss[2]]

    table[start[0]][start[1]] = TYPE_START
    table[end[0]][end[1]] = TYPE_END

    show(table)
    visited = copy.deepcopy(table)
    routeMap = [[RouteNode() for j in range(len(table[0]))] for i in range(len(table))]
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            visited[i][j] = False
    dirs = {
        # 上North
        Knight.DIR_NORTH: ([-1, 0], "North"),
        # 右EAST
        Knight.DIR_EAST: ([0, 1], "East"),
        # 下SOUTH
        Knight.DIR_SOUTH: ([1, 0], "South"),
        # 左WEST
        Knight.DIR_WEST: ([0, -1], "West")
    }
    searchList = PriorityQueue()
    endNode = Knight()
    endNode.x = end[0]
    endNode.y = end[1]
    endNode.dir = end[2]
    startNode = Knight()
    startNode.x = start[0]
    startNode.y = start[1]
    startNode.dir = start[2]
    startNode.step = 0
    startNode.g = 0
    startNode.h = calcH(table, startNode, endNode)
    # A-star算法
    searchList.put(startNode)
    ans = 65535
    time_interval = 0.1
    last_t = None
    visited_count = 0
    while not searchList.empty():
        t = searchList.get()
        # 优化1：如果之前访问过，直接不访问了，无效！！，只有没访问过的才会被加进来
        if visited[t.x][t.y]:
            print("skip (%d,%d)" % (t.x, t.y))
            continue
        if last_t:
            print("(%d,%d,%s)--->(%d,%d,%s)" % (last_t.x, last_t.y, dirs[last_t.dir][1], t.x, t.y, dirs[t.dir][1]))
            cost = abs((abs(last_t.dir - t.dir) + 1) % 4 - 1) + 1
            print("cost=%d" % (cost))
        last_t = t
        visited[t.x][t.y] = True
        visited_count += 1
        table[t.x][t.y] = TYPE_ROUTE
        show(table)
        gevent.sleep(time_interval)
        if t.x == endNode.x and t.y == endNode.y:
            turn_cost = abs((abs(endNode.dir - t.dir) + 1) % 4 - 1)
            if turn_cost:
                print("(%d,%d,%s)--->(%d,%d,%s)" % (t.x, t.y, dirs[t.dir][1], t.x, t.y, dirs[endNode.dir][1]))
            print("cost=%d" % (turn_cost))
            t.step += turn_cost
            ans = t.step
            break
        # 搜索临近点
        for direction, dir_step in dirs.items():
            newNode = Knight()
            newNode.x = t.x + dir_step[0][0]
            newNode.y = t.y + dir_step[0][1]
            # 若未曾访问过且不是障碍，已经visit过的就是在关闭列表中了，不考虑了
            if isInTable(newNode) and table[newNode.x][newNode.y] != TYPE_BARRIER:
                if not visited[newNode.x][newNode.y]:
                    cost = abs((abs(direction - t.dir) + 1) % 4 - 1) + 1
                    # print("(%d,%d,%s)--->(%d,%d,%s)" % (t.x, t.y, dirs[t.dir][1], newNode.x, newNode.y, dir_step[1]))
                    # print("cost=%d" % (cost))
                    newNode._dir = direction
                    newNode.step = t.step + cost
                    newNode.g = t.g + cost
                    newNode.h = calcH(table, newNode, endNode)
                    routeNode = routeMap[newNode.x][newNode.y]
                    if routeNode.g == -1 or newNode.g < routeNode.g:
                        # 如果新找出的路径比上一次的路径更短
                        if newNode.g < routeNode.g:
                            print "!!!!"
                            # 需要重新计算开放列表中该点的f和g值，进行更新
                            # 这里采用的是还是直接new一个节点出来加入到开放列表中
                            # 造成的后果是会使得开放列表中有许多坐标重复但f值不一样的节点，会增加遍历次数，但是最后f值低的节点副本会先被visit，并通过该副本计算周围的节点f值，f值高的节点副本也会再被visit一遍，在确定其周围节点f值时也会再算一遍，会造成开放列表中有很多不必要的重复元素，增大搜索时间
                            # 如果采用更新的方式，则需要则searchList中把节点副本找出来并更新，也需要很多时间，可能还不如不找划算，所以现在这种方式其实效率还是很高的，只是多占用了一点内存，找出来的路径可以确保一定是最短路径（除非heuristic函数非常离谱）（反证法）
                            # 因为heuristic函数是有可能非常离谱的，所以A*算法不能确保一定能找到最短路径（曼哈顿函数是可以确保的），一定能够确保找到最短路径的应该是广度优先搜索
                        # 记录路径的方式：每走一步，记录上一步是从哪里走过来的，到最后就可以从终点回溯寻路
                        routeNode.g = newNode.g
                        routeNode.parent_x = t.x
                        routeNode.parent_y = t.y
                        # 优化2：只在新找路径有提升时才放入searchList  # 有效！！！
                        searchList.put(newNode)
                        table[newNode.x][newNode.y] = TYPE_SEARCH
                        show(table)
                        gevent.sleep(time_interval)
                    else:
                        # newNode.g > routeNode.g的情况
                        print "==="
                        pass
                        # 优化2：只在新找路径有提升时才放入searchList  # 有效！！！
                        # searchList.put(newNode)
                        # table[newNode.x][newNode.y] = TYPE_SEARCH
                        # show(table)
                        # gevent.sleep(time_interval)
                else:
                    # 如果访问过，啥也不干
                    pass
        print("visited_count=%d, searchList.size=%d" % (visited_count, searchList.qsize()))
    print "ans=", ans
    back_x = endNode.x
    back_y = endNode.y
    route = []
    while back_x != -1 and back_y != -1:
        route.append((back_x, back_y))
        back_x, back_y = routeMap[back_x][back_y].parent_x, routeMap[back_x][back_y].parent_y
    route.reverse()
    print(route)
    for node in route:
        table[node[0]][node[1]] = TYPE_FINAL_ROUTE
        gevent.sleep(time_interval)
        show(table)


def main():
    gevent.joinall([
        gevent.spawn(game_loop),
        gevent.spawn_later(1, my_solution)
    ])
    pass


if __name__ == '__main__':
    main()
