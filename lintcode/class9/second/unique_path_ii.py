# coding:utf-8

'''
date: 2017/12/5
content:
"不同的路径" 的跟进问题：
现在考虑网格中有障碍物，那样将会有多少条不同的路径？
网格中的障碍和空位置分别用 1 和 0 来表示。

注意事项
m 和 n 均不超过100

样例
如下所示在3x3的网格中有一个障碍物：
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
一共有2条不同的路径从左上角到右下角。
'''

class Solution(object):
    def unique_path_ii(self, obstacleGrid):
        if not obstacleGrid:
            return

        m, n = len(obstacleGrid), len(obstacleGrid[0])

        f = [[None] * n for _ in range(m)]
        f[0][0] = 1 if obstacleGrid[0][0] != 1 else 0

        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                f[0][i] = f[0][i-1]
            else:
                f[0][i] = 0

        for j in range(1, m):
            if obstacleGrid[j][0] != 1:
                f[j][0] = f[j-1][0]
            else:
                f[j][0] = 0

        for row in range(1, m):
            for line in range(1, n):
                if obstacleGrid[row][line] != 1:
                    f[row][line] = f[row][line-1] + f[row-1][line]
                else:
                    f[row][line] = 0

        return f[m-1][n-1]
