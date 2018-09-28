# -*- coding: utf-8 -*-
#  @Time        :    2018/9/13 18:24
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    打羽毛球的小爱同学.py
#  @Place       :    dormitory
"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # 返回处理后的结果
    a,b,c,d = map(int, line.split(" "))
    return 2**(a+c)+(b+d)*2**(a+c)+b*(b-1)/2*2**a

def main():
    print solution("1 1 1 1")
    pass


if __name__ == '__main__':
    main()
