# -*- coding: utf-8 -*-
#  @Time        :    2018/6/22 4:47
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    implementStack.py
#  @Place       :    dormitory
'''
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
思路：压栈时检查是否为最小值，弹栈时若将最小值弹出去了则重新计算最小值；
最佳思路：维持一个栈与一个最小值栈，弹栈时若把最小值弹出去了则还有后面的次小值顶上，不用重新算，用空间换时间。
'''


class Solution:
    def __init__(self):
        self._list = []
        self._min_initial = False
        self._min = 0
        self._top = 0

    def push(self, node):
        # write code here
        self._top += 1
        self._list.append(node)
        if self._min_initial:
            if node < self._min:
                self._min = node
        else:
            self._min = node
            self._min_initial = True

    def pop(self):
        # write code here
        self._top -= 1
        value = self._list.pop()
        if value == self._min:
            # 重新计算最小值
            if len(self._list) == 0:
                self._min_initial = False
            else:
                self._min = self._list[0]
                for i in range(1, len(self._list)):
                    if self._list[i] < self._min:
                        self._min = self._list[i]
        return value

    def top(self):
        # write code here
        return self._top

    def min(self):
        # write code here
        return self._min


class BestSolution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack or node <= self.min_stack[-1]:
            self.min_stack.append(node)

    def pop(self):
        # write code here
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.min_stack[-1]


def main():
    pass


if __name__ == '__main__':
    main()
