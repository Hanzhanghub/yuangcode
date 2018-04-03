# coding:utf-8
'''
date:2017/12/6
content:
given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
'''

class Solution:
    """
    @param: A: A list of integers
    @return: An integer
    """
    def jump(self, A):

        p = [0]
        for i in range(len(A)-1):
            while i + A[i] >= len(p) and len(p) < len(A):
                p.append(p[i]+1)

        return p[-1]

'''
思路：
1.i表示第i个位置
2.p代表步数的列表，长度就代表了能走到的元素个数
'''
