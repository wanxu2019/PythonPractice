# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 9:46
# @Author  : Json Wan
# @Description : 
# @File    : Print.py
'''
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
思路：就是一个二叉树的层序遍历，用队列实现即可，主要是分层，各层之间加一个None进行分隔即可。
思路2：在什么时候加None是个问题，考虑用两个队列实现，用个Flag控制交替遍历即可。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if not pRoot:
            return []
        from Queue import Queue
        result = []
        sub_result = []
        get_from_queue1 = True
        queue1 = Queue()
        queue2 = Queue()
        queue1.put(pRoot)
        while not (queue1.empty() and queue2.empty()):
            if get_from_queue1:
                node = queue1.get()
                sub_result.append(node.val)
                if node.left:
                    queue2.put(node.left)
                if node.right:
                    queue2.put(node.right)
                # 将sub_result加入result，同时sub_result清空
                if queue1.empty():
                    result.append(sub_result)
                    sub_result = []
                    get_from_queue1 = False
            else:
                node = queue2.get()
                sub_result.append(node.val)
                if node.left:
                    queue1.put(node.left)
                if node.right:
                    queue1.put(node.right)
                # 将sub_result加入result，同时sub_result清空
                if queue2.empty():
                    result.append(sub_result)
                    sub_result = []
                    get_from_queue1 = True
        return result


def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node8
    print(Solution().Print(node1))
    pass


if __name__ == '__main__':
    main()
