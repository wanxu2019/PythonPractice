# -*- coding: utf-8 -*-
#  @Time        :    2018/3/31 13:36
#  @Author      :    Json Wan
#  @Description :    练习动态规划
#  @File        :    dynamic_planning.py
#  @Place       :    dormitory


# 二维解法
def plan(widgets, capacity):
    # 1.生成最大价值矩阵
    value_matrix = [[0 for j in range(capacity + 1)] for i in range(len(widgets) + 1)]
    # 2.遍历行填充价值矩阵
    for i in range(1, len(value_matrix)):
        for j in range(1, capacity + 1):
            # 第i个物品，对应于能力j时的最大价值
            widget = widgets[i - 1]
            # 有能力拿这个物品
            if j >= widget['price']:
                # 选择不拿这个物品的价值
                v1 = value_matrix[i - 1][j]
                # 选择拿这个物品的价值,剩给之前的所有的物品的空间就只有j-widget['price']
                v2 = widget['value'] + value_matrix[i - 1][j - widget['price']]
                value_matrix[i][j] = max(v1, v2)
            else:
                # 根本就拿不了这个物品
                value_matrix[i][j] = value_matrix[i - 1][j]
    # 3.取出最大价值
    return value_matrix[len(widgets)][capacity], value_matrix


# 回溯求解选择的物品
def solve(widgets, value_matrix):
    answers = []
    widgets_num = len(widgets)
    capacity = len(value_matrix[0]) - 1
    if capacity <= 0:
        return [[0 for i in range(len(widgets))]]
    if len(widgets) == 0:
        return [[]]
    sub_widgets = widgets[:widgets_num - 1]
    # 相同容量下价值比前一项价值大，则说明选择了该物品
    if value_matrix[widgets_num][capacity] > value_matrix[widgets_num - 1][capacity]:
        sub_matrix = map(lambda x: x[:capacity+1 - widgets[widgets_num - 1]['price']], value_matrix[:widgets_num])
        sub_answers = solve(sub_widgets, sub_matrix)
        for ans in sub_answers:
            answers.append([1]+ans)
        return answers
    # 相同容量下价值与前一项价值相同，则有可能选择了该物品，也有可能没选
    else:
        # 如果选择了该项物品之后价值达不到当前最大价值，则说明没选，如果能力不够，肯定也没选
        if capacity < widgets[widgets_num-1]['price'] or widgets[widgets_num - 1]['value'] + value_matrix[widgets_num - 1][
                    capacity - widgets[widgets_num - 1]['price']] < value_matrix[widgets_num][capacity]:
            sub_matrix = value_matrix[:widgets_num]
            sub_answers = solve(sub_widgets, sub_matrix)
            for ans in sub_answers:
                answers.append([0]+ans)
            return answers
        else:
            # 两种可能
            # 没选择这一个
            sub_matrix_1 = value_matrix[:widgets_num]
            sub_answers_1 = solve(sub_widgets, sub_matrix_1)
            # print(sub_answers_1)
            for ans in sub_answers_1:
                answers.append([0]+ans)
            # 选择了这一个
            sub_matrix_2 = map(lambda x: x[:capacity+1 - widgets[widgets_num - 1]['price']], value_matrix[:widgets_num])
            sub_answers_2 = solve(sub_widgets, sub_matrix_2)
            # print(sub_answers_2)
            for ans in sub_answers_2:
                answers.append([1]+ans)
            return answers


# 一维解法
def plan2(widgets, capacity):
    pass


def main():
    widgets = [
        {
            "price": 2,
            "value": 3
        },
        {
            "price": 1,
            "value": 2
        },
        {
            "price": 3,
            "value": 6
        },
        {
            "price": 4,
            "value": 3
        },
        {
            "price": 5,
            "value": 8
        },
        {
            "price": 6,
            "value": 12
        },
        {
            "price": 7,
            "value": 13
        },
    ]
    for v in range(1,29):
        print "volume=",v
        max_value, value_matrix = plan(widgets, v)
        print "max_value=",(max_value)
        print(map(lambda x:list(reversed(x)),solve(widgets, value_matrix)))


if __name__ == '__main__':
    main()
