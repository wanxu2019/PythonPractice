# -*- coding: utf-8 -*-
#  @Time        :    2018/10/29 18:59
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test2.py
#  @Place       :    dormitory

class Fraction(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def gcd(self, a, b):
        if a % b == 0:
            return b
        else:
            return self.gcd(b, a % b)

    def simplify(self):
        n = self.gcd(abs(self.a), abs(self.b))
        self.a /= n
        self.b /= n

    def __add__(self, other):
        v = Fraction(self.a * other.b + self.b * other.a, self.b * other.b)
        v.simplify()
        return v

    def __sub__(self, other):
        v = Fraction(self.a * other.b - self.b * other.a, self.b * other.b)
        v.simplify()
        return v

    def __mul__(self, other):
        v = Fraction(self.a * other.a, self.b * other.b)
        v.simplify()
        return v

    def __div__(self, other):
        v = Fraction(self.a * other.b, self.b * other.a)
        v.simplify()
        return v

    def __str__(self):
        s = ""
        if self.a * self.b < 0:
            s += "-"
        a = abs(self.a)
        b = abs(self.b)
        integer = a // b
        a = a % b
        if integer==0 and a==0:
            return "0"
        if a == 0:
            if integer>0:
                s += str(integer)
        else:
            if b == 1:
                if integer>0:
                    s += str(integer) + " " + str(a)
                else:
                    s +=str(a)
            else:
                if integer>0:
                    s += str(integer) + " " + str(a) + "/" + str(b)
                else:
                    s += str(a) + "/" + str(b)
        return s


def main():
    def get_one_fraction():
        s1_arr = raw_input().split()
        if len(s1_arr) > 1:
            n = 0
            if s1_arr[0][0] == "-":
                if len(s1_arr[0]) > 1:
                    n = int(s1_arr[0][1:])
            else:
                n = int(s1_arr[0])
            ab_arr = s1_arr[1].split("/")
            a = int(ab_arr[0])
            b = int(ab_arr[1])
            a = a + n * b
            if s1_arr[0][0] == "-":
                a = -a
        else:
            is_neg = False
            if "-" == s1_arr[0][0]:
                is_neg = True
                s1_arr[0] = s1_arr[0][1:]
            if "/" in s1_arr[0]:
                ab_arr = s1_arr[0].split("/")
                a = int(ab_arr[0])
                b = int(ab_arr[1])
            else:
                a = int(s1_arr[0])
                b = 1
            if is_neg:
                a = -a
        return Fraction(a, b)

    num1 = get_one_fraction()
    op = raw_input()
    num2 = get_one_fraction()
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    pass


if __name__ == '__main__':
    main()
