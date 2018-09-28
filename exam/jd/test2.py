# -*- coding: utf-8 -*-
#  @Time        :    2018/9/9 18:49
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test2.py
#  @Place       :    dormitory


def main():
    test_num = int(raw_input())
    results=[]

    # 从all_list中选choices_num个的选法
    def gen_choices(all_list,choices_num):
        results=[]
        if choices_num==1:
            for x in all_list:
                results.append(set([x]))
        else:
            for x in all_list:
                all_list_copy=all_list[:]
                all_list_copy.remove(x)
                sub_results=gen_choices(all_list_copy,choices_num-1)
                for sub_result in sub_results:
                    sub_result.add(x)
                    if sub_result not in results:
                        results.append(sub_result)
        return results

    # print(gen_choices([1,2,3,4],1))
    # print(gen_choices([1,2,3,4],2))
    # print(gen_choices([1,2,3,4],3))

    # 将all_list分为n组的分法
    def gen_x_groups(all_list,n):
        results=[]
        if n==1:
            # 只有一种分组方法
            results.append([set(all_list)])
        elif n==len(all_list):
            # 只有一种分组方法
            l=[]
            for x in all_list:
                l.append(set([x]))
            results.append(l)
        else:
            # 选一个出来单独分一组，剩下的分n-1组
            for x in all_list:
                all_list_copy=all_list[:]
                all_list_copy.remove(x)
                sub_results=gen_x_groups(all_list_copy,n-1)
                for sub_result in sub_results:
                    sub_result.append(set([x]))
                    results.append(sub_result)
            # 选一个出来，将剩下的分为n组，x再往每组里面加
            for x in all_list:
                all_list_copy=all_list[:]
                all_list_copy.remove(x)
                sub_results=gen_x_groups(all_list_copy,n)
                for sub_result in sub_results:
                    for i in range(len(sub_result)):
                        sub_result_copy=[]
                        for _set in sub_result:
                            ss=set()
                            for xx in _set:
                                ss.add(xx)
                            sub_result_copy.append(ss)
                        sub_result_copy[i].add(x)
                        if sub_result_copy not in results:
                            results.append(sub_result_copy)
        return results

    # print(gen_x_groups([1,2,3],1))
    # print(gen_x_groups([1,2,3],2))
    # print(gen_x_groups([1,2,3],3))
    # print(gen_x_groups([1,2,3,4],1))
    print(gen_x_groups([1,2,3,4],3))

    return
    # 得到所有可能的分组
    def gen_groups(n):
        all_list=range(1,n+1)
        results=[]
        for i in range(1,n+1):
            # 一共分为i组的分法
            for x in gen_x_groups(all_list,i):
                results.append(x)
        return results

    # 组内无连接
    def no_conn_in_group(group,edges):
        conn_list=gen_choices(list(group),2)
        for conn in conn_list:
            if set(conn) in edges:
                return False
        return True

    # 组间有连接
    def has_conn_between_groups(group1,group2,edges):
        for x in group1:
            for y in group2:
                if set([x,y]) in edges:
                    return True
        return False

    def is_all_graph(n,edges):
        # todo:
        # 分组
        all_list=gen_groups(n)
        for x in all_list:
            pass
        return True
    for i in range(test_num):
        n,m=map(int,raw_input().split())
        edges=set()
        for j in range(m):
            edges.add(set(map(int,raw_input().split())))
        if is_all_graph(n,edges):
            results.append("Yes")
        else:
            results.append("No")
    for result in results:
        print result
    pass


if __name__ == '__main__':
    main()


'''
2
5 7
1 3
1 5
2 3
2 5
3 4
4 5
3 5

4 3
1 2
2 3
3 4

Yes
No
'''
