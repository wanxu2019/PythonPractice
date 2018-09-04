# -*- coding: utf-8 -*-
#  @Time        :    2018/9/4 22:20
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    明明的随机数.py
#  @Place       :    dormitory


def main():
    num = int(raw_input())
    nums = set()
    for i in range(num):
        nums.add(int(raw_input()))
    nums = list(nums)
    nums.sort()
    for i in nums:
        print i
    pass


if __name__ == '__main__':
    main()
