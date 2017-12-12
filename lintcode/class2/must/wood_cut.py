# coding:utf-8

'''
日期：2017年6月27日
内容：http://www.lintcode.com/zh-cn/problem/wood-cut/
'''


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """

    def sum_for_wood(self, L, length):
        return sum([x // length for x in L])

    def woodCut(self, L, k):
        # 处理特殊情况
        if L is None or len(L) == 0:
            return 0

        start, end = 1, max(L)
        while start + 1 < end:
            mid = (start + end) // 2
            tmp = self.sum_for_wood(L, mid)
            if tmp == k:
                start = mid
            elif tmp > k:
                start = mid
            else:
                end = mid

        # double check
        if self.sum_for_wood(L, end) >= k: # 这里的>=要注意，有可能就是没有==出现，这时还是要考虑
            return end
        if self.sum_for_wood(L, start) >= k:
            return start
        return 0


s = Solution()
ret = s.woodCut([232, 124, 456], 7)
print(ret)
