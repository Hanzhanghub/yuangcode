#coding:utf-8

'''
date:2017/10/18
content:
Given a set of distinct integers, S, return all possible subsets.

Note: Elements in a subset must be in non-descending order. The solution set must not contain duplicate subsets.

For example, If S = [1,2,3], a solution is:
[ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ]
'''
class Solution(object):
    def subsets(self,nums):
        results = []
        n = len(nums)
        nums.sort()

        # 1 << n is 2 ^ n
        #each subset equals to an binary integer between 0..2 ^ n - 1
        # 0 -> 000 -> []
        # 1 -> 001 -> [1]
        # 2 -> 010 -> [2]
        #..
        # 7 -> 111 -> [1, 2, 3]
        for i in range((1<<n)):
            subset = []
            for j in range(n):
                # check whether the jth digit in i's binary representation is 1
                if i & (1<<j):
                    subset.append(nums[j])
            results.append(subset)
        return results

'''
这种非递归方法要注意：
1.结果的个数是可知的，使用多位二进制数代表每种情况
2.这个方法中要学习到如何判断一个二进制数的每一位是1 --- 按位相与 以及 左移位
'''