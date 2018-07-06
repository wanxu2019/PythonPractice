# -*- coding: utf-8 -*-
#  @Time        :    2018/7/6 14:01
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    python_q15.py
#  @Place       :    dormitory
import re
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
    return abs(a.x - x2) + abs(a.y - y2)


def a_star():
    global x1, y1, x2, y2, visited, ans
    node_map = [[None for i in range(8)] for j in range(8)]
    start_Knight = Knight()
    start_Knight.x = x1
    start_Knight.y = y1
    start_Knight.g = 0
    start_Knight.step = 0
    node_map[x1][y1] = start_Knight
    while not que.empty():
        # t为当前落点
        t = que.get()
        visited[t.x][t.y] = True
        if t.x == x2 and t.y == y2:
            ans = t.step
            break
        for i in range(8):
            s = Knight()
            s.x = t.x + dirs[i][0]
            s.y = t.y + dirs[i][1]
            # 若新的落点在棋盘内
            if is_in_table(s):
                s.g = t.g + 1
                s.h = heuristic(s)
                s.step = t.step + 1
                s.parent_x = t.x
                s.parent_y = t.y
                # 若新的落点未访问过
                if not visited[s.x][s.y]:
                    que.put(s)
                    node_map[s.x][s.y] = s
                # 若新的落点已访问过
                else:
                    # 取出原先记录的落点信息
                    # previous_node = node_map[s.x][s.y]
                    # # 若通过t到达比之前的路径更优
                    # if s.g < previous_node.g:
                    #     print "#####"
                    #     # 则从t前往该落点
                    #     previous_node.g = s.g
                    #     previous_node.parent_x = t.x
                    #     previous_node.parent_y = t.y
                    pass
    node_list = []
    node = node_map[x2][y2]
    while node:
        node_list.append((node.x+1,node.y+1))
        if node.parent_x != -1:
            node = node_map[node.parent_x][node.parent_y]
        else:
            node = None
    node_list.reverse()
    # print("Road=%s" % map(lambda node: (node.x+1, node.y+1), node_list))
    print("Road=%s" % node_list)


def gen_test_data():
    return (" ".join(map(str, [i, j, k, l])) for i in range(1, 9) for j in range(1, 9) for k in range(1, 9) for l in
            range(1, 9))


def run():
    global x1, y1, x2, y2, visited
    test_data = gen_test_data()
    while True:
        # raw_str = raw_input()
        raw_str = test_data.next()
        pattern = re.compile(r"(\s*[1-8]+\s+){3}[1-8]+\s*")
        if not pattern.match(raw_str):
            print "Input must be 4 integers(0-8) separated by space"
            continue
        s = raw_str.split()
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
    run()
    pass


if __name__ == '__main__':
    main()
