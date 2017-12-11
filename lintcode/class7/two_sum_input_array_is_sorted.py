# coding:utf-8

'''
date: 2017/11/16
content:
给定一个已经按升序排列的数组，找到两个数使他们加起来的和等于特定数。
函数应该返回这两个数的下标，index1必须小于index2。注意返回的值不是 0-based。

注意事项
你可以假设每个输入刚好只有一个答案

样例
给定数组为 [2,7,11,15] ，target = 9
返回 [1,2]
'''

class Solution:
    """
    @param: nums: an array of Integer
    @param: target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        results = []
        # special
        if not nums:
            return results

        # Solution 1: two pointers
        self.twoPointerSolution(nums, target, results)

        # Solution 2: hash map
        # self.hashMapSolution(nums, target, results)

        return results

    def twoPointerSolution(self, nums, target, results):
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                results.append(left+1)
                results.append(right+1)
                break

        return

if __name__ == '__main__':
    a = [2,7,11,15]
    s = Solution()
    ret = s.twoSum(a, 9)
    print(ret)

'''
1,这道题可以用两种方法来做，一是hash map，二是two pointers，我在此题中采用了第二种方法
2.能够使用two pointers的做法，前提是我们必须要（能）对array排序，
3.具体的实现中，牢记两个规律：（都是因为这个array是已经排好序的了）
    （1）left + right > target,则要让right -= 1
    （2）left + right < target,则要让left += 1 
'''



