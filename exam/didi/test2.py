# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 20:09
# @Author  : Json Wan
# @Description : 
# @File    : test2.py


def main():
    t = int(raw_input())
    result = []

    # 0
    def get(m, n, d, start):
        if m == 1:
            if start == 0:
                return [[0, 1, 1, 0]]
            elif start == 1:
                return [[1, 1, 0, 1]]
            else:
                raise Exception("Start not right")
        else:
            sub_result = get(m - 1, n, d, start)
            result = []
            for x in sub_result:
                if x[0] == 0:
                    if x[2] < n / 2:
                        if x[1] < d:
                            # 分裂出两种
                            # 继续做0
                            new_x_1 = x[:]
                            new_x_1[1] += 1
                            new_x_1[2] += 1
                            result.append(new_x_1)
                            # 开始做1
                            new_x_2 = x[:]
                            new_x_2[0] = 1
                            new_x_2[1] = 1
                            new_x_2[3] += 1
                            result.append(new_x_2)
                        else:
                            # 只能做1
                            new_x_3 = x[:]
                            new_x_3[0] = 1
                            new_x_3[1] = 1
                            new_x_3[3] += 1
                            result.append(new_x_3)
                    else:
                        # 只能做1
                        new_x_4 = x[:]
                        new_x_4[0] = 1
                        new_x_4[1] = 1
                        new_x_4[3] += 1
                        result.append(new_x_4)
                else:
                    if x[2] < n / 2:
                        if x[1] < d:
                            # 分裂出两种
                            # 继续做1
                            new_x_1 = x[:]
                            new_x_1[1] += 1
                            new_x_1[3] += 1
                            result.append(new_x_1)
                            # 开始做0
                            new_x_2 = x[:]
                            new_x_2[0] = 0
                            new_x_2[1] = 1
                            new_x_2[2] += 1
                            result.append(new_x_2)
                        else:
                            # 只能做0
                            new_x_3 = x[:]
                            new_x_3[0] = 0
                            new_x_3[1] = 1
                            new_x_3[2] += 1
                            result.append(new_x_3)
                    else:
                        # 只能做0
                        new_x_4 = x[:]
                        new_x_4[0] = 0
                        new_x_4[1] = 1
                        new_x_4[2] += 1
                        result.append(new_x_4)
            return result

    def get_final(n, d):
        count = 0
        for start in [0, 1]:
            result = get(n, n, d, start)
            for x in result:
                if x[0] != start:
                    count += 1
        return count

    for i in range(t):
        n, d = map(int, raw_input().split())
        result.append(get_final(n, d))
    for x in result:
        print x
    pass


if __name__ == '__main__':
    main()
