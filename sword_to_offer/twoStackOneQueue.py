# -*- coding: utf-8 -*-
#  @Time        :    2018/6/20 21:19
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    twoStackOneQueue.py
#  @Place       :    dormitory
'''
题目描述：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
解题思路：一个in_stack，一个out_stack，进队往in_stack里面塞，出队从out_stack中往外出，没有了则一次性把in_stack中的数据弹到out_stack中去，再往外出
'''
from random import randint


class Solution:
    in_stack = []
    out_stack = []

    def push(self, node):
        # write code here
        self.in_stack.append(node)

    def pop(self):
        # return xx
        if len(self.out_stack) == 0:
            while len(self.in_stack) != 0:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()


def main():
    queue = Solution()
    for i in range(10):
        queue.push(randint(0,100))
    for i in range(10):
        print(queue.pop())
    queue.pop()
    pass


if __name__ == '__main__':
    main()
