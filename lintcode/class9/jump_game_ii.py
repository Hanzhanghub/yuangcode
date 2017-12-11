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
        ''''''

        '''Solution 2: for loop'''
        p = [0]
        for i in range(len(A) - 1):
            while (i + A[i] >= len(p) and len(p) < len(A)):
                p.append(p[i] + 1)

        return p[-1]

        '''Solution 1: DFS'''
    #     self.minimum = float('inf')
    #     ret = self.dfs_helper(0, A, 0)
    #     if ret is not None:
    #         return self.minimum
    #
    # def dfs_helper(self, indx, num, minimum):
    #     if indx >= len(num) - 1:
    #         if minimum < self.minimum:
    #             self.minimum = minimum
    #         return
    #
    #     for i in range(num[indx], -1, -1):
    #         next_indx = indx + i
    #
    #         if next_indx == indx and next_indx < len(num):
    #             return
    #
    #         self.dfs_helper(next_indx, num, minimum+1)


if __name__ == '__main__':
    a =  [2,3,1,1,4]
    s = Solution()
    ret = s.jump(a)
    print(ret)


'''
1.这道题在jump game的基础上，还有别的一些操作：
    （1）此题中不需要返回True or False，因为是要等到所有的路径都被走完才返回最小的
    （2）第二个改变就是添加一个minimum变量记录找到最后一个index时所跳过的步数
    （3）但是很可惜的是，这道题用这种解法会超时
    
2.有点巧妙，注意一下
'''
















