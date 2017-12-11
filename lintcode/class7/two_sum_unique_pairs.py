# coding:utf-8

'''
date: 2017/11/16
content:
Given an array of integers, find how many unique pairs in the array such
that their sum is equal to a specific target number. Please return the
number of pairs.

Given nums = [1,1,2,45,46,46], target = 47
return 2
1 + 46 = 47
2 + 45 = 47
'''

class Solution(object):
    def two_sum_unique_pairs(self, nums, target):

        results = []

        # special
        if not nums:
            return results

        # sort nums
        nums.sort()

        # First point to remember: Don't eliminate the repeat
        # Two pointers
        left = 0
        right = len(nums) - 1
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                # my version
                if left != 0 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                else:
                    results.append((nums[left], nums[right]))
                    left += 1

                # recommended version
                # left += 1
                # right -= 1
                # results.append((nums[left],nums[right]))
                # while left <= right and nums[left-1] == nums[left]:
                #     left += 1
                # while left <=right and nums[right+1] == nums[right]:
                #     right -= 1

        return results
        # return len(results)

if __name__ == '__main__':
    nums = [1,1,2,2,45,45,45,45,45,46,46]
    s = Solution()
    ret = s.two_sum_unique_pairs(nums, 46)
    print(ret)

'''
主要注意的点：
1. 如何避免选择重复的数，而且不能在一开头就去重。这里用到DFS和BFS中去重的思想：
   如果left的前一位与left值相同，则left往后走一位；——>
   如果right的后一位与right值相同，则right往前走一位；<——
'''



