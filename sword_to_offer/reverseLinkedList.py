# -*- coding: utf-8 -*-
#  @Time        :    2018/6/20 22:00
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    reverseLinkedList.py
#  @Place       :    dormitory
'''
题目描述：反转链表
思路：p1,p2定两个节点，在p1,p2做交换前需要保存p2.next，另外需要注意None的检查和循环条件结束后的后处理p2.next=p1
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        p1 = pHead
        # 注意每次调用.之前需要先检查None！
        if not p1:
            return p1
        p2 = p1.next
        # 注意每次调用.之前需要先检查None！！！
        if not p2:
            return p1
        t2 = p2.next
        p1.next = None
        while t2:
            p2.next = p1
            p1 = p2
            p2 = t2
            t2 = t2.next
        # 注意结束条件到达之后还要后处理一下
        p2.next = p1
        return p2


def printNode(pHead):
    while pHead:
        print pHead.val,
        pHead = pHead.next
    print ""


def main():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    printNode(node1)
    reversed_node = Solution().ReverseList(node1)
    printNode(reversed_node)
    pass


if __name__ == '__main__':
    main()
