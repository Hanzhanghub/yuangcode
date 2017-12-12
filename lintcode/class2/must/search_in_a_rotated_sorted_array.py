# coding:utf-8
'''
日期：2017年6月27日
内容：http://www.lintcode.com/zh-cn/problem/search-in-rotated-sorted-array/
'''


class Solution:
    """
    @param nums : a list of integers
    @param target : an integer to be searched
    @return : an integer
    """

    def search(self, nums, target):
        # 处理特殊情况
        if nums is None or len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            # 判断target和nums[mid]是否在同一侧
            if (nums[mid] - nums[-1]) * (target - nums[-1]) > 0:
                # 再判断target和nums[mid]的关系
                if nums[mid] > target:
                    end = mid
                else:
                    start = mid
            elif (nums[mid] - nums[-1]) * (target - nums[-1]) < 0:
                if nums[mid] > target:
                    start = mid
                else:
                    end = mid
            else:
                # 由于nums中元素不重复，所以此时是nums[-1] == target
                return len(nums) - 1
        # double check
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


if __name__ == '__main__':
    s = Solution()
    ret = s.search([6, 8, 9, 1, 3, 5], 5)
    print(ret)
