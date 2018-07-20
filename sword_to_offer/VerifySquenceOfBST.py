# -*- coding: utf-8 -*-
#  @Time        :    2018/7/14 23:00
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    VerifySquenceOfBST.py
#  @Place       :    dormitory
'''
题目描述
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
几个概念：
完美二叉树：除了叶子结点之外的每一个结点都有两个孩子，每一层(当然包含最后一层)都被完全填充。
完全二叉树：除了最后一层之外的其他每一层都被完全填充，并且所有结点都保持向左对齐。
完满二叉树：除了叶子结点之外的每一个结点都有两个孩子结点。
二叉搜索树：一颗普通的树：若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值，且它的左、右子树也分别为二叉搜索树。
思路：只有后序遍历数据，无法重建二叉树，只能根据搜索树的性质来判断。
虽然不能重建，但是可以尝试重建，在重建的过程中把问题划分为子问题。
先找到根节点，然后将数组分为左右两个子树，再判断左右两个子树都是二叉搜索树即可。
注意：只有一个子树的情况与两个子树的情况不同，需要分别判断。
'''


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 1:
            return True
        elif len(sequence)==0:
            return False
        root_value = sequence[len(sequence) - 1]
        i = 0
        has_two_sub_trees=False
        for i in range(len(sequence) - 2):
            if sequence[i] < root_value < sequence[i + 1]:
                has_two_sub_trees=True
                break
        if not has_two_sub_trees:
            # 必须满足只有一个子树的条件
            if sequence[0]<root_value:
                for x in sequence[:-1]:
                    if x>root_value:
                        return False
            else:
                for x in sequence[:-1]:
                    if x<root_value:
                        return False
            # 而且这个子树必须是搜索树
            return self.VerifySquenceOfBST(sequence[:-1])
        for x in sequence[0:i + 1]:
            if x > root_value:
                return False
        for x in sequence[i + 1:-1]:
            if x < root_value:
                return False
        if self.VerifySquenceOfBST(sequence[0:i + 1]) and self.VerifySquenceOfBST(sequence[i + 1:-1]):
            return True
        else:
            return False


def main():
    print(Solution().VerifySquenceOfBST([1]))
    print(Solution().VerifySquenceOfBST([1, 4]))
    print(Solution().VerifySquenceOfBST([1, 2, 3, 4, 5]))
    print(Solution().VerifySquenceOfBST([1, 4, 3, 6, 8, 10, 9, 7, 5]))
    print(Solution().VerifySquenceOfBST([1, 4, 3, 6, 10, 8, 9, 7, 5]))
    pass


if __name__ == '__main__':
    main()
