# -*- coding: utf-8 -*-
#  @Time        :    2018/11/10 0:16
#  @Author      :    Json Wan
#  @Description :
#  @File        :    Predict the Winner.py
#  @Place       :    dormitory
'''
题目描述
给定一个非负整数的数组代表得分。有两个玩家 A 和 B，玩家 A 先开始玩，可以从数组两端取出一个数作为自己的得分，然后玩家 B 接着从数组两端取出一个数作为自己的得分，再然后是玩家 A ，以此类推。每一次一个玩家取出一个数后，这个数就会消失。交替游戏知道所有的数字都被取走，得分高的玩家获胜。

给定一个数组，预测玩家 A 是否能获胜。假设两个玩家都采用最优策略。

样例
Input: [1, 5, 2]
Output: False
解释: 初始时，玩家 A 可以在 1 和 2 中选择。
如果他选择了 2 （或 1），则玩家B可以选择 1 （或 2）或者 5。如果玩家 B 选择了 5，则玩家A只剩下 1 （或 2）可以选。
所以，最终玩家 A 的得分是 1 + 2 = 3，玩家 B 是 5。
因此，玩家 A 永远都不可能获胜，应该返回 False。
Input: [1, 5, 233, 7]
Output: True
解释: 玩家 A 首先选择 1。接着玩家 B 只能在 5 和 7 之间选择。无论玩家B选择哪个数字，玩家 A 都可以选择 233。
最终，玩家 A (234) 比玩家 B (12) 有更多的分数，所以需要返回 True 代表玩家 A 可以获胜。

注意
1 <= 数组长度 <= 20。
数组中的非负整数不超过 10^7。
如果最后两个玩家得分相同，则玩家 A 也是赢家。
算法
(动态规划) O(n2)O(n2)
从最简单的问题开始考虑，假设只有一个数字，则只能玩家 A 选择这个数字。
接着，问题的规模开始扩大，扩大后，两个玩家会有两种决策，一种是选择数组头部，一种是选择数组尾部，而这两种情况下的子问题都可以提前计算出。至此，动态规划的思路已经很明显。
令 f(i,j)f(i,j) 表示闭区间 [i,j][i,j] 下玩家 A 所能获得的最大分数。
每次 f(i,j)f(i,j) 转移有两种情况：当这一次是玩家 A 取数时，f(i,j)=max(f(i+1,j)+nums[i],f(i,j−1)+nums[j])f(i,j)=max(f(i+1,j)+nums[i],f(i,j−1)+nums[j]) 表示从头部取或者从尾部取，二者最优；当这一次是玩家 B 取数时，玩家B肯定希望自己的得分最大，这必然会导致玩家 A 的得分变小，故此时 f(i,j)=min(f(i+1,j),f(i,j−1))f(i,j)=min(f(i+1,j),f(i,j−1))。
初始时，若最后一次是玩家 A 取数，则 f(i,i)=nums[i]f(i,i)=nums[i]；否则 f(i,i)=0f(i,i)=0。
最后玩家 A 能获得的最大得分就是 f(0,n−1)f(0,n−1)。
时间复杂度
动态规划的状态数为 O(n2)O(n2) ，决策数为 O(1)O(1) ，且每次只需要 O(1)O(1) 的时间转移，故总时间复杂度为 O(n2)O(n2) 。

作者：wzc1995
链接：https://www.acwing.com/solution/leetcode/content/392/
来源：AcWing
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


def get_max_value(arr):
    n = len(arr)
    f = [[0 for i in range(n)] for j in range(n)]
    turn = n & 1
    for i in range(n):
        if turn == 1:
            f[i][i] = arr[i]
        else:
            f[i][i] = 0
    for l in range(2, n + 1):
        turn ^= 1
        for i in range(n - l + 1):
            j = i + l - 1
            if turn == 1:
                f[i][j] = max(f[i + 1][j] + arr[i], f[i][j - 1] + arr[j])
            else:
                f[i][j] = min(f[i + 1][j], f[i][j - 1])
    print(f)
    return f[0][n - 1]


def main():
    print(get_max_value([1, 5, 2]))
    print(get_max_value([1, 5, 233, 7]))
    pass


if __name__ == '__main__':
    main()
