# coding:utf-8

'''
date: 2017/12/5
content:
给定一个只含非负整数的m*n网格，找到一条从左上角到右下角的可以使数字和最小的路径。

注意事项
你在同一时间只能向下或者向右移动一步
'''
class Solution:
    """
    @param: grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):

        f_sum = [[None] * row for row in grid]  # m X n
        m = len(grid)
        n = len(grid[0])

        # start point
        f_sum[0][0] = grid[0][0]

        #  special tackle: when it is the fist column
        for row in range(1, m):
            f_sum[row][0] = grid[row][0] + f_sum[row-1][0]

        # special tackle: when it is the first row
        for column in range(1, n):
            f_sum[0][column] = grid[0][column] + f_sum[0][column-1]

        # Multiple Loop: Top to Bottom
        for row in range(1, m):
            for colum in range(1, n):
                f_sum[row][colum] = grid[row][colum] + min(f_sum[row-1][colum], f_sum[row][colum-1])

        return f_sum[m-1][n-1]

'''
1。还是利用了triangle中的思路，自顶向下，新建了一个f_sum的二维数组来存储到每个点的最小路径和
2. 在进行自顶向下前，注意先处理特殊情况：即第一行和第一列的值
'''















