# -*- coding: utf-8 -*-
#  @Time        :    2018/9/20 20:44
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test2.py
#  @Place       :    dormitory

'''
5
bytedance
toutiaohao
toutiaoapp
iesaweme
iestiktok
'''


def main():
    n = int(raw_input())
    arr = []
    for i in range(n):
        arr.append(raw_input())
    result = []
    for i in range(len(arr)):
        x = arr[i]
        for j in range(1, len(x)):
            prefix = x[:j]
            flag = True
            for remain_s in arr[:i] + arr[i + 1:]:
                if remain_s.startswith(prefix):
                    flag = False
                    break
            if flag:
                result.append(prefix)
                break
    for x in result:
        print x


if __name__ == '__main__':
    main()
