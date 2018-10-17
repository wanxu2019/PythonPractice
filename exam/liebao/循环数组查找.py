# -*- coding: utf-8 -*-
#  @Time        :    2018/10/17 22:46
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    循环数组查找.py
#  @Place       :    dormitory


# 核心：必须判断arr[m]与arr[r]的相对大小来判断当前搜索值在左序列还是右序列
# 进一步判断arr[m]、arr[l]、arr[r]与k的大小才能缩小区间
# 注意：l==m与r==m的情况需要作为边界条件考虑
# 记忆：细分8种情况！！
def find(arr, k):
    l = 0
    r = len(arr) - 1
    m = (l + r) / 2
    while l < r:
        if arr[m] == k:
            return m
        elif arr[m] < k:
            if arr[r] > arr[m]:
                if arr[r] >= k:
                    l = m + 1
                else:
                    r = m - 1
            elif arr[r] == arr[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if arr[l] < arr[m]:
                if arr[l] > k:
                    l = m + 1
                else:
                    r = m - 1
            elif arr[l] == arr[m]:
                l = m + 1
            else:
                r = m - 1
        m = (l + r) / 2
    if arr[m] == k:
        return m
    return -1


# 失败：不能只通过左端与右端数字以及k的大小来缩小区间
def find2(arr, k):
    l = 0
    r = len(arr) - 1
    m = (l + r) / 2
    while l < r:
        if arr[m] == k:
            return m
        elif arr[m] < k:
            if arr[l] < arr[r]:
                l = m + 1
            else:
                if arr[r] >= k:
                    l = m + 1
                else:
                    r = m - 1
        else:
            if arr[l] < arr[r]:
                r = m - 1
            else:
                if arr[r] >= k:
                    l = m + 1
                else:
                    r = m - 1
        m = (l + r) / 2
    if arr[m] == k:
        return m
    return -1


from random import randint


def gen_random_no_repeated_list(n, low=1, high=1000):
    s = set()
    while len(s) < n:
        s.add(randint(low, high))
    return list(s)


def gen_random_no_repeated_sorted_list(n, low=1, high=1000):
    l = gen_random_no_repeated_list(n, low, high)
    l = sorted(l)
    return l


def main():
    print(find([7, 8, 9, 1, 2, 3, 4, 5, 6], 8))
    print(find([7, 8, 9, 1, 2, 3, 4, 5, 6], 10))
    print(find([3, 4, 5, 6, 7, 8, 9, 1, 2], 8))
    print(find([719, 725, 812, 19, 74, 135, 382, 390, 618, 687], 19))
    for i in range(100):
        arr = gen_random_no_repeated_sorted_list(10)
        # 随机选取一个位置截断构造循环数组
        index = randint(0, len(arr) - 1)
        arr = arr[index:] + arr[:index]
        index = randint(0, len(arr) - 1)
        finded_index = find(arr, arr[index])
        if finded_index == index:
            print "OK"
        else:
            print "ERROR"
            print(arr)
            print("k:%d  index:%d   finded_index:%d" % (arr[index], index, finded_index))
            print("======================================")
    pass


if __name__ == '__main__':
    main()
