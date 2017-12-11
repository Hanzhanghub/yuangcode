# coding:utf-8

'''
date: 2017/12/2
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


class Solution:
    """
    @param: triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        '''
        To solve this problem in 5 solutions
        :triangle:  
        :return: 
        '''

        '''Solution 1: DFS: Traverse'''
        # self.min_sum = float('inf')
        # self.tri = triangle
        #
        # # Traverse DFS
        # self.traverse_helper(0, 0, 0)
        #
        # return self.min_sum

        '''Solution 2:DFS: divide conquer'''
        # self.tri = triangle
        #
        # # Divide Conquer for DFS
        # result = self.divide_conquer_helper(0, 0)
        #
        # return result


        '''Solution 3: DFS: devide conquer + memorization --- Actually a kind of realization of dynamic programming'''
        #     self.tri = triangle
        #     self.hash = [[None] * len(row) for row in triangle]
        #
        #     # divide conquer
        #     result = self.divide_conquer_and_memorization_helper(0, 0)
        #     return result

        '''Solution 4: Multiple loop: Bottom to Top'''
        # f = [[None] * len(row) for row in triangle]
        # n = len(triangle)
        #
        # # put the value in last row of the triangle into f
        # for i in range(len(triangle[-1])):
        #     f[n-1][i] = triangle[n-1][i]
        # # print(f)
        #
        # # From bottom to top, add the sum of min(left, right) from next layer
        # for row in range(len(triangle) - 2, -1, -1):
        #     for line in range(len(triangle[row])):
        #         f[row][line] = triangle[row][line] + min(f[row+1][line], f[row+1][line+1])
        # return f[0][0]


        '''Solution 5: Multiple loop: Top to Bottom'''
        f = [[None] * len(row) for row in triangle]
        f[0][0] = triangle[0][0]
        n = len(triangle)
        minimum = float('inf')

        # From top to bottom
        for row in range(1, len(triangle)):
            for line in range(len(triangle[row])):
                # if column == 0
                if line == 0:
                    f[row][line] = f[row - 1][line] + triangle[row][line]
                    continue

                # if column == len(triangle[row]) - 1
                if line == len(triangle[row]) - 1:
                    f[row][line] = f[row - 1][line - 1] + triangle[row][line]
                    continue

                # else
                f[row][line] = triangle[row][line] + min(f[row - 1][line], f[row - 1][line - 1])

                # when come to the last layer, we compare this f[row][line] to the minimum
                if row == n - 1:
                    if f[row][line] < minimum:
                        minimum = f[row][line]

        return minimum


    #
    # def divide_conquer_and_memorization_helper(self, x, y):
    #
    #     # When it comes to the last layer
    #     if x == len(self.tri):
    #         return 0
    #
    #     # construct a hash
    #     if self.hash[x][y] is not None:
    #         return self.hash[x][y]
    #
    #     self.hash[x][y] = self.tri[x][y] + min(self.divide_conquer_and_memorization_helper(x + 1, y),
    #                                            self.divide_conquer_and_memorization_helper(x + 1, y + 1))
    #     return self.hash[x][y]
    #
    #
    #
    #
    #
    # def divide_conquer_helper(self, x, y):
    #
    #     # When comes to the last layer
    #     if x == len(self.tri):
    #         return 0
    #
    #     return self.tri[x][y] + min(self.divide_conquer_helper(x + 1, y), self.divide_conquer_helper(x + 1, y + 1))
    #
    # def traverse_helper(self, x, y, sum):
    #     # When come to the last layer
    #     if x == len(self.tri):
    #         # compare the sum of this path to the global sum
    #         if sum < self.min_sum:
    #             self.min_sum = sum
    #         return
    #
    #     self.traverse_helper(x + 1, y, sum + self.tri[x][y])
    #     self.traverse_helper(x + 1, y + 1, sum + self.tri[x][y])


if __name__ == '__main__':
    tri = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    s = Solution()
    ret = s.minimumTotal(tri)
    print(ret)
