# coding:utf-8

'''
date: 2017/11/17
content:
给一个包含 n 个整数的数组 S, 找到和与给定整数 target 最接近的三元组，返回这三个数的和。

注意事项
只需要返回三元组之和，无需返回三元组本身

样例
例如 S = [-1, 2, 1, -4] and target = 1. 和最接近 1 的三元组是 -1 + 2 + 1 = 2.
'''


class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @param: target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        # special condition
        if not numbers:
            return

        # sort nums
        numbers.sort()

        # pointer declare
        result = float('inf')
        nearest_sum = float('inf')

        # slide the third pointer
        for i in range(len(numbers)):
            remain_target = target - numbers[i]
            two_sum_abs, two_sum = self.twoSumSolution(numbers, remain_target, i, result)
            if two_sum_abs < result:
                result = two_sum_abs
                nearest_sum = two_sum + numbers[i]

        return nearest_sum

    def twoSumSolution(self, nums, target, c, result):
        if not nums:
            return

        left = c + 1
        right = len(nums) - 1
        nearest_sum = 0

        while left < right:
            if nums[left] + nums[right] < target:
                # nearest examine
                if abs(nums[left] + nums[right] - target) < result:
                    result = abs(nums[left] + nums[right] - target)
                    nearest_sum = nums[left] + nums[right]
                left += 1
            elif nums[left] + nums[right] > target:
                # nearest examine
                if abs(nums[left] + nums[right] - target) < result:
                    result = abs(nums[left] + nums[right] - target)
                    nearest_sum = nums[left] + nums[right]
                right -= 1
            else:
                result = 0
                nearest_sum = nums[left] + nums[right]
                break

        return result, nearest_sum


if __name__ == '__main__':
    a = [2,7,11,15]
    s = Solution()
    ret = s.threeSumClosest(a, 3)
    print(ret)


'''
1. 基本的思路为3sum，即循环指针i，然后对nums[i+1:]做2sum。
2. 需要注意的逻辑问题：
    （1）保存两个变量result，nearest_sum，前者用于记录最小的差值（即离得最近），后者用于记录当取得最小差值时的
         三数之和
'''

