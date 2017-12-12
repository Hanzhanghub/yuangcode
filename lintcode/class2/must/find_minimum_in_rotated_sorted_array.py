# coding:utf-8

'''
日期：2017年6月16日
内容：http://www.lintcode.com/zh-cn/problem/find-minimum-in-rotated-sorted-array/
'''


class Solution:
    # @param nums: a rotated sorted array
    # @return: the minimum number in the array
    def findMin(self, nums):
        target = nums[len(nums) - 1]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (end - start) // 2 + start
            if nums[mid] > target:
                start = mid
            else:
                end = mid

        # double check
        return nums[start] if nums[start] < nums[end] else nums[end]


if __name__ == '__main__':
    s = Solution()
    ret = s.findMin([4, 5, 6, 7, 0, 1, 2])
    print(ret)
