# -*- coding: utf-8 -*-
#  @Time        :    2018/6/17 20:44
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    searchMaxNumbers.py
#  @Place       :    dormitory

'''
题目描述：从n个数中找出最大的m个数的O(n)算法
思考：为什么这个算法是O(n)的？
根据数学期望来算：
第一次循环n次的期望是找出n/2个最大的数
第二次循环n/2次的期望是找出n/4个最大的数
....
总共次数的期望是n+n/2+n/4+...<2n
因此可以说算法实际是O(2n)的
'''


def search(arr, m):
    count = 0
    l = 0
    r = len(arr) - 1
    center = arr[l]
    while l < r:
        while l < r and arr[r] > center:
            r -= 1
            count += 1
        if l < r:
            arr[l] = arr[r]
            l += 1
            count += 1
        while l < r and arr[l] < center:
            l += 1
            count += 1
        if l < r:
            arr[r] = arr[l]
            r -= 1
            count += 1
    arr[l] = center
    count += 1
    if len(arr) - l == m:
        return count, arr[l:]
    elif len(arr) - l < m:
        result = search(arr[:l], m - (len(arr) - l))
        return count + result[0], arr[l:] + result[1]
    else:
        # 注意：写递归程序时要保证任意情况下递归的规模都会减小（至少减小1），否则可能无穷递归
        result = search(arr[l + 1:], m)
        return count + result[0], result[1]


from random import randint, random


def main():
    # search([1, 2, 4, 2, 5, 7, 4, 2, 5, 8], 3)
    SIZE = 100000
    for i in range(200):
        arr = [randint(SIZE / 2, SIZE) for j in range(randint(SIZE / 2, SIZE))]
        # num=randint(1,len(arr))
        num = 1
        result = search(arr, num)
        # print arr
        # arr.sort()
        # print arr[-num:]
        # result[1].sort()
        # print result[1],result[0],result[0]/float(len(arr)),len(arr)
        print result[0] / float(len(arr))
        print "=" * 30
    # search([4,2,5,8],3)
    pass


if __name__ == '__main__':
    main()
