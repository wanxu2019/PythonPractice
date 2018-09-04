# -*- coding: utf-8 -*-
#  @Time        :    2018/9/4 23:05
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    质数因子.py
#  @Place       :    dormitory

import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % 2 == 0:
            return False
    return True


def genPrime(n):
    result = []
    for i in range(2, n+1):
        if isPrime(i):
            result.append(i)
    return result


while True:
    try:
        n = long(raw_input())
        primes = genPrime(n)
        i = 0
        while i < len(primes) and n > 1:
            if n % primes[i] == 0:
                print primes[i],
                n = n / primes[i]
            else:
                i += 1
    except:
        break
