# -*- coding: utf-8 -*-
#  @Time        :    2018/9/19 21:50
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test2.py
#  @Place       :    dormitory
'''
题目描述：
小P和小Q在工作之余玩起了无禁手五子棋。无禁手五子棋的规则非常简单，两个人分别执黑棋和白棋，在一个15x15的格子棋盘上交替行棋（黑棋先行）。当一方行棋之后，棋形在横向、纵向或者斜向出现了连续的5枚以上的棋子时，游戏立刻结束，行棋方获胜。如果棋盘上被填满，仍然没有出现一方赢棋，则双方和棋。 你从不靠谱的渠道看到了小P和小Q的进行中或者结束了的棋局。你想知道棋局是谁赢了，或者还在进行中，于是你决定写个程序来判断。注意由于拿到棋局的渠道并不靠谱，所以棋局可能是被恶意篡改成为一个不可能出现的局面。你需要判断出这种局面。

输入
15行每行15个字符表示棋盘上的局面。

'.'表示棋盘格子中没有被棋子占据。

'B'表示棋盘格子被白棋占据。

'W'表示棋盘格子被黑棋占据。
输出
一行一个字符串（不含引号），表示棋局的局面：

"black win"，表示黑棋获胜；

"white win"，表示白棋获胜；

"draw"，表示和棋；

"invalid board"，表示给定的输入数据是不可能出现的局面；

"not finished"，表示棋局仍在进行中；
'''


def main():
    table = []
    for i in range(15):
        table.append(list(raw_input()))

    def get_count(i, j):
        ch = table[i][j]
        count1 = 1
        i1, j1 = i, j
        while True:
            i1, j1 = i1 - 1, j1
            if 0 <= i1 < 15 and 0 <= j1 < 15 and table[i1][j1] == ch:
                count1 += 1
            else:
                break
        i1, j1 = i, j
        while True:
            i1, j1 = i1 + 1, j1
            if 0 <= i1 < 15 and 0 <= j1 < 15 and table[i1][j1] == ch:
                count1 += 1
            else:
                break
        count2 = 1
        i2, j2 = i, j
        while True:
            i2, j2 = i2, j2 - 1
            if 0 <= i2 < 15 and 0 <= j2 < 15 and table[i2][j2] == ch:
                count2 += 1
            else:
                break
        i2, j2 = i, j
        while True:
            i2, j2 = i2, j2 + 1
            if 0 <= i2 < 15 and 0 <= j2 < 15 and table[i2][j2] == ch:
                count2 += 1
            else:
                break

        count3 = 1
        i3, j3 = i, j
        while True:
            i3, j3 = i3 - 1, j3 - 1
            if 0 <= i3 < 15 and 0 <= j3 < 15 and table[i3][j3] == ch:
                count3 += 1
            else:
                break
        i3, j3 = i, j
        while True:
            i3, j3 = i3 + 1, j3 + 1
            if 0 <= i3 < 15 and 0 <= j3 < 15 and table[i3][j3] == ch:
                count3 += 1
            else:
                break

        count4 = 1
        i4, j4 = i, j
        while True:
            i4, j4 = i4 - 1, j4 - 1
            if 0 <= i4 < 15 and 0 <= j4 < 15 and table[i4][j4] == ch:
                count4 += 1
            else:
                break
        i4, j4 = i, j
        while True:
            i4, j4 = i4 + 1, j4 + 1
            if 0 <= i4 < 15 and 0 <= j4 < 15 and table[i4][j4] == ch:
                count4 += 1
            else:
                break
        return max(count1, count2, count3, count4)
    wCount=0
    bCount=0
    draw=True
    for i in range(len(table)):
        for j in range(len(table[0])):
            ch=table[i][j]
            if ch=='W':
                wCount=max(get_count(i,j),wCount)
            elif ch=='B':
                bCount=max(get_count(i,j),bCount)
            else:
                not_draw=False
    if bCount==5 and wCount<5:
        print "black win"
    elif bCount<5 and wCount==5:
        print "white win"
    elif bCount<5 and wCount<5:
        print "not finished"
    elif draw:
        print "draw"
    else:
        print "invalid board"


if __name__ == '__main__':
    main()
