# -*- coding: utf-8 -*-
#  @Time        :    2018/6/22 0:24
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    CloneLinkedList.py
#  @Place       :    dormitory
'''
题目描述
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
思路：采用一个dict存储原链表各节点与其位置供后续查阅，采用一个数组存储新链表节点便于后续随机访问，先遍历一遍创建出新链表next结构，后续再遍历一遍为其random属性赋值，random指向链表中的节点，需要根据原链表中的位置对应关系在新链表中查找到相应节点并赋值给random。
'''


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        d = {}
        index = 0
        l = []
        pHeadBackup = pHead
        newHead = RandomListNode(0)
        p = newHead
        while pHead:
            # 记录链表各节点对应位置
            d[pHead] = index
            index += 1
            # 生成新的链表节点
            node = RandomListNode(pHead.label)
            node.random=pHead.random
            # 将新节点记录到数组便于后续随机访问
            l.append(node)
            p.next = node
            p = node
            pHead = pHead.next
        index = 0
        newHead = newHead.next
        # 记录新链表的头结点
        p = newHead
        # 为新链表中的random属性赋值
        while pHeadBackup:
            # random指向的节点得从链表中找
            if newHead.random:
                newHead.random = l[d[newHead.random]]
            else:
                newHead.random = None
            pHeadBackup = pHeadBackup.next
            newHead = newHead.next
        return p


class BestSolution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here

        head = pHead
        p_head = None
        new_head = None

        random_dic = {}
        old_new_dic = {}

        while head:
            node = RandomListNode(head.label)
            # 先赋值，使用后再覆盖的思想可以借鉴
            node.random = head.random
            old_new_dic[id(head)] = id(node)
            random_dic[id(node)] = node
            head = head.next

            if new_head:
                new_head.next = node
                new_head = new_head.next
            else:
                new_head = node
                p_head = node

        new_head = p_head
        while new_head:
            if new_head.random != None:
                new_head.random = random_dic[old_new_dic[id(new_head.random)]]
            new_head = new_head.next
        return p_head

def main():
    pass


if __name__ == '__main__':
    main()
