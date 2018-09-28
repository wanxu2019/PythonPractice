# -*- coding: utf-8 -*-
#  @Time        :    2018/9/27 14:56
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    如何添加运算符.py
#  @Place       :    dormitory

# 说明：因为做算法题时间比较紧，所以才用Python写的，请见谅。

def main():
    N, M = map(int, raw_input().split())

    def genArr(n):
        if n == 1:
            return [[1]]
        else:
            result = []
            sub_result = genArr(n - 1)
            for x in sub_result:
                x.append("+")
                x.append(n)
                result.append(x)
                x = x[:-2]
                x.append("-")
                x.append(n)
                result.append(x)
                x = x[:-2]
                x.append(n)
                result.append(x)
            return result

    count = 0
    for x in genArr(N):
        if eval("".join(map(str, x))) == M:
            count += 1
    print(count)


if __name__ == '__main__':
    main()
