# coding:utf-8

'''
日期：2017年6月16日
内容：http://www.lintcode.com/zh-cn/problem/find-peak-element/
'''


class Solution:
    # @param nums: An integers list.
    # @return: return any of peek positions.
    def findPeak(self, nums):
        start, end = 1, len(nums) - 2  # 想清楚为什么
        while start + 1 < end:
            mid = (end - start) // 2 + start
            # 这是我的想法
            # if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
            #     return mid
            # elif nums[mid-1] < nums[mid] < nums[mid+1]:
            #     start = mid
            # else:
            #     end = mid

            # 九章算法
            if nums[mid] < nums[mid - 1]:
                end = mid
            elif nums[mid - 1] < nums[mid]:
                start = mid
            else:
                end = mid

            # double check
            if nums[start] > nums[end]:
                return start
            if nums[end] > nums[start]:
                return end


if __name__ == '__main__':
    s = Solution()
    ret = s.findPeak([1, 2, 1, 3, 4, 5, 7, 6])
    print(ret)
