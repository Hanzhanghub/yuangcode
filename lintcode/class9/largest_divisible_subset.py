# coding:utf-8

'''
date: 2017/12/7
content: 
Given a set of distinct positive integers, 
find the largest subset such that every pair (Si, Sj)  of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

Notice
If there are multiple solutions, return any subset is fine.

Example
Given nums = [1,2,3], return [1,2] or [1,3]
Given nums = [1,2,4,8], return [1,2,4,8]
'''
class Solution:
    """
    @param: nums: a set of distinct positive integers
    @return: the largest subset 
    """
    def largestDivisibleSubset(self, nums):
        # special conditions
        if not nums:
            return []

        # sort
        nums.sort()

        # new a path
        n = len(nums)
        # state
        f = [[nums[i]] for i in range(n)]
        largest_length = 0
        largest_path = []

        # function
        for i in range(1, n):
            divider = nums[i]
            for j in range(i):
                if divider % f[j][-1] == 0:
                    tmp = list(f[j])
                    tmp.append(divider)
                    if len(tmp) > len(f[i]):
                        f[i] = tmp
                    if len(tmp) > largest_length:
                        largest_length = len(tmp)
                        largest_path = tmp
        return largest_path

if __name__ == '__main__':
    a = [1,2, 3,4,6,12,24,8]
    s = Solution()
    ret = s.largestDivisibleSubset(a)
    print(ret)

















