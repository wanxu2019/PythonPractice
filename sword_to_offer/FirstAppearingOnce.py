# -*- coding: utf-8 -*-
#  @Time        :    2018/8/11 11:28
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    FirstAppearingOnce.py
#  @Place       :    dormitory
'''
题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
输出描述:
如果当前字符流没有存在出现一次的字符，返回#字符。
思路：
维护一个字符出现次数的字典
用一个队列保存只出现过一次的所有字符即可；
新加入字符，更新队列，更新字典
取字符则取队列第一个，队列为空则返回#

'''


class Solution:
    def __init__(self):
        self.queue = []
        self.map = dict()

    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        if not self.queue:
            return '#'
        return self.queue[0]

    def Insert(self, char):
        # write code here
        if char in self.map.keys():
            # 之前已经出现过一次
            if self.map[char] == 1:
                # 需要从队列中移除
                self.queue.remove(char)
                self.map[char] = 2
            # 之前已经出现过两次以上就不管了
            else:
                pass
        else:
            # 之前没出现过，则记录下来，并放到队列中
            self.map[char] = 1
            self.queue.append(char)
        pass


def main():
    ins = Solution()
    ins.Insert("g")
    print(ins.FirstAppearingOnce())
    ins.Insert("o")
    print(ins.FirstAppearingOnce())
    ins.Insert("o")
    print(ins.FirstAppearingOnce())
    ins.Insert("g")
    print(ins.FirstAppearingOnce())
    ins.Insert("l")
    print(ins.FirstAppearingOnce())
    ins.Insert("e")
    print(ins.FirstAppearingOnce())
    pass


if __name__ == '__main__':
    main()
