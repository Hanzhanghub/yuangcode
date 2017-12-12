# coding:utf-8

'''
日期：2017年6月15日
内容：
http://www.lintcode.com/zh-cn/problem/first-position-of-target/
'''


class Solution(object):
    def search(self, nums, target):
        # 处理特殊情况
        if nums is None or len(nums) == 0:
            return -1
        #
        start, end = 0, len(nums) - 1
        mid = (end - start) // 2 + start
        while start + 1 < end:
            if nums[mid] == target:
                end = mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
            mid = (end - start) // 2 + start

            # double check
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


if __name__ == '__main__':
    s = Solution()
    ret = s.search([], 1)
    print(ret)
