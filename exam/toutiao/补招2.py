# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 13:14
# @Author  : Json Wan
# @Description : 求树的最大深度
# @File    : 补招2.py


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 递归解法
def get_max_depth(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    else:
        return max(1 + get_max_depth(root.left), 1 + get_max_depth(root.right))


# 非递归解法
def get_max_depth_non_recursive(root):
    from Queue import Queue
    que = Queue()
    que.put(root)
    depth = 0
    # 注意：队列里只保存一层的节点，每次出队都把上一层的节点全部出掉
    while not que.empty():
        depth += 1
        size = que.qsize()
        for i in range(size):
            node = que.get()
            print node.val,
            if node.left:
                que.put(node.left)
            if node.right:
                que.put(node.right)
        print
    return depth


def main():
    root = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    root.left = node1
    root.right = node2
    node1.left = node3
    node2.right = node4
    node4.left = node5
    print(get_max_depth(root))
    print(get_max_depth_non_recursive(root))


if __name__ == '__main__':
    main()
