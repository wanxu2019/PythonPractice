# -*- coding: utf-8 -*-
#  @Time        :    2018/7/23 1:12
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    FindContinuousSequence.py
#  @Place       :    dormitory
"""
题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
思路：因数分解，根据因数奇偶性分情况讨论即可
序列长度最长为n,则序列的和肯定大于从1开始的n个数的和，也就是S>=n(n+1)/2，也就可以推出n<sqrt(2S)，减少遍历次数
"""


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        import math
        result = []
        for count in range(int(math.sqrt(tsum)), 0, -1):
            # 若能进行因数分解
            if tsum % count == 0:
                # tsum可由count个num相加得到
                num = tsum / count
                # 连续正数序列不可能为偶数个偶数相加，只能为奇数个奇数相加(41=20+21,63=20+21+22)，或奇数个偶数相加(60=19+20+21)，或偶数个奇数相加(82=19+20+21+22)
                if count % 2 == 0 and num % 2 == 0:
                    pass
                elif count % 2 == 0:
                    # 偶数个奇数相加，需要满足一定条件，往前可无限制，但往后不能超过0
                    # 需要往后拓展的数量为count个,(num-1)/2要大于等于count
                    if (num - 1) / 2 >= count:
                        result.append(range((num - 1) / 2 - count + 1, (num + 1) / 2 + count))
                    else:
                        pass
                elif num % 2 == 0:
                    # 奇数个偶数相加，数量必须大于等于2
                    # 需要往后拓展的数量为(count+1)/2个，num是第(count+1)/2个数字
                    if count >= 2 and num >= (count + 1) / 2:
                        result.append(range(num - (count - 1) / 2, num + (count - 1) / 2 + 1))
                else:
                    # 奇数个奇数相加
                    # 第一种情况：需要往后拓展的数量为count个，(num-1)/2是第count个数字
                    if (num - 1) / 2 >= count:
                        result.append(range((num - 1) / 2 - count + 1, (num + 1) / 2 + count))
                    # 第二种情况：需要往后拓展的数量为(count+1)/2个，num是第(count+1)/2个数字
                    elif count>1 and num>=(count+1)/2:
                        result.append(range(num - (count - 1) / 2, num + (count - 1) / 2 + 1))
                    # 对称性
                    if count!=num:
                        count,num=num,count
                        # 第一种情况：需要往后拓展的数量为count个，(num-1)/2是第count个数字
                        if (num - 1) / 2 >= count:
                            result.append(range((num - 1) / 2 - count + 1, (num + 1) / 2 + count))
                        # 第二种情况：需要往后拓展的数量为(count+1)/2个，num是第(count+1)/2个数字
                        elif count > 1 and num >= (count + 1) / 2:
                            result.append(range(num - (count - 1) / 2, num + (count - 1) / 2 + 1))
            else:
                # 不能进行因数分解直接gg
                pass
        # 还是得排个序，因为奇数个数字相加的序列长度是偶数个数字相加长度的一半，比如5*20与4*25
        result.sort(cmp=lambda x, y: cmp(x[0], y[0]))
        return result


def main():
    print(Solution().FindContinuousSequence(1))
    print(Solution().FindContinuousSequence(3))
    print(Solution().FindContinuousSequence(9))
    print(Solution().FindContinuousSequence(15))
    print(Solution().FindContinuousSequence(99))
    print(Solution().FindContinuousSequence(100))
    print(Solution().FindContinuousSequence(108))
    pass


if __name__ == '__main__':
    main()
