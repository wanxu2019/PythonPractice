# -*- coding: utf-8 -*-
#  @Time        :    2018/7/21 1:41
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    PrintMinNumber.py
#  @Place       :    dormitory
"""
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
思路：最简单的思路：暴力搜索，全排列求最小即可。
稍微好点的思路：根据最小数字的特征：首位最小，次位最小，依次往下排，不同长度的数字比较时先填充成为相同长度再比较
"""


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        numbers=map(str,numbers)
        def get_first_list(nums):
            min_char = nums[0][0]
            for i in range(1, len(nums)):
                if nums[i][0] < min_char:
                    min_char = nums[i][0]
            result = []
            remain_nums = []
            max_length = 0
            for i in range(0, len(nums)):
                if str(nums[i])[0] == min_char:
                    max_length = max(max_length, len(nums[i]))
                    result.append(nums[i])
                else:
                    remain_nums.append(nums[i])

            def custom_cmp(x1, x2):
                return cmp(x1 + x1[0] * (max_length - len(x1)), x2 + x2[0] * (max_length - len(x2)))

            result.sort(custom_cmp)
            return result, remain_nums

        result = []
        # 再从候选数组中依次往后面的位比较直到选出首位
        while len(numbers) > 0:
            first_arr, numbers = get_first_list(numbers)
            # print first_arr, numbers
            result.extend(first_arr)
        return int("".join(result))


def main():
    print(Solution().PrintMinNumber(["3", "32", "321"]))
    print(Solution().PrintMinNumber(["3", "5", "1", "4", "2"]))
    print(Solution().PrintMinNumber(["3", "32", "321", "4", "2", "5"]))
    pass


if __name__ == '__main__':
    main()
