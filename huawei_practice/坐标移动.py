# -*- coding: utf-8 -*-
#  @Time        :    2018/9/5 7:28
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    坐标移动.py
#  @Place       :    dormitory
import re


def is_legal(command):
    if not command:
        return False
    pattern = re.compile("^[ASWD][0-9]{1,2}$")
    ret=pattern.match(command)
    if ret:
        return True
    return False


while True:
    try:
        s = raw_input()
        startX = 0
        startY = 0
        commands = s.split(";")
        for command in commands:
            if is_legal(command):
                if command[0] == 'A':
                    startX += -int(command[1:])
                elif command[0] == 'S':
                    startY += -int(command[1:])
                elif command[0] == 'W':
                    startY += int(command[1:])
                elif command[0] == 'D':
                    startX += int(command[1:])
        print "%d,%d" % (startX, startY)
    except Exception, e:
        break
