# -*- coding: utf-8 -*-
#  @Time        :    2018/6/20 21:36
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    minNumOfRotateArray.py
#  @Place       :    dormitory
'''
题目描述：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
思路：二分查找，判别依据为与首个数字的比较
'''


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # 未旋转的情况
        if len(rotateArray) == 0:
            return 0
        if rotateArray[0] < rotateArray[len(rotateArray) - 1]:
            return rotateArray[0]
        l = 0
        r = len(rotateArray) - 1
        while l < r:
            i = (l + r) / 2
            if rotateArray[i] > rotateArray[i + 1]:
                return rotateArray[i + 1]
            elif rotateArray[i] > rotateArray[0]:
                l = i + 1
            else:
                r = i
        return rotateArray[i]


def main():
    print Solution().minNumberInRotateArray([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print Solution().minNumberInRotateArray([6, 7, 8, 9, 10, 1, 2, 3, 4, 5])
    pass


if __name__ == '__main__':
    main()
