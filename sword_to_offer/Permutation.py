# -*- coding: utf-8 -*-
#  @Time        :    2018/6/22 2:13
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    Permutation.py
#  @Place       :    dormitory
'''
题目描述
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
思路：递归。
最佳思路：return sorted(list(set(map(''.join, itertools.permutations(ss)))))
                排序(list(去重(合并字符(''.join,字符元组全排列list))))
'''

class Solution:
    def get(self,ss):
        if len(ss)==1:
            return [ss]
        result=[]
        visited=[]
        for i in range(len(ss)):
            if ss[i] in visited:
                continue
            else:
                visited.append(ss[i])
            sub_result=self.get(ss[0:i]+ss[i+1:])
            for x in sub_result:
                result.append(ss[i]+x)
        return result

    def Permutation(self, ss):
        # write code here
        l=list(ss)
        l.sort()
        ss="".join(l)
        result=self.get(ss)
        for x in result:
            print x
        return result


def main():
    print(Solution().Permutation("abcc"))
    pass


if __name__ == '__main__':
    main()
