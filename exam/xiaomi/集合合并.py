# -*- coding: utf-8 -*-
#  @Time        :    2018/9/27 14:39
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    集合合并.py
#  @Place       :    dormitory

# 说明：因为做算法题时间比较紧，所以才用Python写的，请见谅。

def main():
    N = int(raw_input())
    allSets = list()
    for i in range(N):
        allSets.append(set(map(int, raw_input().split())))
    change = True
    while change:
        change = False
        for i in range(len(allSets) - 1):
            breakOuter = False
            for j in range(i+1, len(allSets)):
                if len(allSets[i].intersection(allSets[j])) != 0:
                    newAllSets = allSets[:i] + allSets[i + 1:j] + allSets[j + 1:]
                    newAllSets.append(allSets[i].union(allSets[j]))
                    allSets = newAllSets
                    change = True
                    breakOuter = True
                    break
            if breakOuter:
                break
    print(len(allSets))
    maxSize = 0
    for x in allSets:
        if len(x) > maxSize:
            maxSize = len(x)
    print(maxSize)


if __name__ == '__main__':
    main()
