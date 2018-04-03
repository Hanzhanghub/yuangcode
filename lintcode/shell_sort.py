# coding:utf-8

'''
date:2018/3/9
content:
希尔排序
'''

class Solution(object):
    def sort(self, nums):
        if not nums:
            return nums

        d = len(nums) // 2
        while d >= 1:
            for i in range(d+1, len(nums)):
                if nums[i] < nums[i-d]:
                    tmp = nums[i]
                    j = i - d
                    while j >=0 and nums[j] > tmp:
                        nums[j+d] = nums[j]
                        j -= d
                    nums[j+d] = tmp
            d //= 2

        return nums

if __name__ == '__main__':
    s = Solution()
    ret = s.sort([1,4,2,5,2,5,8,3,0])
    print(ret)

