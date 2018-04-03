# coding:utf-8

'''
date:2018/3/9
content:
快速排序
'''

class Solution(object):
    def sort(self, nums):
        if not nums:
            return

        self.quick_sort(0, len(nums) - 1, nums)
        return nums

    def quick_sort(self, start, end, nums):

        if start >= end:
            return

        left = start
        right = end
        pivot = nums[(left+right)//2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and pivot < nums[right]:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quick_sort(start, right, nums)
        self.quick_sort(left, end, nums)

if __name__ == '__main__':
    s = Solution()
    ret = s.sort([1,4,2,5,2,5,8,3,0])
    print(ret)
