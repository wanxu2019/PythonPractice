# -*- coding: utf-8 -*-
#  @Time        :    2018/7/18 8:31
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    GetUglyNumber_Solution.py
#  @Place       :    dormitory
"""
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
思路：观察丑数序列，找出生成规律，丑数相乘一定得到丑数，也就是丑数都是由另外两个较小的丑数相乘得到的。
[2,3,4,5,6,8,9,10,12,...]
观察后发现5以后的丑数一定可以拆分成两个丑数相乘，那么就可以用Cn2的方式遍历数组生成丑数，复杂度为n2，遍历的时候其实可以确定个起始位置，不要从一开始遍历，这可由最后一个丑数确定。
整体思路：遍历+剪枝
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 1:
            return index
        nums = [2, 3, 4, 5]

        def binary_search(arr, n):
            l = 0
            r = len(arr) - 1
            while l < r:
                center = (l + r) / 2
                if arr[center] < n:
                    l = center + 1
                elif arr[center] > n:
                    r = center - 1
                else:
                    return center
            if arr[l] > n:
                return l - 1
            return l

        while len(nums) < index - 1:
            max_num = nums[-1]
            new_value = max_num * 2
            import math
            stop_index = binary_search(nums, math.sqrt(nums[-1])) + 1
            for i in range(0, stop_index + 1):
                # 二分查找找出另一个因子位置
                r_num = max_num / nums[i]
                l_index = binary_search(nums, r_num)
                value = nums[i] * nums[l_index + 1]
                if value < new_value:
                    new_value = value
            nums.append(new_value)
        return nums[index - 2]


def main():
    for i in range(1, 100):
        print(Solution().GetUglyNumber_Solution(i))
    pass


if __name__ == '__main__':
    main()
