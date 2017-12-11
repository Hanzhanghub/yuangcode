# coding:utf-8

'''
date: 2017/11/17
content: 
find the number of two number in array which the sum is greater than target 
'''

class Solution(object):
    def two_sum_follow_up(self, nums, target):
        # special condition
        if not nums:
            return 0

        # sort nums
        nums.sort()

        # variabel defination
        count = 0
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] <= target:
                left += 1
            else:
                count += right - left
                right -= 1

        return count

if __name__ == '__main__':
    nums = [2, 7, 11, 12, 13, 15]
    target = 12
    s = Solution()
    ret = s.two_sum_follow_up(nums, target)
    print(ret)

'''
思路和two_sum_less_than_or_equal_to一样
'''


