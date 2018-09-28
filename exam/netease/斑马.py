# -*- coding: utf-8 -*-
#  @Time        :    2018/9/8 14:57
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    斑马.py
#  @Place       :    dormitory


import sys

if __name__ == "__main__":
    # 读取每一行
    line = sys.stdin.readline().strip()
    def get_max_length(s):
        max_count=0
        count=0
        for i in range(len(s)-1):
            if s[i]!=s[i+1]:
                count+=1
                max_count=max(max_count,count)
            else:
                count=0
        return max_count+1

    # print(get_max_length("wbwbwbwbwb"))
    # print(get_max_length("wbbbwbwwww"))
    # print(get_max_length("wbw"))
    # print(get_max_length("wbwwww"))
    # print(get_max_length("bbwwbbwwbwbw"))
    max_count=0
    count=0
    print(min(len(line),get_max_length(line+line)))
    for i in range(len(line)):
        for j in range(i+2,len(line)+1):
            seg=list(line[i:j])
            seg.reverse()
            new_line=line[:i]+"".join(seg)+line[j:]
            #print new_line
            count=get_max_length(new_line)
            max_count=max(max_count,count)
    print(max_count)
