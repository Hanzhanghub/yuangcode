# coding:utf-8

'''
日期：2017年6月16日
内容：http://www.lintcode.com/zh-cn/problem/first-bad-version/
'''


#
# class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
# Run unit tests to check whether verison `id` is a bad version
# return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """

    def findFirstBadVersion(self, n):
        # 处理特殊情况
        if n == 0:
            return n

        start, end = 1, n
        while start + 1 < end:
            mid = (end - start) // 2 + start
            if SVNRepo.isBadVersion(mid):
                end = mid
            else:
                start = mid

                # double check
        if SVNRepo.isBadVersion(start):
            return start
        if SVNRepo.isBadVersion(end):
            return end
