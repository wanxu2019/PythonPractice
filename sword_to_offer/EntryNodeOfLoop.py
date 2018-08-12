# -*- coding: utf-8 -*-
#  @Time        :    2018/8/11 11:47
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    EntryNodeOfLoop.py
#  @Place       :    dormitory
'''
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
思路：
最简单的思路：
维护一张hashset，走一步记录一次，看看新的节点是否已在set中；
高效解法：
快慢指针：
快慢指针一定会相遇，且相遇点一定在环中；
通过相遇点找出环的大小n；
相距为n的两个指针同时向后移动，一定会在环的入口点相遇；

'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            return None
        p1 = pHead.next
        if not p1:
            return None
        p2 = p1.next
        if not p2:
            return None
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
            if not p2:
                return None
            p2 = p2.next
            if not p2:
                return None
        meetingNode = p1
        loopNodeNum = 1
        p1 = p1.next
        while p1 != meetingNode:
            p1 = p1.next
            loopNodeNum += 1
        p1 = pHead
        p2 = pHead
        while loopNodeNum > 0:
            p1 = p1.next
            loopNodeNum -= 1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

    def EntryNodeOfLoop1(self, pHead):
        # write code here
        nodeSet = set()
        while pHead:
            if pHead not in nodeSet:
                nodeSet.add(pHead)
            else:
                return pHead
            pHead = pHead.next
        return None


def main():
    pass


if __name__ == '__main__':
    main()
