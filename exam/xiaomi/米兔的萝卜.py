# -*- coding: utf-8 -*-
#  @Time        :    2018/9/10 17:44
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    米兔的萝卜.py
#  @Place       :    dormitory

"""
@param string line 为单行测试数据
@return string 处理后的结果
"""
def solution(line):
    # 缩进请使用 4 个空格，遵循 PEP8 规范
    # 返回处理后的结果
    inputs=line.split(";")
    (N,M,R)=map(int,inputs[0].split())
    arr=map(int,inputs[1].split())
    indexs=map(int,inputs[2].split())
    indexs_orders={}
    indexs_arr={}
    results=[]
    # for i,index in enumerate(indexs):
    #     indexs_orders[index]=i
        # results.append(max(arr[max(0,index-1-R):index-1+R+1]))
    # indexs.sort()
    indexs_copy=indexs[:]
    for j,x in enumerate(arr):
        offset=0
        for i in range(len(indexs)):
            index=indexs[i-offset]
            if index-1-R<=j<=index-1+R:
                if index not in indexs_arr.keys():
                    indexs_arr[index]=[x]
                else:
                    indexs_arr[index].append(x)
            elif i>index-1+R+1:
                indexs.remove(index)
                offset+=1
    for index in indexs_copy:
        results.append(max(indexs_arr[index]))
    for result in results:
        print result,
    return " ".join(map(str,results))

def main():
    solution(raw_input())
    pass


if __name__ == '__main__':
    main()
