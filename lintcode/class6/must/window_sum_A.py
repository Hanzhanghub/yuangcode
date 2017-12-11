# coding:utf-8

'''
date: 2017/11/7
content:
Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array,
find the sum of the element inside the window at each moving.

Example 
For array [1,2,7,8,5], moving window size k = 3. 
1 + 2 + 7 = 10 
2 + 7 + 8 = 17 
7 + 8 + 5 = 20 
return [10,17,20]
'''


class Solution(object):
    def windowSum(self, nums, k):
        # special condition
        if not nums or k > len(nums):
            return nums

        # step 1: prefixSum
        prefixSum = [nums[0]]
        for i in range(1, len(nums)):
            round_sum = nums[i] + prefixSum[i - 1]
            prefixSum.append(round_sum)

        # step 2: find the start and end
        ret= []
        for j in range(len(prefixSum) - k + 1):
            if j == 0 :
                tmp = prefixSum[j+k-1]
                ret.append(tmp)
            else:
                tmp = prefixSum[j+k-1] - prefixSum[j-1]
                ret.append(tmp)
        return ret

if __name__ == '__main__':
    a = [1,2,7,8,5,-11,33,4534,3322]
    s = Solution()
    ret = s.windowSum(a, 3)
    print(ret)

'''
1. 使用prefixSum，先统计前缀数组和
2. 确定好起始指针和终止指针的位置，相减即可得窗口内的和
'''