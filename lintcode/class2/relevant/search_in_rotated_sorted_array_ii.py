# coding:utf-8
'''
日期：2017年6月29日
内容：http://www.lintcode.com/zh-cn/problem/search-in-rotated-sorted-array-ii/
跟进“搜索旋转排序数组”，假如有重复元素又将如何？
是否会影响运行时间复杂度？
如何影响？
为何会影响？
写出一个函数判断给定的目标值是否出现在数组中。
'''


class Solution:
    """
    @param A : an integer ratated sorted array and duplicates are allowed
    @param target : an integer to be searched
    @return : a boolean
    """

    def judge_mid(self, nums, mid):
        flag = 0  # 0 reps left, 1 reps right
        tmp = mid
        while tmp < len(nums) - 1:
            if nums[tmp] != nums[mid]:
                flag = 0
                break
            tmp += 1
        if tmp == len(nums) - 1:
            flag = 1
        return flag

    def search(self, nums, target):
        # 处理特殊情况
        if nums is None or len(nums) == 0:
            return False

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[start]:
                if nums[start] == target or nums[mid] == target:
                    return True
                if nums[start] < target < nums[mid]:
                    end = mid
                else:
                    start = mid
            elif nums[mid] < nums[start]:
                if nums[end] == target or nums[mid] == target:
                    return True
                if nums[mid] < target < nums[end]:
                    start = mid
                else:
                    end = mid
            else:
                # nums[mid] == nums[start]
                # 判断mid在左还是在右
                if not self.judge_mid(nums, mid):  # 在左边
                    if target == nums[mid]:
                        return True
                    else:
                        start = mid
                else:
                    if target == nums[mid]:
                        return True
                    else:
                        end = mid

        # double check
        if nums[start] == target or nums[end] == target:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    ret = s.search([4,4,4,4,4,4,4,4,5,7,0,1,2,4,4,4,4],4)
    print(ret)