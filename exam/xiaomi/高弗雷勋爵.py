# -*- coding: utf-8 -*-
#  @Time        :    2018/9/13 17:34
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    高弗雷勋爵.py
#  @Place       :    dormitory
# 此处可 import 模块

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""


def solution1(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # 返回处理后的结果
    nums = map(int, line.split(" "))
    count = 0
    zero_count = 0

    def f(x):
        return max(0, x - 2)

    def get_zero_count(l):
        count = 0
        for x in l:
            if x == 0:
                count += 1
        return count

    while zero_count != len(nums):
        count += 1
        last_zero_count = -1
        while last_zero_count != zero_count:
            last_zero_count = zero_count
            nums = map(f, nums)
            zero_count = get_zero_count(nums)
    return count


def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # 返回处理后的结果
    nums = map(int, line.split(" "))
    nums.sort()
    count = 1
    hit = 2
    last_i = 0
    i = 0
    while hit < nums[-1]:
        while nums[i] <= hit:
            i += 1
        if i != last_i:
            last_i=i
            hit += 2
        else:
            count += 1
            hit += 2
    return count


def main():
    print(solution("1 12 3 6 10"))
    pass


if __name__ == '__main__':
    main()
