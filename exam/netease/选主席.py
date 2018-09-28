# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

if __name__ == "__main__":
    # 读取第一行的n,m
    n, m = map(int, sys.stdin.readline().strip().split(" "))
    d = dict()
    cost_list = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = map(int, line.split())
        t = values[0]
        cost = values[1]
        if t != 1:
            cost_list.append((t, cost))
        if t in d.keys():
            d[t] += 1
        else:
            d[t] = 1

    if 1 not in d.keys():
        d[1] = 0

    cost_list.sort(lambda x, y: cmp(x[1], y[1]))


    def findMaxCount(d):
        l = d.items()
        max_count = 0
        for x in l:
            if x[1] > max_count:
                max_count = x[1]
        result = []
        for x in l:
            if x[1] == max_count:
                result.append(x)
        return result


    def get_least_cost(person, cost_list):
        for cost in cost_list:
            if cost[0] == person[0]:
                return cost[1]
        return 9999


    def solve(d, cost_list):
        max_persons = findMaxCount(d)
        # 将目标人去掉
        max_persons = filter(lambda x: x[0] != 1, max_persons)
        # 若去掉目标人后长度为0说明目标人票数已达最大
        if len(max_persons) == 0:
            return 0
        else:
            # 随便挑一个非1的最高者，随便挑行吗？？
            # 不行，找一个具有最便宜支持者的
            least_cost = 9999
            max_person = max_persons[0]
            for person in max_persons:
                cost = get_least_cost(person, cost_list)
                if cost < least_cost:
                    least_cost = cost
                    max_person = person
            max_person = max_person[0]
            min_p = None
            for p in cost_list:
                if p[0] == max_person:
                    min_p = p
                    break
            if min_p:
                if min_p == cost_list[0]:
                    new_d = dict(d.items())
                    new_d[1] += 1
                    new_d[max_person] -= 1
                    return cost_list[0][1] + solve(new_d, cost_list[1:])
                else:
                    # 选择最高者
                    new_d_1 = dict(d.items())
                    new_d_1[1] += 1
                    new_d_1[max_person] -= 1
                    new_cost_list_1 = cost_list[:]
                    new_cost_list_1.remove(min_p)
                    cost_1 = min_p[1] + solve(new_d_1, new_cost_list_1)
                    new_d_2 = dict(d.items())
                    new_d_2[1] += 1
                    cost_2 = cost_list[0][1] + solve(new_d_2, cost_list[1:])
                    return min(cost_1, cost_2)
            else:
                new_d = dict(d.items())
                new_d[1] += 1
                new_d[max_person] -= 1
                return cost_list[0][1] + solve(new_d, cost_list[1:])

    print(solve(d, cost_list))

'''
7 5
3 1
3 5
4 5
4 5
5 6
5 1
1 1
'''
