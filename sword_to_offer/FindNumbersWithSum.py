# -*- coding: utf-8 -*-
# @Time    : 2018/7/29 4:17
# @Author  : Json Wan
# @Description : 
# @File    : FindNumbersWithSum.py
'''
题目描述
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
思路1：先把特别大的数字或者特别小的数字给去掉，找出一个合理的求解域，然后在求解域中从中间（此处的中间应该是逻辑中间，相邻两个数的和要么大于目标值，要么小于目标值，不能为同一方向，不是物理中间，逻辑中间的确定可由二分法寻找）往两边找，逐步去掉不可能的数字（与它左边的数字相加小于目标值，与它右边的数字相加大于目标值）；
思路2：思路1错了，是把题目当作输出两个数乘积最大的了；
思路3：要找最小的就从两边往中间找即可；从两边往中间找可以先去掉右边的不可能的数字，得到tsum一定在剩下的数组中产生，再去掉左边不可能的数字，如此循环往复，问题逐渐简化，最终得到的乘积最小的两个数一定是数组首尾的两个数，观察很重要！！
非常精妙的一道题！！！
'''


class Solution:
    def FindNumbersWithMaxSum(self, array, tsum):
        # write code here
        # 找求解域
        def findNum(array, target):
            # 如果找不到
            l = 0
            r = len(array) - 1
            mid = (l + r) / 2
            while l < r:
                mid = (l + r) / 2
                if array[mid] > target:
                    r = mid - 1
                elif array[mid] < target:
                    l = mid + 1
                else:
                    return mid
            # 二分查找在找不到的情况下可能返回真实值左边的数的位置，也可能返回真实值右边的数的位置
            return l

        # print(findNum([1, 2, 3, 4, 6, 7, 8], 5))
        # print(findNum([1, 2, 3, 4, 6, 7, 8,9], 5))
        # print(findNum([1, 2, 3, 4, 6, 7, 8,9,10], 5))

        # 去掉右边特别大的数字
        if array[0] + array[len(array) - 1] > tsum:
            # 在数组里二分查找tsum-array[l]的位置
            target = tsum - array[0]
            mid = findNum(array, target)
            if array[mid] <= target:
                mid += 1
            array = array[:mid]
        else:
            # 去掉左边特别小的数字
            target = tsum - array[len(array) - 1]
            mid = findNum(array, target)
            if array[mid] < target:
                mid += 1
            array = array[mid:]
        print("array:", array, tsum)

        # 然后从中间开始往两边找
        def find(array, num):
            l = 0
            r = len(array) - 1
            while l < r:
                mid = (l + r) / 2
                # 如果中间是相邻俩数相加比较大的区域，则继续往左找
                if array[mid - 1] + array[mid] > num and array[mid] + array[mid + 1] > num:
                    r = mid - 1
                # 如果中间是相邻俩数相加比较小的区域，则继续往右找
                elif array[mid - 1] + array[mid] < num and array[mid] + array[mid + 1] < num:
                    l = mid + 1
                else:
                    return mid
            return l

        index = find(array, tsum)
        while index - 1 >= 0 and index + 1 < len(array) and array[index] + array[index + 1] != tsum and array[
                    index - 1] + array[index] != tsum:
            array.remove(array[index])
            index = find(array, tsum)
        if index + 1 < len(array) and array[index] + array[index + 1] == tsum:
            return array[index:index + 2]
        elif index - 1 >= 0 and array[index - 1] + array[index] == tsum:
            return array[index - 1:index + 1]
        else:
            return []

    def FindNumbersWithSum(self, array, tsum):
        # write code here
        # 找求解域
        def findNum(array, target):
            # 如果找不到
            l = 0
            r = len(array) - 1
            mid = (l + r) / 2
            while l < r:
                mid = (l + r) / 2
                if array[mid] > target:
                    r = mid - 1
                elif array[mid] < target:
                    l = mid + 1
                else:
                    return mid
            # 二分查找在找不到的情况下可能返回真实值左边的数的位置，也可能返回真实值右边的数的位置
            return l

        # print(findNum([1, 2, 3, 4, 6, 7, 8], 5))
        # print(findNum([1, 2, 3, 4, 6, 7, 8,9], 5))
        # print(findNum([1, 2, 3, 4, 6, 7, 8,9,10], 5))

        while len(array)>0 and array[0] + array[len(array) - 1]!=tsum:
            # 去掉右边特别大的数字
            if array[0] + array[len(array) - 1] > tsum:
                # 在数组里二分查找tsum-array[l]的位置
                target = tsum - array[0]
                mid = findNum(array, target)
                if array[mid] <= target:
                    mid += 1
                array = array[:mid]
            else:
                # 去掉左边特别小的数字
                target = tsum - array[len(array) - 1]
                mid = findNum(array, target)
                if array[mid] < target:
                    mid += 1
                array = array[mid:]
        if len(array) >= 2:
            return [array[0], array[-1]]
        else:
            return []


def main():
    print(Solution().FindNumbersWithSum([1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16], 5))
    print(Solution().FindNumbersWithSum([1, 2, 3, 5, 10, 11, 12, 13, 14, 15, 16], 17))
    print(Solution().FindNumbersWithSum([1, 2, 3, 5, 10, 11, 12, 13, 14, 15, 16], 31))
    print(Solution().FindNumbersWithSum([1, 2, 4, 7, 11, 16], 10))
    print(Solution().FindNumbersWithSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 21))
    pass


if __name__ == '__main__':
    main()
