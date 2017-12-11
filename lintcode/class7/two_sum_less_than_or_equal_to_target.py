# coding:utf-8

'''
date: 2017/11/17
content:
Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.

Example
Given nums = [2, 7, 11, 15], target = 24. 
Return 5. 
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 25
'''
class Solution(object):
    def two_sum_follow_up(self, nums, target):
        # special
        if not nums:
            return 0

        # sort nums
        nums.sort()

        count = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] <= target:
                count += right - left # key point: how to count the number of pairs
                left += 1
            else:
                right -= 1

        return count

if __name__ == '__main__':
    nums = [2, 7, 11, 12, 13, 15]
    s = Solution()
    ret = s.two_sum_follow_up(nums, 24)
    print(ret)

'''
使用两指针的方法，有一点需要注意：
1. 当nums[left] + nums[right] <= target成立时，就可以直接使用right - left来计算此时的满足条件的pair的个数。
'''





