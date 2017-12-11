# coding:utf-8

'''
date: 2017/12/7
content:
Given a positive integer n, find the least number of perfect square numbers 
(for example, 1, 4, 9, 16, ...) which sum to n.

Example
Given n = 12, return 3 because 12 = 4 + 4 + 4
Given n = 13, return 2 because 13 = 4 + 9
'''

from math import sqrt


class Solution:
    """
    @param: n: a positive integer
    @return: An integer
    """

    def numSquares(self, n):
        # special condition
        if n == 0 or n == 1:
            return n

        # step 1: find the upper bound
        upper = int(sqrt(n))
        f = [0] * (n + 1)
        a = [1] * upper
        for i in range(upper):
            a[i] = (i + 1) ** 2

        # step 2: multiple loop
        for i in range(1, n+1):
            # if pick a[j]
            tmp = []
            for j in range(upper):
                if i >= a[j]:
                    tmp.append(f[i-a[j]] + 1)
            f[i] = min(tmp)
        return f[-1]


if __name__ == '__main__':
    n = 16
    s = Solution()
    ret = s.numSquares(n)
    print(ret)


'''
1. 思路：将他转变为一个相似的问题来求解：有n+1个格子，从第1个格子出发，每次可以跳[1,4,9,16...]步，问到达最后一个
格子的最短的跳数为多少
2. 对应于标准流程：
    （1）state：f[i]表示走到第i个格子时所需最少的跳数
    （2）function：f[i] = min{f[j] + 1}，其中j = i - 1/4/9/16/....
    （3）initial：f = [0] * (n+1)
    （4）answer：f[-1]
3. 一开始我们需要建立可以跳的步数A，方法很简单就是对sqrt(n)取整，就能知道最多能跳多少的平方个步。
'''