# -*- coding: utf-8 -*-
#  @Time        :    2018/9/8 20:15
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    香槟塔.py
#  @Place       :    dormitory
'''
香槟塔：很高的香槟塔，A发出两种指令，指令1是向X层倒入体积V的香槟，
指令2是询问第k层香槟体积为多少 输入描述：
第一行为n,m表示香槟塔的总层数和指令数。
第二行为n个整数a，表示每层香槟塔的容量。
第三行到第2+m行有两种输入，一种是“1 k”表示询问第k层当前有多少香槟
另一种是“2 x y”表示往x层倒入体积v的香槟。
1<=n,m<=200000;1<=a,v<=1000000000.
示例：
输入：
1 2
8
2 1 9
1 1
输出:
8
示例：
输入：
5 4
1 2 2 10 1
1 3
2 2 5
2 4 3
1 4
输出：
0
4
'''


def main():
    n, m = map(int, raw_input().split())
    volumes = map(int, raw_input().split())
    volumes = [0] + volumes
    nums = [0 for i in range(n + 1)]

    for i in range(m):
        commands = map(int, raw_input().split())
        if commands[0] == 1:
            # 查询
            print(nums[commands[1]])
        elif commands[0] == 2:
            # 倒香槟
            nums[commands[1]] += commands[2]
            i = commands[1]
            while nums[i] > volumes[i]:
                # 往下一层流
                if i < n:
                    nums[i + 1] += nums[i] - volumes[i]
                nums[i] = volumes[i]
                i += 1


if __name__ == '__main__':
    main()
