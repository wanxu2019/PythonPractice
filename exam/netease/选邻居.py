# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

if __name__ == "__main__":
    def solve(fill_num, blank_num):
        if fill_num <= 1 or blank_num <= 1:
            return 0, 0
        min_num = 0
        if fill_num == blank_num:
            max_num = fill_num - 1
        elif fill_num > blank_num:
            max_num = blank_num
        else:
            max_num = fill_num - 1
        return min_num, max_num

    # 读取第一行的n
    n = int(raw_input())
    ans_list = []
    for i in range(n):
        # 读取每一行
        line = raw_input()
        # 把每一行的数字分隔后转化成int列表
        values = map(int, line.split())
        ans_list.append(solve(values[1], values[0] - values[1]))
    for ans in ans_list:
        print("%d %d" % (ans[0], ans[1]))
