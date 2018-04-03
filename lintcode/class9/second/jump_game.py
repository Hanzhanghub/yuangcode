# coding:utf-8

'''
date: 2017/12/6
content:
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Notice
This problem have two method which is Greedy and Dynamic Programming.

The time complexity of Greedy method is O(n).
The time complexity of Dynamic Programming method is O(n^2).

We manually set the small data set to allow you pass the test in both ways. 
This is just to let you learn how to use this problem in dynamic programming ways. 
If you finish it in dynamic programming ways, you can try greedy method to make it accept again.

Example
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
'''

class Solution(object):
    def jump_game(self, A):

        if not A:
            return False

        return self.dfs_helper(0, A)

    def dfs_helper(self, indx, nums):
        if indx >= len(nums) -1:
            return True

        for i in range(nums[indx], -1, -1):
            next_indx = indx + i

            if next_indx == indx and indx < len(nums) -1:
                return False

            ret = self.dfs_helper(next_indx, nums)
            if ret:
                return True
        return False
