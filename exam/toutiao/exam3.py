# -*- coding: utf-8 -*-
# @Time    : 2018/10/8 20:01
# @Author  : Json Wan
# @Description : 
# @File    : exam3.py



def main():

    N=int(raw_input())

    def genArr(s):
        n=len(s)
        if n == 1:
            return [[s],["-",s]]
        else:
            result = []
            sub_result = genArr(s[:-1])
            for x in sub_result:
                x.append("+")
                x.append(s[-1])
                result.append(x)
                x = x[:-2]
                x.append("-")
                x.append(s[-1])
                result.append(x)
                x = x[:-2]
                x.append(s[-1])
                result.append(x)
            return result

    arr=[]
    for i in range(N):
        s = raw_input()
        count = 0
        sArr=genArr(s)
        # print sArr
        for x in sArr:
            if eval("".join(map(str, x))) == 0:
                count += 1
        arr.append(count)
    for x in arr:
        print(x)


if __name__ == '__main__':
    main()