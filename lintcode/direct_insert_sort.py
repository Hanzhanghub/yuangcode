# coding:utf-8

'''
date: 2018/3/9
content: 
直接插入排序
'''

class Solution(object):
    def sort(self, nums):
        if not nums:
            return nums

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                tmp = nums[i]
                j = i - 1
                while j >= 0 and  tmp < nums[j]:
                    nums[j+1] = nums[j]
                    j -= 1
                nums[j+1] = tmp
        return nums

