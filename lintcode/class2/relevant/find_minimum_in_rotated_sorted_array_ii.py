# coding:utf-8

'''
日期：2017年6月29日
内容：http://www.lintcode.com/zh-cn/problem/find-minimum-in-rotated-sorted-array-ii/
假设一个旋转排序的数组其起始位置是未知的（比如0 1 2 4 5 6 7 可能变成是4 5 6 7 0 1 2）。
你需要找到其中最小的元素。
数组中可能存在重复的元素。
'''


class Solution(object):
    def findMinimum(self, nums):
        '''
        :param nums:
        :return:
        '''
        # 处理特殊情况
        if nums is None or len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        target = nums[-1]  # 设置比较的对象(目标值)
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                tmp = mid
                while tmp < len(nums)-1: # 这个操作是去重的重点，可以减笔记
                    if nums[tmp] != target:
                        start = mid
                        break
                    tmp += 1
                if tmp == len(nums) - 1: end = mid
            elif nums[mid] < target:
                end = mid
            else:
                start = mid

        # double check
        if nums[start] <= nums[end]:
            return nums[start]
        else:
            return nums[end]


if __name__ == '__main__':
    s = Solution()
    ret = s.findMinimum([1,1,-1,1])
    print(ret)
