# -*- coding: utf-8 -*-
#  @Time        :    2018/11/10 7:36
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    Beautiful Arrangement.py
#  @Place       :    dormitory
'''
题目描述
假设有从 1 到 N 的 N 个整数，如果从这 N 个数字中成功构造出一个数组，使得数组的第 i 位 (1 <= i <= N) 满足如下两个条件中的一个，我们就称这个数组为一个优美的排列。条件：
1. 第 i 位的数字能被 i 整除。
2. i 能被第 i 位上的数字整除。

现在给定一个整数 N，请问可以构造多少个优美的排列？

样例
输入: 2
输出: 2
解释:

第 1 个优美的排列是 [1, 2]:
  第 1 个位置（i=1）上的数字是1，1能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是2，2能被 i（i=2）整除

第 2 个优美的排列是 [2, 1]:
  第 1 个位置（i=1）上的数字是2，2能被 i（i=1）整除
  第 2 个位置（i=2）上的数字是1，i（i=2）能被 1 整除
注意
N 是一个正整数，并且不会超过 15。
算法
(动态规划，状态压缩) O(n⋅2n)O(n⋅2n)
状态 f(S)f(S) 表示用去的数字集合为 SS的方案数。其中 SS 是一个整数，SS 的二进制表示中，为 0 的数位表示该数字还没被用过，为 1 的数位表示已经被用过。
从 1 开始枚举 SS，保证 f(S)>0f(S)>0（否则没有意义），统计 SS 中用过数字的个数 tottot，然后从 SS 中选择一个没有被使用过的数字ii，然后用tottot 和 ii 判断该数字是否满足题目中的两个条件。若满足，则 f(S | 1 << i) += f(S)。
初始时，f(1<<i)=1f(1<<i)=1。最终答案为 f((1<<n)−1)f((1<<n)−1)。
时间复杂度
状态数为 O(2n)O(2n)，决策数为 O(n)O(n)，转移时间为 O(1)O(1)，故总时间复杂度为 O(n⋅2n)O(n⋅2n)。

作者：wzc1995
链接：https://www.acwing.com/solution/leetcode/content/418/
来源：AcWing
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


def count_arrangement(n):
    f = [0 for i in range(1 << n)]
    for i in range(n):
        f[1 << i] = 1
    for s in range(1, (1 << n)):
        if f[s] > 0:
            tot = 0
            for i in range(n):
                if s & (1 << i) > 0:
                    tot += 1
            for i in range(n):
                if s & (1 << i) == 0 and ((tot + 1) % (i + 1) == 0 or (i + 1) % (tot + 1) == 0):
                    f[s | 1 << i] += f[s]
    return f[(1 << n) - 1]


def main():
    for i in range(1,16):
        print(count_arrangement(i))
    pass


if __name__ == '__main__':
    main()
