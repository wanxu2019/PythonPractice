# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 10:26
# @Author  : Json Wan
# @Description : 
# @File    : Serialize.py
'''
题目描述
请实现两个函数，分别用来序列化和反序列化二叉树
思路1：
什么叫做序列化？
序列化的最终目的是实现网络传输，是要把所有的引用类型给去掉，变成顺序存储的结构；
最简单的序列化方法就是把二叉树补成满二叉树，然后层序遍历。
如何重建？
最容易想到的树的重建方式是递归重建，但是如何才能递归呢？
给我一个层序遍历的序列化结果，人工操作是很容易重建的，直接按次序排就可以了，抽象为数学表达其实是父节点与子节点的索引关系：Index(leftChildNode)=Index(parentNode)*2+1，Index(rightChildNode)=Index(parentNode)*2+2
遍历节点数组重建连接关系即可。
思路2：
完整描述一个二叉树的节点需要的信息：（节点的值，节点所在的层，节点在层中所处的顺位）；
知道所有节点信息的集合就可以重建二叉树。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from Queue import Queue


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        from Queue import Queue
        result = []
        sub_result = []
        get_from_queue1 = True
        queue1 = Queue()
        queue2 = Queue()
        queue1.put(pRoot)
        while not (queue1.empty() and queue2.empty()):
            if get_from_queue1:
                node = queue1.get()
                sub_result.append(node.val)
                if node.left:
                    queue2.put(node.left)
                if node.right:
                    queue2.put(node.right)
                # 将sub_result加入result，同时sub_result清空
                if queue1.empty():
                    result.append(sub_result)
                    sub_result = []
                    get_from_queue1 = False
            else:
                node = queue2.get()
                sub_result.append(node.val)
                if node.left:
                    queue1.put(node.left)
                if node.right:
                    queue1.put(node.right)
                # 将sub_result加入result，同时sub_result清空
                if queue2.empty():
                    result.append(sub_result)
                    sub_result = []
                    get_from_queue1 = True
        return result

    def allNone(self, queue):
        queue_copy = Queue()
        all_none = True
        while not queue.empty():
            node = queue.get()
            queue_copy.put(node)
            if node:
                all_none = False
        return all_none, queue_copy

    def Serialize(self, root):
        # write code here
        s = ""
        queue = Queue()
        queue.put(root)
        all_none = False
        while not queue.empty() and not all_none:
            node = queue.get()
            if node:
                s += str(node.val) + ","
                queue.put(node.left)
                queue.put(node.right)
            else:
                s += ","
                queue.put(None)
                queue.put(None)
            all_none, queue = self.allNone(queue)
        if len(s) > 0:
            s = s[:-1]
        return s

    def Deserialize(self, s):
        # write code here
        if len(s) == 0:
            return None
        arr = s.split(",")
        node_arr = []
        l = len(arr)
        for i in range(l):
            if arr[i] != "":
                node_arr.append(TreeNode(int(arr[i])))
            else:
                node_arr.append(None)
        for i in range(l):
            if not node_arr[i]:
                continue
            index = i * 2 + 1
            if index < l:
                node_arr[i].left = node_arr[index]
            else:
                break
            index += 1
            if index < l:
                node_arr[i].right = node_arr[index]
        return node_arr[0]


def main():
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node4.right = node5
    solution = Solution()
    print(solution.Serialize(node1))
    print(solution.Print(solution.Deserialize(solution.Serialize(node1))))
    print(Solution().Serialize(solution.Deserialize(solution.Serialize(node1))))
    pass


if __name__ == '__main__':
    main()
