# -*- coding: utf-8 -*-
#  @Time        :    2018/8/5 9:16
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    GetNext.py
#  @Place       :    dormitory
'''
题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
思路1：
通过父节点指针逐层向上找到根节点，进行中序遍历，用一个全局变量记录是否遍历到了给定节点，若遍历到了，直接返回下一个节点；
思路2：
分类讨论：
（1）给定节点没有右子节点：则中序遍历的下一个是它的父节点；
（2）给定节点有右子节点：则中序遍历下一个是其右子树中最左的节点；
注意：以上只讨论了节点在左子树的情况，若节点在右子树，其父节点是已经遍历过了的，右子树的情况为：
（1）给定节点没有右子节点：则返回None
（2）给定节点有右子节点：则下一个是其右子树中最左的节点
注意：其实以上左子树的情况还没讨论完，若节点是右叶节点且在左子树，则应该往上找，直到找到一个左子节点，下一个应该是该左子节点的父节点
'''


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __str__(self):
        return "Node(" + str(self.val) + ")"


class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return pNode
        # 若节点没有右子节点
        if not pNode.right:
            # 若节点是根节点
            if not pNode.next:
                return pNode.next
            # 若节点是左子节点
            elif pNode.next.left and pNode == pNode.next.left:
                return pNode.next
            # 若节点是右子节点
            else:
                # 一直往上找，直到找到一个左子节点或根节点
                # 当前节点的父节点
                pNode = pNode.next
                # 考察当前节点的父节点的父节点
                parentNode = pNode.next
                # 一直往上找，直到找到一个左分支
                while parentNode and parentNode.left != pNode:
                    pNode = parentNode
                    parentNode = parentNode.next
                return parentNode
        pNode = pNode.right
        while pNode.left:
            pNode = pNode.left
        return pNode


def main():
    # 树的构建
    node1 = TreeLinkNode(1)
    node2 = TreeLinkNode(2)
    node3 = TreeLinkNode(3)
    node4 = TreeLinkNode(4)
    node5 = TreeLinkNode(5)
    node6 = TreeLinkNode(6)
    node7 = TreeLinkNode(7)
    node8 = TreeLinkNode(8)
    node9 = TreeLinkNode(9)
    node10 = TreeLinkNode(10)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.next = node1
    node3.left = node6
    node3.right = node7
    node3.next = node1
    node4.right = node5
    node4.next = node2
    node5.left = node8
    node5.right = node9
    node5.next = node4
    node6.next = node7.next = node3
    node8.right = node10
    node8.next = node9.next = node5
    node10.next = node8
    # node5.left = node5.right = None
    # node4.left = node5
    # node4.right = None
    print(Solution().GetNext(node4))
    print(Solution().GetNext(node6))
    print(Solution().GetNext(node3))
    print(Solution().GetNext(node7))
    print(Solution().GetNext(node10))
    pass


if __name__ == '__main__':
    main()
