# coding:utf-8

'''
date: 2017/12/11
content:
给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。
你可以假设在数组中无重复元素。

样例
[1,3,5,6]，5 → 2
[1,3,5,6]，2 → 1
[1,3,5,6]， 7 → 4
[1,3,5,6]，0 → 0
'''
class Solution:
    """
    @param: A: an integer sorted array
    @param: target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        # special check
        if not A:
            return 0

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            if A[mid] == target:
                return mid
            elif A[mid] < target:
                start = mid
            else:
                end = mid
        # equal
        if A[start] == target:
            return start
        if A[end] == target:
            return end

        # non-equal
        if A[start] < target < A[end]:
            return start + 1
        elif target > A[end]:
            return end + 1
        else:
            return 0

'''
1. 这道题思路相对简单，首先使用常规的二分法进行寻找，找到即返回
2. 当找不到的时候，等循环退出后，检查几种情况：
    （1）target == A[start] or target == A[end]
    （2）target < A[start] or A[start] < target < A[end] or A[end] < target 
'''























