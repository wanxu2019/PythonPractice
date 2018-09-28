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
    groups=[]
    visitedSet=set()
    i=0
    while i<len(allSets):
        if i not in visitedSet:
            group=set()
            group.add(i)
            visitedSet.add(i)
            j=i+1
            while j<len(allSets):
                if j not in visitedSet:
                    for index in group:
                        # 只要有一个有交集就是一组的
                        if len(allSets[index].intersection(allSets[j]))>0:
                            group.add(j)
                            visitedSet.add(j)
                            break
                j+=1
            groups.append(group)
        i+=1
    newSets=[]
    for group in groups:
        newSet=set()
        for index in group:
            newSet=newSet.union(allSets[index])
        newSets.append(newSet)
    print(len(newSets))
    maxSize = 0
    for x in newSets:
        if len(x) > maxSize:
            maxSize = len(x)
    print(maxSize)


if __name__ == '__main__':
    main()
