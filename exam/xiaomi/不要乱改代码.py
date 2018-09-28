# -*- coding: utf-8 -*-
#  @Time        :    2018/9/10 18:18
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    不要乱改代码.py
#  @Place       :    dormitory

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # 返回处理后的结果
    inputs=line.split(";")
    records_list=inputs[1:]
    zombies=inputs[0].split()
    records_dict=dict()
    for record in records_list:
        segs=record.split()
        records_dict[segs[0]]=segs[1:]
    # 先统计出每个人都编辑过哪些代码
    person_codes=dict()
    for record in records_dict.items():
        for person in record[1]:
            if person not in person_codes.keys():
                person_codes[person]=[record[0]]
            else:
                person_codes[person].append(record[0])
    from Queue import Queue
    queue=Queue()
    for zomb in zombies:
        queue.put(zomb)
    visited=zombies[:]
    while not queue.empty():
        zomb=queue.get()
        # 遍历他编辑过的代码
        if zomb in person_codes.keys():
            codes=person_codes[zomb]
            for code in codes:
                # 遍历代码的编辑者
                for person in records_dict[code]:
                    if person not in zombies:
                        zombies.append(person)
                    if person not in visited:
                        queue.put(person)
                        visited.append(person)
        else:
            pass
    if "neighbor_wang" in zombies:
        return "go die"
    return "good programmer"

def main():
    print(solution("xiaohong xiaoqiang;Main.java neighbor_wang xiaoming;IndexController.java xiaohong xiaomingxiaohong god;DoSomeService.java xiaoqiang neighbor_wang;MagicCode.scala junjun xiaohong"))
    pass


if __name__ == '__main__':
    main()
