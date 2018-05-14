# -*- coding: utf-8 -*-
#  @Time        :    2018/5/12 9:45
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    图路径最多节点.py
#  @Place       :    dormitory


# 各个节点的路径数量
road_num = []
# 表示图的邻接矩阵
graph_matrix = []


def traverse(n):
    global road_num,graph_matrix
    if road_num[n] != -1:
        return road_num[n]
    t = 0
    for i in range(len(graph_matrix[n])):
        t = t + traverse(graph_matrix[n][i]) + 1
    road_num[n] = t
    return t


def main():
    global road_num, graph_matrix
    node_num = int(raw_input())
    road_num = [-1 for i in range(node_num)]
    graph_matrix = [[] for i in range(node_num)]
    edge_num = int(raw_input())
    for i in range(edge_num):
        a, b = list(map(int, raw_input().split()))
        graph_matrix[a-1].append(b-1)
    zmax = -1
    zi = 0
    for i in range(node_num):
        t = traverse(i)
        if t > zmax:
            zi = i
            zmax = t
    print("zmax=" + str(zmax))
    pass


# 测试数据
# 8
# 10
# 1 2
# 1 3
# 2 3
# 2 4
# 3 5
# 3 6
# 4 7
# 5 7
# 6 7
# 6 8

if __name__ == '__main__':
    main()
