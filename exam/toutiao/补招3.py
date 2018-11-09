# -*- coding: utf-8 -*-
#  @Time        :    2018/11/9 16:56
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    补招3.py
#  @Place       :    dormitory


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def main():
    root = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)
    node13 = Node(13)
    node14 = Node(14)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    node3.left = node7
    node3.right = node8
    node4.left = node9
    node4.right = node10
    node5.left = node11
    node5.right = node12
    node6.left = node13
    node6.right = node14
    stack1 = []
    stack2 = []
    left = True
    stack1.append(root)
    while len(stack1) != 0 or len(stack2) != 0:
        if left:
            node = stack1.pop()
            print node.val,
            if node.left:
                stack2.append(node.left)
            if node.right:
                stack2.append(node.right)
            if len(stack1) == 0:
                left = False
                print
        else:
            node = stack2.pop()
            print node.val,
            if node.right:
                stack1.append(node.right)
            if node.left:
                stack1.append(node.left)
            if len(stack2) == 0:
                left = True
                print


if __name__ == '__main__':
    main()
