# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 14:47
# @Author  : Json Wan
# @Description : 
# @File    : hasPath.py
'''
题目描述
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
思路：
分解为子问题解决，递归操作还是很容易想到的，高效解法得上动规了。

'''


class Solution:
    def copy(self, matrix):
        result = []
        for i in range(len(matrix)):
            sub_result = []
            for j in range(len(matrix[i])):
                sub_result.append(matrix[i][j])
            result.append(sub_result)
        return result

    def hasPathStartFrom(self, matrix, i, j, path):
        rows = len(matrix)
        cols = len(matrix[0])
        if not 0 <= i < rows or not 0 <= j < cols:
            return False
        if matrix[i][j] != path[0]:
            return False
        if len(path) == 1:
            if matrix[i][j] == path[0]:
                return True
            else:
                return False
        if matrix[i][j] == path[0]:
            matrix_copy_1 = self.copy(matrix)
            matrix_copy_1[i][j] = None
            if self.hasPathStartFrom(matrix_copy_1, i - 1, j, path[1:]):
                return True
            matrix_copy_1 = self.copy(matrix)
            matrix_copy_1[i][j] = None
            if self.hasPathStartFrom(matrix_copy_1, i + 1, j, path[1:]):
                return True
            matrix_copy_1 = self.copy(matrix)
            matrix_copy_1[i][j] = None
            if self.hasPathStartFrom(matrix_copy_1, i, j - 1, path[1:]):
                return True
            matrix_copy_1 = self.copy(matrix)
            matrix_copy_1[i][j] = None
            if self.hasPathStartFrom(matrix_copy_1, i, j + 1, path[1:]):
                return True
        return False

    def hasPath(self, matrix, rows, cols, path):
        # write code here
        # 构造二维矩阵
        real_matrix = []
        for i in range(rows):
            real_matrix.append(matrix[i * cols:(i + 1) * cols])
        for i in range(rows):
            for j in range(cols):
                if self.hasPathStartFrom(real_matrix, i, j, path):
                    return True
        return False


def main():
    print(Solution().hasPath(list("abcesfcsadee"), 3, 4, "asade"))
    print(Solution().hasPath(list("abcesfcsadee"), 3, 4, "asadef"))
    print(Solution().hasPath(list("abcesfcsadee"), 3, 4, "bcced"))
    print(Solution().hasPath(list("abcesfcsadee"), 3, 4, "abcb"))
    pass


if __name__ == '__main__':
    main()
