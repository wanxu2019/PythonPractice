# -*- coding: utf-8 -*-
#  @Time        :    2018/8/11 12:19
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    KthNode.py
#  @Place       :    dormitory
'''
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
思路：
中序遍历即可
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.count = 0

    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:
            return None
        node = None
        if pRoot.left:
            node = self.KthNode(pRoot.left, k)
        if node:
            return node
        self.count += 1
        if self.count == k:
            return pRoot
        node = self.KthNode(pRoot.right, k)
        if node:
            return node
        return None


def main():
    pass


if __name__ == '__main__':
    main()
