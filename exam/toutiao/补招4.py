# -*- coding: utf-8 -*-
#  @Time        :    2018/11/9 23:31
#  @Author      :    Json Wan
#  @Description :    二分查找找出第一次出现的数字
#  @File        :    补招4.py
#  @Place       :    dormitory


def binary_search(arr, val):
    l = 0
    r = len(arr) - 1
    while l < r:
        m = (l + r) / 2
        if arr[m] == val:
            if m > 0:
                if arr[m - 1] < val:
                    return m
                else:
                    r = m - 1
            else:
                return m
        elif arr[m] < val:
            l = m + 1
        else:
            r = m - 1
    if arr[l] == val:
        return l
    return -1


def main():
    print(binary_search([1, 2, 2, 2, 2, 3], 2))
    print(binary_search([1, 2, 2, 2, 2, 3], 1))
    print(binary_search([1, 2, 2, 2, 2, 3], 3))
    print(binary_search([1, 2, 2, 2, 2, 2, 2, 2, 3], 2))
    print(binary_search([1, 1, 1, 2, 2, 2, 2, 3], 1))
    print(binary_search([1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3], 3))


if __name__ == '__main__':
    main()
