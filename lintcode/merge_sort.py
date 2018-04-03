# coding:utf-8

'''
date:2018/3/10
content:
归并排序
'''

class Solution(object):
    def sort(self, nums):
        if not nums:
            return nums

        tmp = [None] * len(nums)
        self.merge_sort(nums, 0, len(nums) -1 , tmp)
        return nums

    def merge_sort(self, nums, start, end , tmp):
        if start >= end:
            return

        self.merge_sort(nums, start, (start + end) //2, tmp)
        self.merge_sort(nums, (start + end) // 2 +1, end, tmp)
        self.merge(nums, start, end, tmp)

    def merge(self, nums, start, end, tmp):
        mid = (start +end) //2
        left, right, index = start, mid+1, start

        while left <= mid and right <= end:
            if nums[left] < nums[right]:
                tmp[index] = nums[left]
                left += 1
                index += 1
            else:
                tmp[index] = nums[right]
                right += 1
                index += 1

        while left <= mid:
            tmp[index] = nums[left]
            left += 1
            index += 1

        while right <= end:
            tmp[index] = nums[right]
            right += 1
            index += 1

        # merge
        for i in range(start, end+1):
            nums[i] = tmp[i]



if __name__ == '__main__':
    s = Solution()
    ret = s.sort([1,4,2,5,2,5,8,3,0])
    print(ret)
