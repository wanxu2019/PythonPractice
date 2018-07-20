# -*- coding: utf-8 -*-
#  @Time        :    2018/7/15 0:04
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    FindPath.py
#  @Place       :    dormitory
'''
题目描述
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)
思路：深度优先遍历+剪枝，或者就是任务细化，递归求解。

'''
import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.solution=[]
    def findPathWithArr(self, root, expectNumber, arr):
        arr.append(root.val)
        number = sum(arr)
        if number == expectNumber:
            if not root.left and not root.right:
                # print arr
                self.solution.append(arr)
            else:
                return
        elif number < expectNumber:
            if root.left:
                newArr=copy.deepcopy(arr)
                self.findPathWithArr(root.left, expectNumber, newArr)
            if root.right:
                newArr2=copy.deepcopy(arr)
                self.findPathWithArr(root.right, expectNumber, newArr2)

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        self.findPathWithArr(root, expectNumber, [])
        pass


def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(2)
    node5 = TreeNode(2)
    node6 = TreeNode(1)
    node7 = TreeNode(3)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    Solution().FindPath(node1, 4)
    Solution().FindPath(node1, 5)
    Solution().FindPath(node1, 7)
    Solution().FindPath(node1, 10)
    pass


if __name__ == '__main__':
    main()
