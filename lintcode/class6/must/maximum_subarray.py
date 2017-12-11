# coding:utf-8

'''
date: 11/6
content: 
Given an array of integers, find a contiguous subarray which has the largest sum.
Notice
The subarray should contain at least one number.

Example
Given the array [−2,2,−3,4,−1,2,1,−5,3], the contiguous subarray [4,−1,2,1] has the largest sum = 6
'''


class Solution:
    """
    @param: nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # special
        if len(nums) <= 1:
            return nums[0]

        # step 1: construct a prefix sum collections
        prefixSum = [nums[0]]
        max_subsum = - float('inf')
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[i - 1] + nums[i])

        # step 2: find the maxmum value



        # solution 1
        # return max(prefixSum) - min(prefixSum)


if __name__ == '__main__':
    a = [-2, 2,-3, 4,-1, 2, 1,-5, 3]
    s = Solution()
    ret = s.maxSubArray(a)
    print(ret)

