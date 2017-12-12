# coding:utf-8
'''
日期：2017年6月15日
内容：找到target最后出现的位置
'''


class Solution(object):
    def search(self, nums, target):
        # extra circumstance
        if nums is None or len(nums) == 0:
            return -1

            # start, end, middle position
        start, end = 0, len(nums) - 1
        mid = (end - start) // 2 + start
        while start + 1 < end:
            if nums[mid] == target:
                start = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
            mid = (end - start) // 2 + start

            # double check
        if nums[end] == target:
            return end
        if nums[start] == target:
            return start


if __name__ == '__main__':
    s = Solution()
    ret = s.search([1, 2, 3, 3, 4, 5, 10], 3)
    print(ret)
