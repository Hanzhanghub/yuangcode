# coding:utf-8

'''
date: 2017/11/7
content:
Given an integer array, find a subarray where the sum of numbers is zero. 
Your code should return the index of the first number and the index of the last number.

Notice
There is at least one subarray that it's sum equals to zero.

Example
Given [-3, 1, 2, -3, 4], return [0, 2] or [1, 3].
'''
class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # special condition
        if not nums:
            return nums

        # step 1: prefixSum
        prefixSum = [nums[0]]
        for i in range(1,len(nums)):
            round_sum = nums[i] + prefixSum[i-1]
            prefixSum.append(round_sum)

        # step 2: construct a dict for storing the index of the same value in  prefixSum
        # note that: we just need to find a pair! only a pair is enough
        indx_dict = {0:-1}
        ret = []
        for j in range(len(prefixSum)):
            if prefixSum[j] in indx_dict:
                ret.append(indx_dict[prefixSum[j]]+1)
                ret.append(j)
                break
            else:
                indx_dict[prefixSum[j]] = j
        return ret

if __name__ == '__main__':
    a = [-3, 1, 2, -3, 4]
    s = Solution()
    ret = s.subarraySum(a)
    print(ret)


'''
1. 首先使用prefixSum统计前缀数组的和
2. 要明确一点，在prefixSum中相同的两个值之间的数的和就是0。
   所以使用字典来存prefixSum中的每个值，由于这道题只需要找到一组结果即可，
   所以，字典中的键为prefixSum中的值，字典的值为其下标
3. 在构建字典的过程中，需要注意一点，字典的初始化应该为{0:-1},因为prefixSum的初始和为0
'''