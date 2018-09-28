# -*- coding: utf-8 -*-
#  @Time        :    2018/9/26 19:33
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test2.py
#  @Place       :    dormitory


def main():
    def solution(arr):
        if len(arr) == 0:
            return 0, []
        elif len(arr) == 1:
            return arr[0], []
        elif len(arr) == 2:
            if arr[0] > arr[1]:
                return arr[0], arr[1:]
            else:
                return arr[1], arr[:1]
        else:
            # 取首位
            n1, arr1 = solution(arr[1:])
            n2, arr2 = solution(arr1)
            value1 = arr[0] + solution(arr2)[0]
            # 取尾
            n1, arr1 = solution(arr[:-1])
            n2, arr2 = solution(arr1)
            value2 = arr[-1] + solution(arr2)[0]
            if value1 >= value1:
                # 取首位
                return value1, arr[1:]
            else:
                return value2, arr[:-1]

    N = int(raw_input())
    arr = map(int, raw_input().split())
    print(solution(arr)[0])
    # value = 0
    # while len(arr) > 0:
    #     n1, arr = solution(arr)
    #     n2, arr = solution(arr)
    #     n3, arr = solution(arr)
    #     value += n1
    # print value


if __name__ == '__main__':
    main()
