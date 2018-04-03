# coding:utf-8


'''
date: 2018/3/9
content:
简单选择排序
'''

class Solution(object):
    def sort(self, nums):
        if not nums:
            return nums

        for i in range(len(nums)):
            idx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[idx]:
                    idx = j
            if idx != i:
                nums[i], nums[idx] = nums[idx], nums[i]
        return nums

if __name__ == '__main__':
    s = Solution()
    ret = s.sort([1,4,2,5,2,5,8,3,0])
    print(ret)














