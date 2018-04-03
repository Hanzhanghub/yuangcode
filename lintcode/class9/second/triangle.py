# coding:utf-8

'''
date: 2018/4/1
content:
给定一个数字三角形，找到从顶部到底部的最小路径和。每一步可以移动到下面一行的相邻数字上。

注意事项
如果你只用额外空间复杂度O(n)的条件下完成可以获得加分，其中n是数字三角形的总行数。

样例
比如，给出下列数字三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
从顶到底部的最小路径和为11 ( 2 + 3 + 5 + 1 = 11)。
'''


class Solution(object):
    def triangle(self, triangle):
        '''solution 1, dfs: traverse'''
        # if not triangle:
        #     return 0
        #
        # self.tri = triangle
        #
        # self.minimum_sum = float('inf')
        #
        # self.dfs_helper(0, 0, 0)
        # return self.minimum_sum

        '''solution 2, dfs: divide conquer'''
        # if not triangle:
        #     return 0
        #
        # self.tri = triangle
        # result = self.divide_conquer(0, 0)
        # return result


        '''solution 3, dfs: divide cxonquer + memory search '''
        # if not triangle:
        #     return 0
        #
        # self.tri = triangle
        # self.hash = [[None] * len(row) for row in triangle]
        #
        # result = self.divide_conquer_with_memory_seearch(0, 0)
        # return result

        '''solution 4:multiloop: bottom up'''
        f = [[None] * len(row) for row in triangle]
        n = len(triangle)

        for i in range(len(triangle[-1])):
            f[n-1][i] = triangle[n-1][i]

        for row in range(n-2, -1, -1):
            for line in range(len(triangle[row])):
                f[row][line] = triangle[row][line] + min(f[row+1][line], f[row+1][line+1])

        return f[0][0]


    def divide_conquer_with_memory_search(self, x, y):
        if x == len(self.tri):
            return 0

        if self.hash[x][y] is not None:
            return self.hash[x][y]

        self.hash[x][y] = self.tri[x][y] + min(self.divide_conquer_with_memory_search(x+1, y),
                                               self.divide_conquer_with_memory_search(x+1, y+1))

        return self.hash[x][y]


    def divide_conquer(self, x, y):
        if x == len(self.tri):
            return 0

        left = self.divide_conquer(x+1, y)
        right = self.divide_conquer(x+1, y+1)

        return min(left, right) + self.tri[x][y]


    def dfs_helper(self, x, y, sum):
        if x == len(self.tri):
            if sum < self.minimum_sum:
                self.minimum_sum = sum

            return

        self.dfs_helper(x+1, y, sum + self.tri[x][y])
        self.dfs_helper(x+1, y+1, sum + self.tri[x][y])


