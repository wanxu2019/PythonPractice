# -*- coding: utf-8 -*-
#  @Time        :    2018/9/27 19:38
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test2.py
#  @Place       :    dormitory
'''
s="catsanddog"
dict="cat","cats","and","sand","dog"
'''
import re

def main():
    p1=re.compile("\"(\w*)\"")
    s=p1.findall(raw_input())
    d=p1.findall(raw_input())
    # print s
    # print d
    def wordBreak(s,d):
        if len(s)==0:
            return [""]
        if len(d)==0:
            return []
        flag=False
        for i in range(len(s)-1,-1,-1):
            subStr=s[i:]
            if subStr in d:
                flag=True
                break
        if not flag:
            return []
        else:
            result=[]
            for i in range(1,len(s)+1):
                subStr=s[:i]
                if subStr in d:
                    subResult=wordBreak(s[i:],d)
                    if len(subResult)>0:
                        for x in subResult:
                            result.append((subStr+" "+x).strip())
            return result
    print wordBreak(s[0],d)
    pass


if __name__ == '__main__':
    main()
