# -*- coding: utf-8 -*-
#  @Time        :    2018/9/26 19:53
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test3.py
#  @Place       :    dormitory
'''
9
1 2
2 1
2 3
3 2
1 4
2 4
6 7
6 8
7 7
'''


def main():
    N = int(raw_input())
    arr = []
    for i in range(N):
        arr.append(map(int, raw_input().split()))
    count = 0

    def is_ok(arr1, arr2, arr3):
        if arr1[0] == arr2[0] and arr1[1] == arr3[1]:
            return True
        if arr2[0] == arr3[0] and arr2[1] == arr1[1]:
            return True
        if arr3[0] == arr1[0] and arr3[1] == arr2[1]:
            return True
        return False

    for i in range(0, N - 2):
        for j in range(i, N - 1):
            for k in range(j, N):
                if is_ok(arr[i], arr[j], arr[k]):
                    count += 1
    print(N + count)
    pass


if __name__ == '__main__':
    main()
