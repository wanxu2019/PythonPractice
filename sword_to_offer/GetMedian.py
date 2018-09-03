# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 13:55
# @Author  : Json Wan
# @Description : 
# @File    : GetMedian.py
'''
题目描述
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
思路：
只有1个数时，中位数是这1个数
只有2个数时，中位数是这2个数均值
只有3个数时，中位数是这3个数中间的数
随着数据量增加，前期的数是否能舍弃？？
第一个数是可能成为中间数的，因此不能舍弃，也就是说空间复杂度不可能比O(n)小，那就把所有的数都存起来呗，用空间换时间了；
数据一个一个的来，感觉插入排序的思想可以利用，二分插入嘛。
维护一个有序数组，不断往里面二分插入，复杂度应该是nlog(n)。
'''


class Solution:
    def __init__(self):
        self.arr = []
        self.count = 0

    def Insert(self, num):
        # write code here
        # 二分插入
        l = 0
        r = self.count - 1
        while l < r:
            m = (l + r) / 2
            if num > self.arr[m]:
                l = m + 1
            elif num < self.arr[m]:
                r = m - 1
            else:
                l = m
                break
        if self.count == 0:
            self.arr.append(num)
        elif num > self.arr[l]:
            self.arr = self.arr[:l + 1] + [num] + self.arr[l + 1:]
        else:
            self.arr = self.arr[:l] + [num] + self.arr[l:]
        self.count += 1

    def GetMedian(self):
        # write code here
        if self.count % 2 == 0:
            return (self.arr[self.count / 2] + self.arr[self.count / 2 - 1]) / 2.0
        else:
            return self.arr[self.count / 2]


def main():
    from random import randint
    solution = Solution()
    for i in range(100):
        solution.Insert(randint(0, 100))
        print(solution.arr)
        print(solution.GetMedian())
    pass


if __name__ == '__main__':
    main()
