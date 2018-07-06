# -*- coding: utf-8 -*-
#  @Time        :    2018/7/6 14:01
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    python_q15.py
#  @Place       :    dormitory
import re
from Queue import PriorityQueue


class Node(object):
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


def is_in_table(node):
    if node.x < 0 or node.y < 0 or node.x >= 8 or node.y >= 8:
        return False
    return True


def heuristic(node):
    # manhattan估价函数，对于马飞日的情况并不适用！
    # return abs(node.x - x2) + abs(node.y - y2)
    # 返回0使算法退化至BFS，确保路径为最短
    return 0


def a_star():
    global x1, y1, x2, y2, visited, ans
    node_map = [[None for i in range(8)] for j in range(8)]
    start_node = Node()
    start_node.x = x1
    start_node.y = y1
    start_node.g = 0
    start_node.step = 0
    node_map[x1][y1] = start_node
    # print "start_node:", (x1, y1)
    while not que.empty():
        # 选取距离出发点最近的点作为当前节点
        current_node = que.get()
        visited[current_node.x][current_node.y] = True
        # 终止条件判断
        if current_node.x == x2 and current_node.y == y2:
            ans = current_node.step
            break
        for i in range(8):
            # 下一步节点的探测
            next_node = Node()
            next_node.x = current_node.x + dirs[i][0]
            next_node.y = current_node.y + dirs[i][1]
            # 若新的落点在棋盘内
            if is_in_table(next_node):
                # 设定下一个节点的状态
                next_node.g = current_node.g + 1
                next_node.h = heuristic(next_node)
                next_node.step = current_node.step + 1
                next_node.parent_x = current_node.x
                next_node.parent_y = current_node.y
                # 若下一个节点未访问过
                if not visited[next_node.x][next_node.y]:
                    # 放进队列
                    que.put(next_node)
                    # 记录来的路径
                    node_map[next_node.x][next_node.y] = next_node
                # 若下一个节点已访问过
                else:
                    # 取出原先记录的节点状态
                    previous_node = node_map[next_node.x][next_node.y]
                    # 若通过当前节点到达比之前的路径更优
                    if next_node.g < previous_node.g:
                        # 使用广度优先搜索这里根本就执行不到，因为广度优先每次选择的节点一定是真实的离出发点最近的节点，比当前路径长的路径不可能在当前路径探索之前被探索
                        # 加入启发式成分后能执行到但是在回溯找路径时存在死循环的问题
                        # todo:有待找出原因解决死循环
                        print "update ", (next_node.x, next_node.y)
                        # 则从当前节点前往该下一个节点
                        previous_node.g = next_node.g
                        previous_node.step = next_node.step
                        previous_node.parent_x = current_node.x
                        previous_node.parent_y = current_node.y
                    pass

    def f(node):
        if node:
            return (node.parent_x, node.parent_y)
        return None

    def printNodeMap(node_map):
        for i in range(len(node_map)):
            print(node_map[i])

    # printNodeMap(map(lambda arr: map(f, arr), node_map))
    node_list = []
    node = node_map[x2][y2]
    while node:
        node_list.append((node.x + 1, node.y + 1))
        if node.parent_x != -1:
            node = node_map[node.parent_x][node.parent_y]
        else:
            node = None
    node_list.reverse()
    # print("Road=%s" % map(lambda node: (node.x+1, node.y+1), node_list))
    # print "end_node:", (x2, y2)
    return node_list


def gen_test_data():
    return (" ".join(map(str, [i, j, k, l])) for i in range(1, 9) for j in range(1, 9) for k in range(1, 9) for l in
            range(1, 9))


def gen_one_data():
    yield "1 2 5 5"


def run():
    global x1, y1, x2, y2, visited
    # test_data = gen_test_data()
    # test_data = gen_one_data()
    while True:
        raw_str = raw_input()
        # raw_str = test_data.next()
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
        start_node = Node()
        start_node.x = x1
        start_node.y = y1
        start_node.g = start_node.step = 0
        start_node.h = heuristic(start_node)
        while not que.empty():
            que.get()
        que.put(start_node)
        road = a_star()
        print("Road=%s" % road)
        print("To get from (%s,%s) to (%s,%s) takes %d knight moves.\n" % (s[0], s[1], s[2], s[3], ans))


def main():
    run()
    pass


if __name__ == '__main__':
    main()
