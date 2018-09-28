# -*- coding: utf-8 -*-
#  @Time        :    2018/9/15 10:52
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test1.py
#  @Place       :    dormitory


def main():
    l = map(int, list(raw_input()))
    arr1 = l[:3]
    arr2 = l[3:]
    s1 = sum(arr1)
    s2 = sum(arr2)
    result = 0

    def get(arr1, arr2):
        arr1.sort(lambda x, y: cmp(y, x))
        arr2_copy = arr2[:]
        arr2_copy.sort()
        arr2_copy = map(lambda x: 9 - x, arr2_copy)
        # 同时将sum1变小，将sum2变大
        sum1 = sum(arr1)
        sum2 = sum(arr2)
        count1 = 0
        count2 = 0
        while sum1 > sum2:
            choice1 = arr1[count1]
            choice2 = arr2_copy[count2]
            if choice1 > choice2:
                sum1 -= choice1
                count1 += 1
            else:
                sum2 += choice2
                count2 += 1
        return count1 + count2

    if s1 == s2:
        result = 0
    elif s1 > s2:
        result = get(arr1, arr2)
    else:
        result = get(arr2, arr1)
    print result


if __name__ == '__main__':
    main()
