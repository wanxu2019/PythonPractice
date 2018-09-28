# -*- coding: utf-8 -*-
#  @Time        :    2018/9/20 20:53
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test3.py
#  @Place       :    dormitory
'''
<div class="js-left-part coding-side-bar" style="overflow: hidden; padding: 0px; height: 428px; width: 672px;"><div class="js-left-top" style="overflow-y: auto; padding: 0px 10px; height: 339px;"><div class="subject-title test-title">[编程|15分] 单词查找</div><div class="question-intr">时间限制：C/C++ 1秒，其他语言 2秒<br>空间限制：C/C++ 32768K，其他语言 65536K<br>64bit IO Format: %lld</div><div class="nk-warning">本题可使用本地IDE编码，不做跳出限制，编码后请点击“保存并调试”按钮进行代码提交。</div><div class="module-box subject-box"><div class="module-head clearfix"><h1>题目描述</h1></div><div class="subject-main"><div class="subject-content js-question-main"><div class="subject-question"><div>  <span>   <div>   给定一个(M * N)二维的字母词典和一组单词列表（长度K），<strong>M为列数，N为行数</strong>，从词典里找出所有的单词。  </div>  <div>   单词要遵循的规则是所有的字母要在词典中是相邻的，可以上下相邻也可以左右相邻，词典中每个字母单元只能使用一次。  </div> </span>  </div> <div> </div></div><div><h2 style="font-size:14px;font-weight:bold;">输入描述:</h2><pre>第一行三个整数分别代表 M N K<br>第二行 K个单词<br>第三行到第N+3行为词典</pre><h2 style="font-size:14px;font-weight:bold;">输出描述:</h2><pre>找到的单词，每行一个</pre></div><div class="question-oi"><div class="question-oi-hd" style="font-size:14px;font-weight:bold;">示例1<span class="question-oi-tips">输入输出示例仅供调试，后台判题数据一般不包含示例</span></div><div class="question-oi-bd"><div class="question-oi-mod"><h2>输入</h2><a class="code-copy-btn js-sample-clipboard" data-type="input" data-index="0" href="javascript:void(0);">复制</a></div><div class="question-oi-cont"><pre>5&nbsp;5&nbsp;3
hello&nbsp;help&nbsp;high
p&nbsp;a&nbsp;b&nbsp;h&nbsp;m
f&nbsp;h&nbsp;e&nbsp;c&nbsp;p
o&nbsp;i&nbsp;l&nbsp;l&nbsp;h
b&nbsp;g&nbsp;h&nbsp;o&nbsp;n
h&nbsp;x&nbsp;c&nbsp;m&nbsp;l
</pre></div><div class="question-oi-mod"><h2>输出</h2><a class="code-copy-btn js-sample-clipboard" data-type="output" data-index="0" href="javascript:void(0);">复制</a></div><div class="question-oi-cont"><pre>hello
high
</pre></div></div></div></div></div></div></div><div class="js-left-bottom clearfix" style="height: auto;"><div class="answer-sheet-box open js-pager"><a href="javascript:void(0)" class="card-unfold">收起答题卡 <i class="icon-angle-down"></i></a><a href="javascript:void(0)" class="card-fold">展开答题卡 <i class="icon-angle-up"></i></a><ul class="answer-sheet-num clearfix"><li data-type="example" data-index="0"><a href="javascript:void(0);" class="answer-done">例1</a></li><li data-type="example" data-index="1"><a href="javascript:void(0);" class="answer-done">例2</a></li><li data-type="question" data-index="0"><a href="javascript:void(0);" class="answer-done">1</a></li><li data-type="question" data-index="1"><a href="javascript:void(0);" class="answer-done">2</a></li><li data-type="question" data-index="2"><a href="javascript:void(0);" class="answering-num">3</a></li><li data-type="question" data-index="3"><a href="javascript:void(0);" class="">4</a></li><li data-type="question" data-index="4"><a href="javascript:void(0);" class="">5</a></li></ul></div></div></div>

思路：DFS
'''


def main():
    M, N, K = map(int, raw_input().split())
    words = raw_input().split()
    chars = []
    for i in range(N):
        chars.append(raw_input().split())
    result = []

    # def del_col(arr, col_index):
    #     for i in len(arr):
    #         arr[i] = arr[i][:col_index] + arr[i][col_index + 1:]
    #
    # # 行扫描
    # for i in range(len(chars)):
    #     break_1 = False
    #     for j in range(len(chars[i])):
    #         break_2 = False
    #         for k in range(j + 1, len(chars[i]) + 1):
    #             word = "".join(chars[i][j:k])
    #             if word in words:
    #                 result.append(word)
    #                 break_2 = True
    #                 break
    #         if break_2:
    #             break
    #     if break_1:
    #         break
    # # 列扫描
    # for j in range(len(chars[0])):
    #     break_1 = False
    #     for i in range(len(chars)):
    #         break_2 = False
    #         for k in range(i + 1, len(chars) + 1):
    #             word = ""
    #             for index in range(i, k):
    #                 word += chars[index][j]
    #             if word in words:
    #                 result.append(word)
    #                 break_2 = True
    #                 break
    #         if break_2:
    #             break
    #     if break_1:
    #         break
    # for x in result:
    #     print x

    def dfs(chars, visited, i, j, target_s):
        if not 0 <= i < len(chars) or not 0 <= j < len(chars[i]):
            return False
        if target_s[0] != chars[i][j]:
            return False
        visited_copy = [[visited[i][j] for jj in range(len(visited[i]))] for ij in range(len(visited))]
        visited_copy[i][j] = True
        # 不复制
        # visited_copy=visited
        # visited_copy[i][j] = True
        if len(target_s) == 1:
            return chars[i][j] == target_s
        else:
            return dfs(chars, visited_copy, i - 1, j, target_s[1:]) \
                   or dfs(chars, visited_copy, i + 1, j, target_s[1:]) \
                   or dfs(chars, visited_copy, i, j - 1, target_s[1:]) \
                   or dfs(chars, visited_copy, i, j + 1, target_s[1:])

    visited = [[False for j in chars[0]] for i in range(len(chars))]
    for i in range(len(chars)):
        for j in range(len(chars[0])):
            for word in words:
                if dfs(chars, visited, i, j, word):
                    result.append(word)

    for x in result:
        print x


if __name__ == '__main__':
    main()
