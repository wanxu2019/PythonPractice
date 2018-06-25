# -*- coding: utf-8 -*-
#  @Time        :    2018/6/21 23:17
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    FindKthToTail.py
#  @Place       :    dormitory
'''
题目描述
输入一个链表，输出该链表中倒数第k个结点。
思路：先求长度l，再顺数去找第l-k；
思路2：遍历链表存到数组中，再随机存取，空间换时间
最佳代码思路：两个指针，先让第一个指针和第二个指针都指向头结点，然后再让第一个指正走(k-1)步，到达第k个节点。然后两个指针同时往后移动，当第一个结点到达末尾的时候，第二个结点所在位置就是倒数第k个节点了。
最佳代码用时应该跟自己的思路是一样的，指针移动次数和比较次数都一样。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k < 1:
            return None
        p = head
        l = 0
        while p and p.next:
            l += 1
            p = p.next
        l = l - k + 1
        if l < 0:
            return None
        while l > 0:
            head = head.next
            l -= 1
        return head


def main():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    head = ListNode(None)
    for i in range(5):
        head.next = node1
        print(Solution().FindKthToTail(head, i))
    pass


if __name__ == '__main__':
    main()
