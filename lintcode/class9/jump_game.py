# coding:utf-8

'''
date: 2017/12/6
content:
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Notice
This problem have two method which is Greedy and Dynamic Programming.

The time complexity of Greedy method is O(n).
The time complexity of Dynamic Programming method is O(n^2).

We manually set the small data set to allow you pass the test in both ways. 
This is just to let you learn how to use this problem in dynamic programming ways. 
If you finish it in dynamic programming ways, you can try greedy method to make it accept again.

Example
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.
'''
class Solution:
    """
    @param: A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):

        result = self.dfs_helper(0, A)
        return result

    def dfs_helper(self, indx, num):
        if indx >= len(num) - 1:
            return True

        for i in range(num[indx], -1, -1):
            next_indx = indx + i

            if next_indx == indx and next_indx < len(num):
                return False

            ret = self.dfs_helper(next_indx, num)
            if ret is True:
                return True

        return False



if __name__ == '__main__':
    a = [1,0]
    # a = [2,3,1,1,4]
    s = Solution()
    ret = s.canJump(a)
    print(ret)

'''
1. 这道题的思路：从i=0开始，使用递归的思想，对range(A[i])从大到小取值。next_index = i + range(A[i]),然后
   利用递归的思想重复上面的过程，直到：
    （1）next_index >= len(A) - 1，就一直往回弹True
    （2）如果next_index == indx, 说明这次加的数是0。那么如果next_index < len(num) - 1，我们就返回False
    

'''

















