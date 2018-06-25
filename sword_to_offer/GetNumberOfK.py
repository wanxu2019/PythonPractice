# -*- coding: utf-8 -*-
#  @Time        :    2018/6/22 0:13
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    GetNumberOfK.py
#  @Place       :    dormitory
'''
题目描述
统计一个数字在排序数组中出现的次数。
'''


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        l = 0
        r = len(data) - 1
        while l <= r:
            m = (l + r) / 2
            if data[m] == k:
                count = 1
                ml = m - 1
                while ml >= 0 and data[ml] == k:
                    count += 1
                    ml -= 1
                mr = m + 1
                while mr <= len(data) - 1 and data[mr] == k:
                    count += 1
                    mr += 1
                return count
            elif data[m] < k:
                l = m + 1
            else:
                r = m - 1
        return 0


def main():
    pass


if __name__ == '__main__':
    main()
