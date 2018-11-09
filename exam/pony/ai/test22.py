# -*- coding: utf-8 -*-
#  @Time        :    2018/10/29 18:58
#  @Author      :    Json Wan
#  @Description :    
#  @File        :    test22.py
#  @Place       :    dormitory


import sys


def dfs(board, x, y, last_dir, count, cls):
    if count == 5:
        return True
    if not last_dir:
        for each_dir in DIR:
            temp_x = x + each_dir[0]
            temp_y = y + each_dir[1]
            if 0 <= temp_x < N and 0 <= temp_y < N and board[temp_x][temp_y] == cls:
                rvt = dfs(board, temp_x, temp_y, each_dir, count + 1, cls)
                if rvt:
                    return True
    else:
        temp_x = x + last_dir[0]
        temp_y = y + last_dir[1]
        if 0 <= temp_x < N and 0 <= temp_y < N and board[temp_x][temp_y] == cls:
            rvt = dfs(board, temp_x, temp_y, last_dir, count + 1, cls)
            if rvt:
                return True
    return False


if __name__ == '__main__':
    N = 15
    DIR = [[1, 0], [0, 1], [-1, 1], [1, 1]]

    chess_board = []
    for i in range(N):
        temp = sys.stdin.readline().strip()
        chess_board.append(temp)

    count_white, count_black = 0, 0
    for i in range(N):
        count_white += chess_board[i].count('W')
        count_black += chess_board[i].count('B')

    if count_white > count_black or count_black > count_white + 1:
        print("invalid board")
    else:
        rvt_w, rvt_b = False, False
        for i in range(N):
            if rvt_w:
                break
            for j in range(N):
                if chess_board[i][j] == 'W':
                    rvt_w = dfs(chess_board, i, j, None, 1, 'W')
                    if rvt_w:
                        break
        for i in range(N):
            if rvt_b:
                break
            for j in range(N):
                if chess_board[i][j] == 'B':
                    rvt_b = dfs(chess_board, i, j, None, 1, 'B')
                    if rvt_b:
                        break

        if not rvt_w and not rvt_b:
            if count_white + count_black == N * N:
                print("draw")
            else:
                print("not finished")
        elif rvt_w:
            if count_white == count_white:
                print("white win")
            else:
                print("invalid board")
        elif rvt_b:
            if count_black > count_white:
                print("black win")
            else:
                print("invalid board")
