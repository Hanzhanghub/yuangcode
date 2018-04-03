# coding:utf-8


'''
date: 2018/4/1
content:
给定一个只含非负整数的m*n网格，找到一条从左上角到右下角的可以使数字和最小的路径。

注意事项
你在同一时间只能向下或者向右移动一步
'''

class Solution(object):
    def minimum_path_sum(self, grid):

        if not grid:
            return

        f = [[None] * len(row) for row in grid]
        f[0][0] = grid[0][0]

        for i in range(1, len(grid[0])):
            f[0][i] = grid[0][i] + f[0][i-1]

        for j in range(1, len(grid)):
            f[j][0] = grid[j][0] + f[j-1][0]

        for row in range(1, len(grid)):
            for line in range(1, len(grid[row])):
                f[row][line] = min(f[row - 1][line], f[row][line-1]) + grid[row][line]

        return f[-1][-1]
