# -*- coding: utf-8 -*-
#  @Time        :    2018/9/9 18:49
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test1.py
#  @Place       :    dormitory

# 因为答题时间很有限，python写算法比Java快，所以才用的python请见谅啊

def main():
    n = int(raw_input())
    arr = []
    for i in range(n):
        arr.append(map(int, raw_input().split()))
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1] and arr[j][2] > arr[i][2]:
                count += 1
                break
    print(count)


if __name__ == '__main__':
    main()
