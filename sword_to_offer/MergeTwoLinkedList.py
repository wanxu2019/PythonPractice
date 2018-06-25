# -*- coding: utf-8 -*-
#  @Time        :    2018/6/21 23:42
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    MergeTwoLinkedList.py
#  @Place       :    dormitory
'''
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
思路：归并的思想，递归合并即可；
最佳思路：新建mergeHead并保存头结点副本，while遍历两个链表，根据值大小决定往后推移哪个Head，一个表完成后mergeHead指向另一个表剩余部分，最后返回mergeHead头结点副本。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge(pHead1.next, pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2


def main():
    node11 = ListNode(1)
    node12 = ListNode(2)
    node13 = ListNode(3)
    node14 = ListNode(4)
    node15 = ListNode(5)
    node11.next = node12
    node12.next = node13
    node13.next = node14
    node14.next = node15
    node21 = ListNode(1)
    node22 = ListNode(2)
    node23 = ListNode(3)
    node24 = ListNode(4)
    node25 = ListNode(5)
    node21.next = node22
    node22.next = node23
    node23.next = node24
    node24.next = node25
    head = Solution().Merge(node11, node21)
    while head:
        print head.val
        head = head.next
    pass


if __name__ == '__main__':
    main()
