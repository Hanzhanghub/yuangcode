# coding:utf-8

'''
date:2017/12/6
content:
假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？

样例
比如n=3，1+1+1=1+2=2+1=3，共有3种不同的方法
'''

class Solution(object):
    def climbing_stairs(self, n):
        if n == 0:
            return 0

        f = [None] * (n + 1)
        f[2] = 2
        f[1] = 1

        for i in range(3, n+1):
            f[i] = f[i-1] + f[i-2]

        return f[n]
