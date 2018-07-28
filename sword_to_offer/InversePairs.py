# -*- coding: utf-8 -*-
#  @Time        :    2018/7/22 1:20
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    InversePairs.py
#  @Place       :    dormitory
"""
题目描述
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
输入描述:
题目保证输入的数组中没有的相同的数字
数据范围：
对于%50的数据,size<=10^4
对于%75的数据,size<=10^5
对于%100的数据,size<=2*10^5
思路：求出所有，数组无规则，只能考虑遍历了，后期看看其他大佬解法。
遍历根本过不了，只能另求它法。。。。
思路2：递归思想，将一个数组分为两部分，左部与右部，则整个数组逆序对的数量为左部内部逆序对数量+右部内部逆序对数量+左部与右部共同构成的逆序对数量，而左右共同构成的逆序对数量与左右部内部数据顺序无关，因此可先排序，再用乘法计算以取代遍历，得到更小的时间复杂度；
在归并排序的时候就统计逆序对数量，而不是排完了再来遍历；
整体思路还是大问题的分解，有递归思想，同时考虑归并思想在逆序对的应用；
思路3：思路2想法是正确的，但是时间依旧不达标，在写程序时应考虑通过下标的游走代替切片操作，尽量少生成新的list，少分配内存，这样能节省大量时间。
"""


class Solution:
    def __init__(self):
        self.count = 0

    def InversePairs1(self, data):
        # write code here
        count = 0
        for i in range(len(data) - 1):
            for j in range(i + 1, len(data)):
                if data[i] > data[j]:
                    count += 1
        return count

    def InversePairs2(self, data):
        length = len(data)
        if length <= 1:
            return 0
        left_arr = data[:length / 2]
        right_arr = data[length / 2:]
        left_num = self.InversePairs2(left_arr)
        right_num = self.InversePairs2(right_arr)
        sorted_left_arr = sorted(left_arr)
        sorted_right_arr = sorted(right_arr)
        left_length = len(sorted_left_arr)
        right_length = len(sorted_right_arr)
        count = 0
        j = 0
        while j < right_length:
            i = 0
            while i < left_length:
                if sorted_left_arr[i] > sorted_right_arr[j]:
                    count += left_length - i
                    break
                i += 1
            j += 1
        return (count + left_num + right_num) % 1000000007

    def merge_sort(self, data):
        length = len(data)
        if length <= 1:
            return data
        # 注意：这两句是非常消耗时间的，应当充分利用已经分配的空间
        left_arr = data[:length / 2]
        right_arr = data[length / 2:]
        sorted_left_arr = self.merge_sort(left_arr)
        sorted_right_arr = self.merge_sort(right_arr)
        # 归并过程
        arr = []
        while len(sorted_left_arr) and len(sorted_right_arr) > 0:
            if sorted_left_arr[0] > sorted_right_arr[0]:
                self.count += len(sorted_left_arr)
                arr.append(sorted_right_arr[0])
                sorted_right_arr.remove(sorted_right_arr[0])
            else:
                arr.append(sorted_left_arr[0])
                sorted_left_arr.remove(sorted_left_arr[0])
        arr += sorted_left_arr + sorted_right_arr
        return arr

    def InversePairs(self, data):
        self.merge_sort(data)
        return self.count % 1000000007


# 通过的解法
class Solution2:
    def InversePairs(self, data):
        if not data:
            return 0
        Copy = [i for i in data]
        count = self.InversePairsCore(data, Copy, 0, len(data) - 1)
        del Copy
        return count % 1000000007

    def InversePairsCore(self, data, Copy, start, end):
        if start == end:
            Copy[start] = data[start]
            return 0
        mid = int((start + end) / 2)
        left = self.InversePairsCore(Copy, data, start, mid)
        right = self.InversePairsCore(Copy, data, mid + 1, end)
        # 下面相当于merge
        # i初始化为前半段最后一个数字的下标，j初始化为后半段最后一个数字的下标
        i, j = mid, end
        indexCopy = end
        count = 0
        while i >= start and j >= mid + 1:
            if data[i] > data[j]:
                Copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
                count += j - mid
            else:
                Copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1
        # 进行到这里，说明知道有一个数组已经到头了，或者是i或者是j
        # 如果前半段还有剩余的话，要全部复制到copy数组里面
        while i >= start:
            Copy[indexCopy] = data[i]
            indexCopy -= 1
            i -= 1
        # 如果后半段还有剩余的话，要全部复制到copy数组里面
        while j >= mid + 1:
            Copy[indexCopy] = data[j]
            indexCopy -= 1
            j -= 1
        return left + right + count


def main():
    print(Solution().InversePairs1([1, 2, 3, 4, 0]))
    print(Solution().InversePairs([1, 2, 3, 4, 0]))
    print(Solution().InversePairs1([1, 2, 3, 4, 5, 6, 7, 0]))
    print(Solution().InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))
    from random import randint
    from time import time
    NUM = 100000
    arr = [randint(1, NUM) for i in range(NUM)]
    # print(arr)
    # time_start = time()
    # print(Solution().InversePairs1(arr))
    # print(time() - time_start)
    # time_start = time()
    # print(Solution().InversePairs2(arr))
    # print(time() - time_start)
    time_start = time()
    print(Solution().InversePairs(arr))
    print(time() - time_start)


if __name__ == '__main__':
    main()
