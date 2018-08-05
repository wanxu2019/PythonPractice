# -*- coding: utf-8 -*-
#  @Time        :    2018/8/5 10:23
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    deleteDuplication.py
#  @Place       :    dormitory
'''
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
思路：遍历一波，直接删呗
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 不保留重复节点
    def deleteDuplication(self, pHead):
        # write code here
        bakHead = pHead
        if not bakHead:
            return None
        rFlag=False
        while bakHead.next and bakHead.val==bakHead.next.val:
            bakHead=bakHead.next
            rFlag=True
        pHead=bakHead
        while pHead:
            flag=False
            while pHead.next and pHead.next.next and pHead.next.val == pHead.next.next.val:
                pHead.next = pHead.next.next
                flag=True
            if flag and pHead.next:
                pHead.next = pHead.next.next
            else:
                pHead = pHead.next
        if rFlag:
            return bakHead.next
        return bakHead

    # 保留重复节点的做法
    def deleteDuplication1(self, pHead):
        # write code here
        bakHead = pHead
        while pHead:
            while pHead.next and pHead.val == pHead.next.val:
                pHead.next = pHead.next.next
            pHead = pHead.next
        return bakHead


def main():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(3)
    node5 = ListNode(4)
    node6 = ListNode(4)
    node7 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    pHead = Solution().deleteDuplication(node1)
    while pHead:
        print pHead.val, " ",
        pHead = pHead.next
    print ""
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(1)
    node4 = ListNode(1)
    node5 = ListNode(2)
    node6 = ListNode(2)
    node7 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    pHead = Solution().deleteDuplication(node1)
    while pHead:
        print pHead.val, " ",
        pHead = pHead.next
    pass


if __name__ == '__main__':
    main()
