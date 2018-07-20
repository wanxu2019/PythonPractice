# coding:utf-8
from time import time


# 最容易想到的解法：
# 将任务分解成规模更小的子任务组合，再递归求解
def get_max_money_recursion(arr):
    start_time = time()
    if len(arr) <= 2:
        return max(arr),time() - start_time
    # 偷arr[0]，则arr[1]不能偷，得到的最大money如下：
    money1 = arr[0] + get_max_money_recursion(arr[2:])[0]
    # 不偷arr[0]，则之后的都可以偷，得到的最大money如下：
    money2 = get_max_money_recursion(arr[1:])[0]
    # 选择两个子任务的最大值即可
    return max(money1, money2), time() - start_time


# 高效解法：动态规划
def get_max_money_dp(arr):
    start_time = time()
    # f(n)=max(arr[0]+f(n-2),f(n-1))
    # f(1)=arr[0]
    # f(2)=max(arr[0],arr[1])
    max_value_1 = arr[0]
    if len(arr) == 1:
        return max_value_1
    max_value_2 = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        # 从简单问题开始，逐步迭代求出复杂问题的解
        max_value_2, max_value_1 = max(max_value_2, max_value_1 + arr[i]), max_value_2
    return max_value_2, time() - start_time


def test_data():
    yield [1, 2, 3, 1]
    yield [2, 7, 9, 3, 1]
    yield [1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3]
    yield [183, 219, 57, 193, 94, 233, 202, 154, 65, 240, 97, 234, 100, 249, 186, 66, 90, 238, 168, 128, 177, 235, 50,
           81,
           185, 165, 217, 207, 88, 80, 112, 78, 135, 62, 228, 247, 211]


for data in test_data():
    print "data:", data
    result = get_max_money_dp(data)
    print "solution by dynamic planning:", result[0], ", time consuming:", result[1]
    result = get_max_money_recursion(data)
    print "solution by recursion:", result[0], ", time consuming:", result[1]
