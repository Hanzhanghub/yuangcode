# coding:utf-8

'''
date: 12/1
content:

在一个排序矩阵中找从小到大的第 k 个整数。
排序矩阵的定义为：每一行递增，每一列也递增。

样例
给出 k = 4 和一个排序矩阵：
[
  [1 ,5 ,7],
  [3 ,7 ,8],
  [4 ,8 ,9],
]
返回 5。
'''

import heapq

class Solution:
    """
    @param: matrix: a matrix of integers
    @param: k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):

        # special condition
        if not matrix:
            return

        # 1. a heap to store all the number
        tmp_heap = []
        for row in matrix:
            for number in row:
                heapq.heappush(tmp_heap, number)

        # 2. pop minimum number in the heap
        while k > 1:
            heapq.heappop(tmp_heap)

        # return the kth number
        return heapq.heappop(tmp_heap)

'''
regular move!
'''









