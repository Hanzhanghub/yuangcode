# coding:utf-8

'''
date: 2017/12/5
content: 
有一个机器人的位于一个 m × n 个网格左上角。
机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角。
问有多少条不同的路径？

注意事项
n和m均不超过100

样例
给出 m = 3 和 n = 3, 返回 6.
给出 m = 4 和 n = 5, 返回 35.
'''


class Solution(object):
    def unique_path(self, m, n):

        f = [[None] * n for _ in m]

        for i in range(n):
            f[0][i] = 1

        for j in range(m):
            f[j][0] = 1

        for row in range(1, m):
            for line in range(1, n):
                f[row][line] = f[row-1][line] + f[row][line-1]

        return f[m-1][n-1]
    


