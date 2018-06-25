# -*- coding: utf-8 -*-
#  @Time        :    2018/6/22 2:37
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    HasSubtree.py
#  @Place       :    dormitory
'''
题目描述
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
思路：递归，先用深度做一些剪枝，不知是否有必要啊，再层序遍历，判断每一个节点是否包含子结构；
最佳思路：两层递归，若B为A的子结构，要么B是A根节点相同的子树，要么B包含在A的左子树中，要么B包含在A的右子树中，在判断B是否为A的根节点子树时，再次递归，看根节点的左右子节点是否包含B的左右子节点。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def calcDepth(self, pRoot):
        if not pRoot:
            return -1
        if not pRoot.left and not pRoot.right:
            pRoot.depth = 0
        else:
            pRoot.depth = 1 + max(self.calcDepth(pRoot.left), self.calcDepth(pRoot.right))
        return pRoot.depth

    def contain(self, pRoot1, pRoot2):
        if not pRoot2 and not pRoot1:
            return True
        elif not pRoot1:
            return False
        elif not pRoot2:
            return True
        if pRoot1.val != pRoot2.val:
            return False
        return self.contain(pRoot1.left, pRoot2.left) and self.contain(pRoot1.right, pRoot2.right)

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot2:
            return False
        # 先计算树的深度
        d1 = self.calcDepth(pRoot1)
        d2 = self.calcDepth(pRoot2)
        if d1 < d2:
            return False
        from collections import deque
        # 树的层序遍历+深度剪枝
        d = deque()
        d.append(pRoot1)
        while len(d) > 0:
            node = d.popleft()
            if self.contain(node, pRoot2):
                return True
            else:
                if node.left and node.left.depth >= d2:
                    d.append(node.left)
                if node.right and node.right.depth >= d2:
                    d.append(node.right)
        return False


class BestSolution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.is_subtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
                                                                                                          pRoot2)

    def is_subtree(self, A, B):
        if not B:
            return True
        if not A or A.val != B.val:
            return False
        return self.is_subtree(A.left, B.left) and self.is_subtree(A.right, B.right)


def main():
    pass


if __name__ == '__main__':
    main()
