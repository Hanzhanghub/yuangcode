# coding:utf-8

'''
date:2018/3/9
content:
冒泡排序
'''

class Solution(object):
    def sort(self, nums):
        if not nums:
            return nums

        '''solution 1 '''
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > nums[j]:
        #             nums[i], nums[j] = nums[j], nums[i]

        '''solution 2'''
        pos = len(nums) - 1
        while pos != 0:
            bound = pos
            pos = 0
            for i in range(bound):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                    pos = i
        return nums

if __name__ == '__main__':
    s = Solution()
    ret = s.sort([13,50,27,55,38,49,65,97])
    print(ret)
