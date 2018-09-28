# -*- coding: utf-8 -*-
#  @Time        :    2018/9/27 17:35
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test1.py
#  @Place       :    dormitory


def main():
    strs = raw_input().split("|")
    value = int(raw_input())
    arr = []
    result=True
    try:
        for s in strs:
            arr.append(map(int, s.split(",")))
    except:
        result=False

    def find(arr, i, j, value):
        if i<0 or j<0:
            return False
        while arr[0][j] > value:
            j -= 1
        if j < 0:
            return False
        while arr[i][0] > value:
            i -= 1
        if i < 0:
            return False
        if arr[i][j] < value:
            return False
        elif arr[i][j] == value:
            return True
        else:
            while i + j > 0:
                # 行查找
                l = 0
                r = j - 1
                while l < r:
                    m = (l + r) / 2
                    if arr[i][m] == value:
                        return True
                    elif arr[i][m] > value:
                        r = m - 1
                    else:
                        l = m + 1
                if arr[i][l] == value:
                    return True
                # 列查找
                l = 0
                r = i - 1
                while l < r:
                    m = (l + r) / 2
                    if arr[m][j] == value:
                        return True
                    elif arr[m][j] > value:
                        r = m - 1
                    else:
                        l = m + 1
                if arr[l][j] == value:
                    return True
                # 都没找到
                if i > 0:
                    i -= 1
                if j > 0:
                    j -= 1
            if len(arr)>0 and arr[0][0] == value:
                return True
            return False

    if result:
        result=(find(arr, len(arr) - 1, len(arr[0]) - 1, value))
    if result:
        print("true")
    else:
        print("false")

'''
1,3,5,16,18|10,11,14,17,20|23,30,34,40,50|25,33,36,42,55
17
'''
if __name__ == '__main__':
    main()
