# -*- coding: utf-8 -*-
#  @Time        :    2018/6/22 5:03
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    IsPopOrder.py
#  @Place       :    dormitory
'''
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
思路：模拟一遍整个压栈出栈流程，按照给定的出栈顺序出不了了就说明序列有问题。
'''


class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        for x in popV:
            # 栈空了先压栈
            if len(stack) == 0:
                stack.append(pushV[0])
                pushV.remove(pushV[0])
            # 如果当前不能按照给定的出栈顺序出栈就一直压
            while x != stack[len(stack) - 1] and len(pushV) > 0:
                stack.append(pushV[0])
                pushV.remove(pushV[0])
            # 如果把给定的压栈数组都压完了还不能出就说明这个出栈序列有问题
            if len(pushV) == 0 and x != stack[len(stack) - 1]:
                return False
            # 终于压到可以出的情况了，那就按照给定的出栈顺序出栈
            stack.pop()
        return True


def main():
    print(Solution().IsPopOrder([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(Solution().IsPopOrder([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))
    print(Solution().IsPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
    print(Solution().IsPopOrder([], []))
    pass


if __name__ == '__main__':
    main()
