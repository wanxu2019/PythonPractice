# -*- coding: utf-8 -*-
#  @Time        :    2018/3/27 21:48
#  @Author      :    Json Wan
#  @Description :    2018春季实习笔试模拟题目1
#                    判断任意输入的四点是否能够构成一个正方形
#  @File        :    judge_quadrate.py
#  @Place       :    dormitory


import sys
import math


# 计算两点距离
def calc_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))


# 计算三点构成的三角形面积
def calc_area(p_list):
    a = calc_distance(p_list[0], p_list[1])
    b = calc_distance(p_list[0], p_list[2])
    c = calc_distance(p_list[2], p_list[1])
    p = (a + b + c) / 2.0
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


# 判断P1P2与P3P4平行
def is_parallel(p1, p2, p3, p4):
    vector1 = (p1[0] - p2[0], p1[1] - p2[1])
    vector2 = (p3[0] - p4[0], p3[1] - p4[1])
    if vector1[0] * vector2[1] == vector1[1] * vector2[0]:
        return True
    return False


# 判断P1P2与P3P4垂直
def is_vertical(p1, p2, p3, p4):
    vector1 = (p1[0] - p2[0], p1[1] - p2[1])
    vector2 = (p3[0] - p4[0], p3[1] - p4[1])
    if vector1[0] * vector2[0] + vector1[1] * vector2[1] == 0:
        return True
    return False


# 判断是否是三角形
def is_triangle(p1, p2, p3):
    L12 = calc_distance(p1, p2)
    L13 = calc_distance(p1, p3)
    L23 = calc_distance(p3, p2)
    if L12 + L13 > L23 and L12 + L23 > L13 and L13 + L23 > L12:
        return True
    else:
        return False


# 根据三个点获取一个等腰三角形，首个点为顶点，不是等腰三角形则返回None
def get_isosceles_triangle(p1, p2, p3):
    if not is_triangle(p1, p2, p3):
        return None
    L12 = calc_distance(p1, p2)
    L13 = calc_distance(p1, p3)
    L23 = calc_distance(p3, p2)
    if L12 == L13:
        return p1, p2, p3
    elif L12 == L23:
        return p2, p1, p3
    elif L13 == L23:
        return p3, p1, p2
    else:
        return None


# 判断三个点是等腰直角三角形
def is_isosceles_right_angle_triangle(p1, p2, p3):
    triangle = get_isosceles_triangle(p1, p2, p3)
    if triangle is None:
        return False
    else:
        p1, p2, p3 = triangle[0], triangle[1], triangle[2]
    if is_vertical(p1, p2, p1, p3):
        return True
    return False


def is_square_by_me(point_list):
    if not is_isosceles_right_angle_triangle(point_list[0], point_list[1], point_list[2]):
        return False
    if not is_isosceles_right_angle_triangle(point_list[0], point_list[1], point_list[3]):
        return False
    if not is_isosceles_right_angle_triangle(point_list[0], point_list[2], point_list[3]):
        return False
    if not is_isosceles_right_angle_triangle(point_list[3], point_list[1], point_list[2]):
        return False
    return True


# 最优解法：两点之间距离只有两种，2条对角线+4条边
def is_square(point_list):
    d = dict()
    for i in range(len(point_list)):
        for j in range(i + 1, len(point_list)):
            distance = calc_distance(point_list[i], point_list[j])
            if distance not in d.keys():
                d[distance] = 1
            else:
                d[distance] += 1
    if len(d.keys()) != 2:
        return False
    else:
        if d[d.keys()[0]] == 4 and d[d.keys()[1]] == 2:
            return True
        elif d[d.keys()[1]] == 4 and d[d.keys()[0]] == 2:
            return True
    return False


def run():
    n = int(raw_input("Please input data list size:").strip())
    # n = int(sys.stdin.readline().strip())
    ans = []
    for i in range(n):
        print("Please input x array:")
        line = sys.stdin.readline().strip()
        values_x = map(int, line.split())
        print("Please input y array:")
        line = sys.stdin.readline().strip()
        values_y = map(int, line.split())
        p = 0
        point_list = zip(values_x, values_y)
        if is_square(point_list):
            ans.append("Yes")
        else:
            ans.append("No")

    for x in ans:
        print(x)


def main():
    while True:
        run()


if __name__ == "__main__":
    main()
