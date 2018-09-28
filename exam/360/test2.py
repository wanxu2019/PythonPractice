# -*- coding: utf-8 -*-
#  @Time        :    2018/9/17 20:46
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test2.py
#  @Place       :    dormitory


def main():
    n=int(raw_input())
    def get_count(k,j):
        s=""
        while j>0:
            s+=str(j%k)
            j=j/k
        count=0
        for x in s:
            if x==str(k-1):
                count+=1
        return count

    for i in range(n):
        k,l,r=map(int,raw_input().split())
        max_count=0
        max_one=l
        for j in range(l,r+1):
            count=get_count(k,j)
            if count>max_count:
                max_count=count
                max_one=j
            elif count==max_count and j<max_one:
                max_count=count
                max_one=j
        print max_one
    pass


if __name__ == '__main__':
    main()
