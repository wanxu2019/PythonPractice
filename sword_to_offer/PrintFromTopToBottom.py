# -*- coding: utf-8 -*-
#  @Time        :    2018/7/14 22:48
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    PrintFromTopToBottom.py
#  @Place       :    dormitory
'''
题目描述
从上往下打印出二叉树的每个节点，同层节点从左至右打印。
思路：其实就是一个层序遍历，可以用队列实现；
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = [root]
        values = []
        while len(queue) > 0:
            # 取一个出来
            node = queue[0]
            values.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            queue = queue[1:]
        return values


def main():
    root = TreeNode(0)
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    print(Solution().PrintFromTopToBottom(root))
    pass


if __name__ == '__main__':
    main()
