# coding:utf-8

'''
date: 2018/3/10
content:
堆排序
'''


class Solution(object):
    def sort(self, nums):

        if not nums:
            return nums

        # heapify
        for i in range(len(nums)//2, -1, -1):
            self.heapify(nums, i)

        # sort
        ret = []
        for j in range(len(nums)):
            nums[0], nums[-1] = nums[-1], nums[0]
            ret.append(nums.pop())
            self.heapify(nums, 0)

        return ret

    def heapify(self, nums, k):
        while k < len(nums):
            smallest = k
            if k * 2 + 1 < len(nums) and nums[k*2+1] < nums[smallest]:
                smallest = k * 2 +1

            if k * 2 + 2 < len(nums) and nums[k*2+2] < nums[smallest]:
                smallest = k * 2 + 2

            if smallest == k:
                break

            # exchange value
            tmp = nums[smallest]
            nums[smallest] = nums[k]
            nums[k] = tmp

            k = smallest

if __name__ == '__main__':
    s = Solution()
    ret = s.sort([1,4,2,5,2,5,8,3,0])
    print(ret)








