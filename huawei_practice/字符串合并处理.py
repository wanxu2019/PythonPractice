# -*- coding: utf-8 -*-
#  @Time        :    2018/9/5 11:43
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    字符串合并处理.py
#  @Place       :    dormitory


while True:
    try:
        s="".join(raw_input().split())
        even_s=""
        odd_s=""
        for i in range(len(s)):
            if i%2==0:
                odd_s+=s[i]
            else:
                even_s+=s[i]
        even_s="".join(sorted(even_s))
        odd_s="".join(sorted(odd_s))
        result=""
        def convert(ch):
            d={
                #F:1111:1111:F
                "F":"F",
                #E:1110:0111:7
                "E":"7",
                #D:1101:1011:B
                "D":"B",
                #C:1100:0011:3
                "C":"3",
                #B:1011:1101:D
                "B":"D",
                #A:1010:0101:5
                "A":"5",
                #9:1001:1001:9
                "9":"9",
                #8:1000:0001:1
                "8":"1",
                #7:0111:1110:E
                "7":"E",
                #6:0110:0110:6
                "6":"6",
                #5:0101:1010:A
                "5":"A",
                #4:0100:0010:2
                "4":"2",
                #3:0011:1100:C
                "3":"C",
                #2:0010:0100:4
                "2":"4",
                #1:0001:1000:8
                "1":"8",
                #0:0000:0000:0
                "0":"0",
            }
            if '0'<=ch.upper()<='9' or 'A'<=ch.upper()<='F':
                return d[ch.upper()]
            return ch
        i=0
        while i<len(even_s):
            result+=convert(odd_s[i])
            result+=convert(even_s[i])
            i+=1
        if i<len(odd_s):
            result+=convert(odd_s[i])
        print result
    except Exception,e:
        break



while True:
    try:
        line = raw_input().split()
        line = line[0]+line[1]
        lineA , lineB, lineRes, lineTrans= '' , '', '', ''
        for i in range(len(line)):
            if i%2 == 0:
                lineA += line[i]#oushu
            else :
                lineB += line[i]#jishu
        lineA, lineB = sorted(lineA), sorted(lineB)
        for i in range(len(lineB)):
            lineRes += lineA[i]
            lineRes += lineB[i]
        if len(lineA) > len(lineB):
            lineRes += lineA[i+1]
        for i in lineRes:
            # bin函数以及这波翻转的操作可以借鉴
            if i in '0123456789abcdefABCDEF':
                temp = bin(int('0x'+i,16))[2:]
                temp = (4-len(temp))*'0' + temp
                temp = (hex(int(temp[::-1],2))[2:]).upper()
            else:
                temp = i
            lineTrans += temp
        print lineTrans
    except:
        break
