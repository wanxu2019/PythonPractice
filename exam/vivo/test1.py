# -*- coding: utf-8 -*-
#  @Time        :    2018/9/13 20:48
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test1.py
#  @Place       :    dormitory

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def main():
    def reconstruct(s1,s2):
        if not s1:
            return None
        elif len(s1)==1:
            return TreeNode(s1)
        else:
            root=TreeNode(s1[0])
            index=s2.index(s1[0])
            sub_s1_1=s1[1:1+index]
            sub_s1_2=s1[1+index:]
            sub_s2_1=s2[:index]
            sub_s2_2=s2[index+1:]
            root.left=reconstruct(sub_s1_1,sub_s2_1)
            root.right=reconstruct(sub_s1_2,sub_s2_2)
            return root
    def back_print(root):
        result=""
        if not root:
            return result
        else:
            if root.left:
                result+=back_print(root.left)
            if root.right:
                result+=back_print(root.right)
            result+=root.val
        return result
    s1 = raw_input()
    s2=raw_input()
    root=reconstruct(s1,s2)
    print(back_print(root))


if __name__ == '__main__':
    main()
