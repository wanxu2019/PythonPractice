# -*- coding: utf-8 -*-
#  @Time        :    2018/9/15 11:17
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test2.py
#  @Place       :    dormitory


def main():
    N, M, P = map(int, raw_input().split())
    arr = map(int, raw_input().split())
    for i in range(M):
        op, index = raw_input().split()
        index = int(index)
        if op == "A":
            arr[index - 1] += 1
        elif op == "B":
            arr[index - 1] = max(arr[index - 1] - 1, 0)
    l = list(enumerate(arr))
    l.sort(lambda x, y: cmp(y[1], x[1]))
    i = 0
    real_order = 0
    order = 0
    while l[i][0] != P - 1:
        if i == 0:
            real_order = 1
        else:
            if l[i][1] != l[i - 1][1]:
                real_order = i + 1
        i += 1
    if i == 0:
        real_order += 1
    elif l[i][1] != l[i - 1][1]:
        real_order = i + 1
    print real_order


if __name__ == '__main__':
    main()
