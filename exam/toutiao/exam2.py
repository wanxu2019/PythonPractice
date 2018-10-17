# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 19:35
# @Author  : Json Wan
# @Description : 
# @File    : exam2.py


def main():
    n = int(raw_input())
    m = int(raw_input())
    matrix = []
    s = raw_input()
    while s:
        matrix.append(map(int, s.split()))
        s = raw_input()
    # print matrix

    def get_max(matrix, n, m):
        if len(matrix)==0:
            return 0
        if m == 0:
            return 0
        elif m == 1:
            sub_matrix = filter(lambda x: x[0] <= n,matrix)
            sub_matrix.sort(lambda x, y: cmp(y[1], x[1]))
            if len(sub_matrix) == 0:
                return 0
            else:
                return sub_matrix[0][1]
        else:
            new_one = matrix[-1]
            if n >= new_one[0]:
                # 买
                sub_max_1 = get_max(matrix[:-1], n - new_one[0], m - 1) + new_one[1]
                # 不买
                sub_max_2 = get_max(matrix[:-1], n, m)
                return max(sub_max_1, sub_max_2)
            else:
                return get_max(matrix[:-1], n, m)

    print get_max(matrix, n, m)

'''
130
3
100 380
20 320
40 360
50 310
'''

if __name__ == '__main__':
    main()
