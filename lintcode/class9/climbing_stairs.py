# coding:utf-8

'''
date:2017/12/6
content:
假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？

样例
比如n=3，1+1+1=1+2=2+1=3，共有3种不同的方法
'''
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # special condition
        if n == 0:
            return 0

        if n == 1:
            return 1

        # new a f_path, each point in the list, represents the ith step in the n steps.
        # and f_path[step] is the means of how to get to this step
        f_path = [0] * (n + 1)

        # sprcial concern: the first step and the second step
        f_path[1], f_path[2] = 1, 2

        # for the rest of the steps, the value of which obeys the rule of [i-1] + [i-2]
        for step in range(3, n+1):
            f_path[step] = f_path[step - 1] + f_path[step - 2]

        return f_path[n]

if __name__ == '__main__':
    n = 1
    s = Solution()
    ret = s.climbStairs(n)
    print(ret)


'''
1. 思路：对于第一格，有一种方法到达；
         对于第二格，有两种方法到达；
         对于大于第二格后的格i，到达其的方法均为：[i-1] + [i-2]
'''