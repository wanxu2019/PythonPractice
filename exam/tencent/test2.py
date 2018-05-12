# coding=utf-8
import sys


def C(x, a):
    sum = 1
    list_a = range(1,a+1)
    list_a_copy = range(1,a+1)
    for i in list_a_copy:
        sum *= x
        x -= 1
        for y in list_a:
            if sum%y==0:
                sum/=y
                list_a.remove(y)
    return sum

print(C(5,2))
if __name__ == "__main__":
    # 读取第一行的n
    k = int(sys.stdin.readline().strip())
    ans = 0
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    a,x,b,y = map(int, line.split())
    # print(a,x,b,y)
    if a>b:
        for i in range(0,k/a):
            if (k-i*a)%b==0:
                ans+=C(x,i)*C(y,(k-i*a)/b)
                # print("C({0},{1})={2}".format(x,i,C(x,i)))
                # print("C({0},{1})={2}".format(y,(k-i*a)/b,C(y,(k-i*a)/b)))
    else:
        for i in range(0,k/b):
            if (k-i*b)%a==0:
                ans+=C(x,(k-i*b)/a)+C(y,i)
    print ans
