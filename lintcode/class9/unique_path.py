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
class Solution:
    """
    @param: m: positive integer (1 <= m <= 100)
    @param: n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):

        # define a variable to store the path
        f_path = [[0] * n for _ in range(m)]

        f_path[0][0] = 0

        # first row
        for column in range(1, n):
            f_path[0][column] = 1

        # first column
        for row in range(1, m):
            f_path[row][0] = 1

        # general circumstance
        for row in range(1, m):
            for colum in range(1, n):
                f_path[row][colum] = f_path[row-1][colum] + f_path[row][colum-1]


        return f_path[m-1][n-1]


if __name__ == '__main__':
    m, n = 4, 5
    s = Solution()
    ret = s.uniquePaths(m, n)
    print(ret)

'''
1. 思路为：自顶向下。新建一个f_path的二维数组，里头存的是到这个mXn矩阵的每个点的路径个数
2. 注意处理特殊情况：对于第一行和第一列的点，其路径方向是固定的（只能往右/只能往下），所有这两组点的值均为1.
3. 对于非第一行及第一列的点，到这个点的路径的个数即为从上方或左方来的点的值之和。
'''





















