# -*- coding: utf-8 -*-
#  @Time        :    2018/6/20 22:41
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    leastNumbers.py
#  @Place       :    dormitory
'''
题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
思路：快排的思想，左右交换，多了再细分找，不够再从另一半里面找，注意递归规模的减小和所有循环的l<r控制，防止越界
'''


class Solution:
    def solute(self, tinput, k):
        if len(tinput)==0 or k>len(tinput):
            return []
        l = 0
        r = len(tinput) - 1
        p = tinput[l]
        while l < r:
            while l<r and tinput[r] >= p:
                r -= 1
            if l < r:
                tinput[l] = tinput[r]
                l += 1
            while l<r and tinput[l] < p:
                l += 1
            if l < r:
                tinput[r] = tinput[l]
                r -= 1
        tinput[l] = p
        if l == k:
            return tinput[:l]
        elif l < k:
            return tinput[:l + 1] + self.solute(tinput[l + 1:], k - l - 1)
        else:
            return self.solute(tinput[:l], k)

    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        result = self.solute(tinput, k)
        result.sort()
        return result


def main():
    # print(Solution().GetLeastNumbers_Solution([1, 2, 3, 2, 1, 4, 5, 6, 7, 8], 5))
    print(Solution().GetLeastNumbers_Solution(range(1,9), 8))
    pass


if __name__ == '__main__':
    main()
