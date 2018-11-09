# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 11:21
# @Author  : Json Wan
# @Description : 链表拆分、反转、合并
# @File    : 补招1.py


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __unicode__(self):
        return str(self.val)


# 拆分链表
def split(root):
    p1 = root
    p2 = root.next
    p1_bak = p1
    p2_bak = p2
    while p2:
        p1.next = p2.next
        p1 = p1.next
        if p1:
            p2.next = p1.next
        else:
            p2.next = None
        p2 = p2.next
    return p1_bak, p2_bak


# 反转链表
def reverse_list2(root):
    p = root
    if not p:
        return root
    p1 = root.next
    if not p1:
        return root
    p2 = p1.next
    p.next = None
    while p2:
        p1.next = p
        tmp = p2.next
        p2.next = p1
        p = p1
        p1 = p2
        p2 = tmp
    p1.next = p
    return p1


# 反转链表
def reverse_list(root):
    p = root
    if not p:
        return root
    q = root.next
    if not q:
        return root
    p.next = None
    while q:
        r = q.next
        q.next = p
        p = q
        q = r
    return p


# 合并升序链表
def merge_list(p1, p2):
    if not p1:
        return p2
    if not p2:
        return p1
    p = None
    if p1.val < p2.val:
        p = p1
        p1 = p1.next
    else:
        p = p2
        p2 = p2.next
    p_bak = p
    while p1 and p2:
        if p1.val < p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next
        p = p.next
    if p1:
        p.next = p1
    if p2:
        p.next = p2
    return p_bak


# 打印链表
def print_node(root_bak):
    root = root_bak
    while root.next:
        print root.val, "-->",
        root = root.next
    print root.val


def main():
    node1 = Node(1)
    node2 = Node(100)
    node3 = Node(2)
    node4 = Node(99)
    node5 = Node(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # node6 = Node(98)
    # node5.next = node6
    print "原始链表"
    print_node(node1)
    print "拆分"
    p1, p2 = split(node1)
    print_node(p1)
    print_node(p2)
    # 需要注意的是反转链表时是会影响传入的参数的！！会改变参数p2.next的值
    # print_node(reverse_list(p1))
    # print_node(reverse_list(p2))
    print "反转"
    p3 = reverse_list(p2)
    print_node(p3)
    print "合并"
    p4 = merge_list(p1, p3)
    print_node(p4)
    print "反转"
    p5 = reverse_list(p4)
    print_node(p5)


if __name__ == '__main__':
    main()
