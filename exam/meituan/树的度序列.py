# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 20:37
# @Author  : Json Wan
# @Description : 
# @File    : 树的度序列.py


def main():
    T = int(raw_input())

    def is_not_loop(n, arr):
        if sum(arr) > 2 * n - 1:
            return False
        for i in range(n):
            sub_arr = arr[:i] + arr[i + 1:]
            if not is_not_loop(n - 1, sub_arr):
                return False
        return True

    def is_tree(n, arr):
        s = 0
        for x in arr:
            if x <= 0:
                return False
            s += x
        if s != 2 * (n - 1):
            return False
        if len(arr) == 1:
            return arr[0] == 0
        elif len(arr) == 2:
            return arr[0] == 1 and arr[1] == 1
        else:
            # for i in range(n):
            #     sub_arr = arr[:i] + arr[i + 1:]
            #     if not is_not_loop(n - 1, sub_arr):
            #         return False
            i=0
            j=1
            s=arr[0]
            while j<n:
                while s>=arr[j]:
                    s+=arr[j]
                    j+=1
            return True

    result = []
    for i in range(T):
        n = int(raw_input())
        arr = map(int, raw_input().split())
        if is_tree(n, arr):
            result.append("Yes")
        else:
            result.append("No")
    for x in result:
        print(x)


'''
1
6
1 1 1 4 2 1
Yes
1
5
1 1 2 2 2
No
'''
if __name__ == '__main__':
    main()
