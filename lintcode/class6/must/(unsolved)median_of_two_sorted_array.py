# coding:utf-8

'''
date: 2017/11/9
content:
两个排序的数组A和B分别含有m和n个数，找到两个排序数组的中位数，要求时间复杂度应为O(log (m+n))。

样例
给出数组A = [1,2,3,4,5,6] B = [2,3,4,5]，中位数3.5
给出数组A = [1,2,3] B = [4,5]，中位数 3
'''


class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):

        ''' quick select'''
        nums = A + B

        if not nums:
            return 0

        if len(nums) % 2 != 0:
            ret = self.quick_select(nums, 0, len(nums) - 1, len(nums) // 2)
            # print(ret)
        else:
            ret_1 = self.quick_select(nums, 0, len(nums) - 1, len(nums) // 2)
            # print(ret_1)
            ret_2 = self.quick_select(nums, 0, len(nums) - 1, len(nums) // 2 + 1)
            ret = (ret_1 + ret_2) / 2
        return ret

    def quick_select(self, nums, start, end, k):

        if start >= end:
            return nums[start]

        left = start
        right = end
        pivot = nums[(start+end)//2]

        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
                right -= 1

        # select
        if start + k - 1 <= right:
            return self.quick_select(nums, start, right, k)
        if start + k - 1 >= left:
            return self.quick_select(nums, left, end, k - (left - start))
        return nums[right+1]






            #     # step 1: calculate the length of A + B
            #     length = len(A) + len(B)
            #     # examine whether is odds
            #     if length % 2 == 1:
            #         return self.findKth(A, B, length // 2 + 1)
            #     else:
            #         small = self.findKth(A, B, length // 2)
            #         large = self.findKth(A, B, length // 2 + 1)
            #         return (small + large) / 2.0
            #
            # def findKth(self, a, b, k):
            #     # special condition
            #     if len(a) == 0:
            #         return b[k - 1]
            #     if len(b) == 0:
            #         return a[k - 1]
            #     if k == 1:
            #         return min(a[0], b[0])
            #
            #     next_a = a[k // 2 - 1] if len(a) >= k // 2 else None
            #     next_b = b[k // 2 - 1] if len(b) >= k // 2 else None
            #
            #     if next_b is None or (next is not None and next_a < next_b):
            #         return self.findKth(a[k // 2:], b, k - k // 2)
            #     return self.findKth(a, b[k // 2:], k - k // 2)


if __name__ == '__main__':
    s = Solution()
    ret = s.findMedianSortedArrays([1, 2, 3, 4, 5, 6], [2, 3, 4, 5])
    print(ret)
