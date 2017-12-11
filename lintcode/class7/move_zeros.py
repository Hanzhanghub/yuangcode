# coding:utf-8

'''
date: 2017/11/9
content:
给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序

注意事项
1.必须在原数组上操作
2.最小化操作数

样例
给出 nums = [0, 1, 0, 3, 12], 调用函数之后, nums = [1, 3, 12, 0, 0].
'''


class Solution:
    """
    @param: nums: an integer array
    @return: 
    """

    def moveZeroes(self, nums):
        # special condition
        if not nums:
            return nums

        # two pointers
        point1 = 0
        point2 = 0
        while point1 < len(nums) and point2 < len(nums):
            # find the non-zero number
            while point2 < len(nums) and nums[point2] == 0:
                point2 += 1

            # find the zero index
            while point1 < len(nums) and nums[point1] != 0:
                point1 += 1

            # exchange the value
            if point2 < len(nums) and point1 < len(nums):
                if point2 > point1:
                    tmp = nums[point2]
                    nums[point2] = nums[point1]
                    nums[point1] = tmp
                else:
                    point2 += 1

        return nums

if __name__ == '__main__':
    nums = [1,2,0,2,3,0,0,0,12,0]
    s = Solution()
    ret = s.moveZeroes(nums)
    print(ret)



'''
1. 设立的两个指针，p1指向0，p2指向非零
2. 同时要考虑p1和p2的相对位置：
    1.当p1小于p2时，就交换二者的值
    2.当p1大于p2时，不交换，且p2向前一位
'''







