# coding:utf-8

'''
date: 2017/11/14
content:
分割一个整数数组，使得奇数在前偶数在后。

样例
给定 [1, 2, 3, 4]，返回 [1, 3, 2, 4]。
'''
class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        if not nums:
            return

        odd = 0
        even = 0

        while odd < len(nums) and even < len(nums):
            while odd < len(nums) and not self.is_odd(nums[odd]):
                # number is not odd
                odd += 1

            while even < len(nums) and self.is_odd(nums[even]):
                # number is odd
                even += 1

            if odd < len(nums) and even < len(nums):
                if odd > even:
                    # exchange two number
                    tmp = nums[odd]
                    nums[odd] = nums[even]
                    nums[even] = tmp
                else:
                    odd += 1
        return nums

    def is_odd(self, number):
        # examine whether a number is odd
        if number % 2 == 0:
            return False
        else:
            return True

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    s = Solution()
    ret = s.partitionArray(nums)
    print(ret)


'''
1. 设立两根指针odd，even分别指向奇数和偶数。并让二者分别首先找到第一个odd和第一个even。
2. 判断odd和even的相对位置：
   （1）如果odd在even前面，这时则不用进行值交换，只需要将odd下标加1
   （2）如果odd在even后面，这时交换二者的值，不做其余操作
3. 这道题和之前的move_zeros很像
'''

