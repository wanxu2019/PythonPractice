# -*- coding: utf-8 -*-
#  @Time        :    2018/7/6 14:01
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    python_q15.py
#  @Place       :    dormitory

from Queue import PriorityQueue


class Knight(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.step = 0
        self.g = 0
        self.h = 0
        self.parent_x = -1
        self.parent_y = -1

    @property
    def f(self):
        return self.g + self.h

    def __cmp__(self, other):
        return cmp(self.f, other.f)


# 开启列表
que = PriorityQueue()
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


def is_in_table(a):
    if a.x < 0 or a.y < 0 or a.x >= 8 or a.y >= 8:
        return False
    return True


# manhattan估价函数
def heuristic(a):
    return (abs(a.x - x2) + abs(a.y - y2)) * 10


def a_star():
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
            if is_in_table(s):
                if visited[s.x][s.y]:
                    s.g = t.g + 23
                    s.h = heuristic(s)
                    s.step = t.step + 1
                    que.put(s)
                else:
                    if s.g>


def demo1():
    global x1, y1, x2, y2, visited
    while True:
        s = raw_input().split()
        x1 = ord(s[0]) - ord('1')
        y1 = ord(s[1]) - ord('1')
        x2 = ord(s[2]) - ord('1')
        y2 = ord(s[3]) - ord('1')
        visited = [[False for j in range(8)] for i in range(8)]
        k = Knight()
        k.x = x1
        k.y = y1
        k.g = k.step = 0
        k.h = heuristic(k)
        while not que.empty():
            que.get()
        que.put(k)
        a_star()
        print("To get from (%s,%s) to (%s,%s) takes %d knight moves.\n" % (s[0], s[1], s[2], s[3], ans))


def main():
    demo1()
    pass


if __name__ == '__main__':
    main()
