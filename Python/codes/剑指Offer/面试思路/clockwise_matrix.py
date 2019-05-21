# -*- coding:utf-8 -*-

"""
题目描述:输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如:
如果输入如下4 X 4矩阵：
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
"""


class Solution:
    def printMatrix(self, matrix):
        # Create a list for result
        res = []
        # Loop to get a layer while matrix not None
        while matrix:
            # Get the first line of layer
            res += matrix.pop(0)
            # Get the right line of layer
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            # Get the bottom line of layer
            if matrix:
                res += matrix.pop()[::-1]
            # Get the left line of layer
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res


class Solution2:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        # create result list
        res = []
        # Get the rows number of matrix
        rows = len(matrix)
        # Get the coloums number of matirx
        cols = len(matrix[0])
        # If the matrix only have one element,return this element
        if rows == 1 and cols == 1:
            res = [matrix[0][0]]
            return res
        # Get the required layer number of matrix
        for o in range((min(rows, cols) + 1) // 2):
            # Get the top line of current layer
            [res.append(matrix[o][t]) for t in range(o, cols - o)]
            # Get the right line of current layer
            [res.append(matrix[r][cols - 1 - o]) for r in range(o, rows - o) if matrix[r][cols - 1 - o] not in res]
            # Get the bottom line of current layer
            [res.append(matrix[rows - 1 - o][b]) for b in range(cols - 1 - o, o - 1, -1) if
             matrix[rows - 1 - o][b] not in res]
            # Get the left line of current layer
            [res.append(matrix[l][o]) for l in range(rows - 1 - o, o - 1, -1) if matrix[l][o] not in res]
        return res


# -*- coding:utf-8 -*-
class Solution3:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        rst = []
        rows = len(matrix)
        cols = len(matrix[0])
        if rows == 1 and cols == 1:
            rst.append(matrix[0][0])
            return rst
        for x in range((min(rows, cols) + 1) // 2):
            [rst.append(matrix[x][t]) for t in range(x, cols - x)]
            [rst.append(matrix[r][cols - 1 - x]) for r in range(x + 1, rows - x)
             if matrix[r][cols - 1 - x] not in rst]
            [rst.append(matrix[rows - 1 - x][b]) for b in range(cols - x - 2, x - 1, -1)
             if matrix[rows - 1 - x][b] not in rst]
            [rst.append(matrix[l][x]) for l in range(rows - 1 - x, x, -1) if matrix[l][x] not in rst]
        return rst


if __name__ == '__main__':
    s = Solution3()
    matrix = [[], [], [], []]
    row = 0
    for x in range(1, 17):
        matrix[row].append(x)
        if x % 4 == 0:
            row += 1
    print(matrix)
    res = s.printMatrix(matrix)
    print(res)
