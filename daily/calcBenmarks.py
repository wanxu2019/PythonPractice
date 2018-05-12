# -*- coding: utf-8 -*-
#  @Time        :    2018/3/29 0:33
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    calcBenmarks.py
#  @Place       :    dormitory
import math


def calc_overlap_rate(x1, y1, x2, y2, x3, y3, x4, y4):
    overlap_x = max(math.fabs(x2 - x1) + math.fabs(x4 - x3) - (max(x2, x4) - min(x1, x3)), 0)
    overlap_y = max(math.fabs(y2 - y1) + math.fabs(y4 - y3) - (max(y2, y4) - min(y1, y3)), 0)
    return overlap_x * overlap_y / float(math.fabs((x1 - x2) * (y1 - y2)) + math.fabs((x3 - x4) * (y3 - y4))-overlap_x * overlap_y )


def main():
    print(calc_overlap_rate(0, 0, 3, 3, 0, 0, 3, 3))
    print(calc_overlap_rate(0, 0, 3, 3, 1, 1, 3, 3))
    print(calc_overlap_rate(0, 0, 3, 3, 5, 5, 3, 3))
    print(calc_overlap_rate(0, 0, 3, 3, 3, 3, 5, 5))
    print(calc_overlap_rate(0, 0, 3, 3, 2, 2, 3, 3))

    pass


if __name__ == '__main__':
    main()
