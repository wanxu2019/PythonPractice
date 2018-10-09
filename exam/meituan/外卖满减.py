# -*- coding: utf-8 -*-
# @Time    : 2018/10/9 20:25
# @Author  : Json Wan
# @Description : 
# @File    : 外卖满减.py


def main():
    n, x = map(int, raw_input().split())
    arr = map(int, raw_input().split())

    def get(arr, x):
        big_arr = filter(lambda a: a >= x, arr)
        if len(big_arr) > 0:
            return min(big_arr)
        min_cost = sum(arr)
        for i in range(len(arr)):
            choosed = arr[i]
            sub_arr = arr[:i] + arr[i + 1:]
            cost = choosed + get(sub_arr, x - choosed)
            if cost < min_cost:
                min_cost = cost
        return min_cost

    print(get(arr, x))


if __name__ == '__main__':
    main()
