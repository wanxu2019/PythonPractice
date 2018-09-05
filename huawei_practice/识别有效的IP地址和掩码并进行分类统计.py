# -*- coding: utf-8 -*-
#  @Time        :    2018/9/5 7:54
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    识别有效的IP地址和掩码并进行分类统计.py
#  @Place       :    dormitory
'''
要点：掩码的数量是有限的，可以枚举

'''
import sys

A = 0
B = 0
C = 0
D = 0
E = 0
err = 0
pri = 0
lll = ['254', '252', '248', '240', '224', '192', '128', '0']


def check_ip(ip):
    if len(ip) != 4 and '' in ip:
        return False
    else:
        for i in range(4):
            if int(ip[i]) < 0 or int(ip[i]) > 255:
                return False
        else:
            return True


def check_mask(ms):
    if len(ms) != 4:
        return False
    if ms[0] == '255':
        if ms[1] == '255':
            if ms[2] == '255':
                if ms[3] in lll:
                    return True
                else:
                    return False
            elif ms[2] in lll and ms[3] == '0':
                return True
            else:
                return False
        elif ms[1] in lll and ms[2] == ms[3] == '0':
            return True
        else:
            return False
    elif ms[0] in lll and ms[1] == ms[2] == ms[3] == '0':
        return True
    else:
        return False


while True:
    string = sys.stdin.readline().strip()
    if string == "":
        break
    list1 = string.split("~")[0]
    list2 = string.split("~")[1]
    ip = list1.split('.')
    ms = list2.split('.')
    if check_mask(ms) and check_ip(ip):
        if 1 <= int(ip[0]) <= 126:
            A += 1
        if 128 <= int(ip[0]) <= 191:
            B += 1
        if 192 <= int(ip[0]) <= 223:
            C += 1
        if 224 <= int(ip[0]) <= 239:
            D += 1
        if 240 <= int(ip[0]) <= 255:
            E += 1
        if int(ip[0]) == 10 or (int(ip[0]) == 172 and 15 < int(ip[1]) < 32) or (
                int(ip[0]) == 192 and int(ip[1]) == 168):
            pri += 1
    else:
        err += 1
print "%s %s %s %s %s %s %s" % (A, B, C, D, E, err, pri)
