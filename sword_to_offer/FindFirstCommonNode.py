# -*- coding: utf-8 -*-
#  @Time        :    2018/6/22 0:07
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    FindFirstCommonNode.py
#  @Place       :    dormitory
'''
题目描述
输入两个链表，找出它们的第一个公共结点。
思路：先求出俩链表长度差，把长的表头结点往后推移差值后同时移动。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        l1 = 0
        l2 = 0
        p1 = pHead1
        p2 = pHead2
        while pHead1:
            l1 += 1
            pHead1 = pHead1.next
        while pHead2:
            l2 += 1
            pHead2 = pHead2.next
        if l1 > l2:
            for i in range(l1 - l2):
                p1 = p1.next
        else:
            for i in range(l2 - l1):
                p2 = p2.next
        while p1 is not p2:
            p1 = p1.next
            p2 = p2.next
        return p1


def main():
    pass


if __name__ == '__main__':
    main()
