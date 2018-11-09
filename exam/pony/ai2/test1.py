# -*- coding: utf-8 -*-
#  @Time        :    2018/10/29 18:59
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test1.py
#  @Place       :    dormitory
'''
齿轮
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
PonyAI的自动驾驶车辆中有一个神奇的装置包含了N个齿轮，这N个齿轮依次标号为0至N-1。现在这些齿轮被连成了一个环，第i个齿轮分别和第(i-1)和齿轮以及第(i+1)个齿轮相连，第0个齿轮和第N-1个齿轮相连。 当整个装置运作起来的时候，如果两个齿轮啮合（相邻），那么它们必定朝相反的方向旋转，一个顺时针一个逆时针旋转。 这N个齿轮每个都有一个理想的旋转方向，这些信息被一个长度为N的字符串D表示。如果D[i]='L'表示第i个齿轮理想的旋转方向为朝左旋转（逆时针），如果D[i]='R'表示第i个齿轮理想的旋转方向为朝右旋转（顺时针）， 显然，我们的装置不能满足所有齿轮的理想旋转方向。现在我们允许移除这个齿轮环上的一些齿轮，使得剩下的齿轮能够同时向其理想的方向旋转。你需要计算出最小需要移除的齿轮数量。 注意，当移除了一个齿轮之后，会在和它啮合的两个齿轮间创造一个间隙，例如移除了齿轮7之后，齿轮6和齿轮8不再啮合，转动方向不再受彼此约束。

输入
一行一个由'L'和'R'构成的字符串，字符串的长度大于等于3小于等于50。

输出
一行一个整数，表示最小需要移除的齿轮个数。

样例输入
LRRR
样例输出
1

Hint
移除了齿轮2之后，其它三个齿轮可以朝其理想的方向旋转。

'''
global_dict = dict()


def main():
    s = raw_input()

    def get(s):
        if s in global_dict:
            return global_dict[s]
        if len(s) <= 1:
            global_dict[s] = 0
            return 0
        elif len(s) == 2:
            if s[0] == s[1]:
                global_dict[s] = 1
                return 1
            else:
                global_dict[s] = 0
                return 0
        elif len(s) == 3:
            if s[1] != s[0] and s[1] != s[2]:
                global_dict[s] = 0
                return 0
            else:
                global_dict[s] = 1
                return 1
        else:
            need_remove = False
            for i in range(1, len(s) - 1):
                if s[i] == s[i - 1] or s[i] == s[i + 1]:
                    need_remove = True
                    break
            if not need_remove:
                global_dict[s] = 0
                return 0
            min_count = len(s) / 2
            for i in range(len(s)):
                if (i > 0 and s[i] == s[i - 1]) or (i < len(s) - 1 and s[i] == s[i + 1]):
                    count = 1 + get(s[:i]) + get(s[i + 1:])
                    if count < min_count:
                        min_count = count
            if not need_remove:
                min_count = 0
            global_dict[s] = min_count
            return min_count

    print(get(s))


# LRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLRLLR
# 10


if __name__ == '__main__':
    main()
