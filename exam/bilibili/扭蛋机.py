# -*- coding: utf-8 -*-
#  @Time        :    2018/9/21 15:59
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    扭蛋机.py
#  @Place       :    dormitory


def f(current_n, target_n):
    if current_n == 0 and target_n == 1:
        return [2]
    elif current_n == 0 and target_n == 2:
        return [3]
    else:
        # 边界情况的处理
        if current_n * 2 + 1 == target_n:
            return [2]
        elif current_n * 2 + 2 == target_n:
            return [3]
        elif current_n * 2 + 1 > target_n:
            # 不能这么扭，之前的是错的
            return None
        else:
            # 方案一：扭蛋机1先扭
            sub_solution_1 = f(current_n * 2 + 1, target_n)
            # 方案二：扭蛋机2先扭
            sub_solution_2 = f(current_n * 2 + 2, target_n)
            if not sub_solution_1 and not sub_solution_2:
                return None
            elif not sub_solution_1:
                return [3] + sub_solution_2
            elif not sub_solution_2:
                return [2] + sub_solution_1
            else:
                # 如果两种扭蛋方法都可以，选择一个次数最少的
                if len(sub_solution_1) < len(sub_solution_2):
                    return [2] + sub_solution_1
                else:
                    return [3] + sub_solution_2


def main():
    n = int(raw_input())
    result = f(0, n)
    if result:
        print "".join(map(str, result))


if __name__ == '__main__':
    main()
