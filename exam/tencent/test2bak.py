# coding=utf-8
import sys


def C(x, a):
    sum = 1
    l = range(a)
    for i in l:
        sum *= x
        x -= 1
    for j in l:
        sum /= a
        a -= 1
    return sum


if __name__ == "__main__":
    # 读取第一行的n
    k = int(sys.stdin.readline().strip())
    ans = 0
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    a,x,b,y = map(int, line.split())
    # print(a,x,b,y)
    if True:
        for i in range(0,k/a):
            if (k-i*a)%b==0:
                ans+=C(x,i)*C(y,(k-i*a)/b)
    else:
        for i in range(0,k/b):
            if (k-i*b)%a==0:
                ans+=C(x,(k-i*b)/a)*C(y,i)
    print ans%1000000007
