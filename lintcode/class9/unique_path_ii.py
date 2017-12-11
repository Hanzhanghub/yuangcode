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


class Solution:
    """
    @param: obstacleGrid: A list of lists of integers
    @return: An integer
    """

    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 0

        if obstacleGrid[0][0] == 1 :
            return 0

        # New a variable to store the path number
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        f_path = [[0] * n for _ in range(m)]


        f_path[0][0] = 1
        # special concern: first row
        for column in range(1, n):
            if obstacleGrid[0][column] == 1:
                f_path[0][column] = 0
            else:
                f_path[0][column] = f_path[0][column - 1]

        # special concern: first column
        for row in range(1, m):
            if obstacleGrid[row][0] == 1:
                f_path[row][0] = 0
            else:
                f_path[row][0] = f_path[row - 1][0]

        # In general
        for row in range(1, m):
            for colum in range(1, n):
                if obstacleGrid[row][colum] == 1:
                    f_path[row][colum] = 0
                    continue

                f_path[row][colum] = f_path[row][colum - 1] + f_path[row - 1][colum]

        return f_path[m - 1][n - 1]



        # special concern: first column


if __name__ == '__main__':
    a = []
    s = Solution()
    ret = s.uniquePathsWithObstacles(a)


'''
1. 在unique_path的基础上，我们就需要在设置每个点的路径值时多加一个考虑，即如果在这个点的位置上，obstacleGrid的值
为1， 那么f_path相对应的位置就设置成0， 表示没有路径能够到达这个点
'''