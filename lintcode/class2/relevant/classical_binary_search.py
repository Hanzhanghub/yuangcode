# coding:utf-8

'''
日期：2017年6月29日
内容：http://www.lintcode.com/zh-cn/problem/classical-binary-search/
在一个排序数组中找一个数，返回该数出现的任意位置，如果不存在，返回-1
'''


class Solution(object):
    def binarySearch(self, nums, target):
        '''

        :param nums:
        :param target:
        :return:
        '''
        # 处理特殊情况
        if nums is None or len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid
            else:
                start = mid

        # double check
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
