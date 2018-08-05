# -*- coding: utf-8 -*-
#  @Time        :    2018/8/2 0:04
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    expansion.py
#  @Place       :    dormitory
'''
题目描述：
小明接到一个业务扩容的需求，需要出一份机房机器部署方案，需求如下：
业务扩容需求：一共需要扩容N种机型，对于机型Ni需要扩容Mi台
机房部署要求：现有一排机架，一个机架只能放置12台机器，且只能放置一种机型，对于部署了同种机型的机架在物理上需要间隔n个机架。

举例如下:
现需要扩容A，B两种机型，分别需要30台，20台，同种机型的机架在物理上需要间隔2个机架，则部署方案如下

 -----------------------------------------
|     |     |     |     |    |       |    |
| A12 | B12 |empty| A12 | B8 | empty | A6 |
|     |     |     |     |    |       |    |
 ------------------------------------------
（这里不能贴图，需要看图的可以上iwork）
根据图示一共需要占用7个机架位，各机架部署方式如下
1号机架部署A机型12台
2号机架部署B机型12台
3号机架部署留空
4号机架部署A机型12台
5号机架部署B机型8台
6号机架部署留空
7号机架部署A机型6台
思路：
最容易想到的方法还是递归，先安排一种型号的主机，再接着安排剩下的，把问题简化；
'''


def remove_host_by_type(host_list, host_type):
    '''
    移除主机列表中某种类型的主机并返回移除值
    :param host_list:主机列表
    :param host_type:主机类型
    :return:
    '''
    if not host_list:
        return None
    length = len(host_list)
    i = 0
    while i < length and host_list[i][0] != host_type:
        i += 1
    host = None
    if i < length:
        host = host_list[i]
        host_list.remove(host)
    return host


global_min_num = 0


# 最容易想到的解法：递归求解
def arrange_by_state(arranged_list, need_host_list, n):
    '''
    根据当前状态安排一次主机，进入下一个状态
    :param arranged_list: 已被安排的主机列表
    :param need_host_list: 需要安排的主机列表
    :param n: 间隔数
    :return:
    '''
    global global_min_num
    arranged_list_length = len(arranged_list)
    # 已经安排完了，没有需要安排的了
    if len(need_host_list) == 0:
        if arranged_list_length < global_min_num:
            global_min_num = arranged_list_length
        return arranged_list
    # 先根据已安排的主机情况求得可行域
    avaliable_host_list = need_host_list[:]
    # 将移除可行域的主机存储起来
    removed_host_list = []
    i = 0
    while i < n and i < arranged_list_length:
        removed_host = remove_host_by_type(avaliable_host_list, arranged_list[arranged_list_length - 1 - i][0])
        if removed_host:
            removed_host_list.append(removed_host)
        i += 1
    # 可行域为空，全部是与前面相隔很近的
    if len(avaliable_host_list) == 0:
        # 只能空一个机架再接着安排
        arranged_list.append(('empty', 0))
        # 安排情况已经很坏了，没必要再沿这条路走下去了
        if len(arranged_list)>=global_min_num:
            return None
        return arrange_by_state(arranged_list, removed_host_list, n)
    # 可行域不为空，随机安排一个，遍历找出占用机架最少的安排方法
    else:
        min_result_list = []
        min_frame_num = 0
        for i in range(len(avaliable_host_list)):
            # 大于12台的主机先安排12台
            if avaliable_host_list[i][1] > 12:
                arranged_list.append((avaliable_host_list[i][0], 12))
                avaliable_host_list[i] = (avaliable_host_list[i][0], avaliable_host_list[i][1] - 12)
                # 求得新的需要安排的主机列表
                new_need_host_list = removed_host_list + avaliable_host_list
            else:
                # 小于12台的直接安排完
                arranged_list.append(avaliable_host_list[i])
                new_need_host_list = removed_host_list + avaliable_host_list[:i] + avaliable_host_list[i + 1:]
            # 安排情况已经很坏了，没必要再沿这条路走下去了
            if len(arranged_list) >= global_min_num:
                continue
            # 安排完成后进入下一波安排直至求得结果
            result_list = arrange_by_state(arranged_list[:], new_need_host_list, n)
            # 有改良的安排才比对记录
            if result_list:
                if i == 0:
                    min_result_list = result_list
                    min_frame_num = len(min_result_list)
                else:
                    if len(result_list) < min_frame_num:
                        min_result_list = result_list
                        min_frame_num = len(min_result_list)
        return min_result_list


def host_arrange(need_host_list, n):
    """
    arrange host according the rule
    :param need_host_list: [('A', 30), ('B', 20)]
    :param n: 2
    :return: [('A', 12), ('B', 12), ('empty', 0), ('A', 12), ('B', 8), ('empty', 0), ('A', 6)]
    """
    return arrange_by_state([], need_host_list, n)


# 高效解法：动态规划
def host_arrange_by_dp(need_host_list, n):
    pass


def gen_dataset():
    yield [('A', 30), ('B', 20)], 2
    yield [('A', 30), ('B', 20)], 3
    yield [('A', 30), ('B', 40)], 2
    yield [('A', 36), ('B', 36), ('C', 36), ('D', 24)], 2
    yield [('A', 360), ('B', 1200), ('C', 800), ('D', 240)], 3


def main():
    global global_min_num
    test_dataset = gen_dataset()
    for need_host_list, n in test_dataset:
        global_min_num = reduce(lambda x, y: ("sum", x[1] + y[1]), need_host_list)[1] * (n + 1)
        print("机架数量上限：%d" % global_min_num)
        print(host_arrange(need_host_list, n))


if __name__ == '__main__':
    main()
