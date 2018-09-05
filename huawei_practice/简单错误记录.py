# -*- coding: utf-8 -*-
#  @Time        :    2018/9/5 10:39
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    简单错误记录.py
#  @Place       :    dormitory

import re

records = []
while True:
    try:
        s=""
        subs = raw_input()
        while len(subs)>0:
            s+=subs
            subs=raw_input()
        segs = re.split("\s+", s)
        while len(segs) > 1:
            name = segs[0]
            if name.find("\\") != -1:
                name = name[name.rindex("\\") + 1:]
            name = name[-16:]
            line = segs[1]
            exist = False
            for record in records:
                if record[0] == (name, line):
                    exist = True
                    record[1] += 1
            if not exist:
                records.append([(name, line), 1])
            segs = segs[2:]
        for record in records[-8:]:
            print record[0][0], record[0][1], record[1]
    except Exception,e:
        break
