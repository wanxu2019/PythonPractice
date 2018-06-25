# -*- coding: utf-8 -*-
#  @Time        :    2018/6/22 1:14
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    BinaryTreeToDuplexLinkedList.py
#  @Place       :    dormitory
'''
题目描述
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
思路：递归，先求左子树双向链表与右子树链表，再与根节点连接构成整个链表。
最佳思路：中序遍历的非递归写法。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        else:
            lList = self.Convert(pRootOfTree.left)
            head = pRootOfTree
            if lList:
                head = lList
            while lList and lList.right:
                lList = lList.right
            if lList:
                lList.right = pRootOfTree
            pRootOfTree.left = lList
            rList = self.Convert(pRootOfTree.right)
            pRootOfTree.right = rList
            if rList:
                rList.left = pRootOfTree
            pRootOfTree = head
        return pRootOfTree


def main():
    pass


if __name__ == '__main__':
    main()
