# coding:utf-8
'''
日期：2017年6月28日
内容：http://www.lintcode.com/zh-cn/problem/copy-books/
'''


class Solution(object):
    def search_k(self, pages, target):
        #TODO：这里要重点理解
        sum = pages[0]
        copier = 1
        for i in range(1, len(pages)):
            if sum + pages[i] > target:
                copier += 1
                sum = 0
            sum += pages[i]
        return copier

    def copyBooks(self, pages, k):
        # 处理特殊情况
        if pages is None or len(pages) == 0:
            return 0

        start, end = max(pages), sum(pages)
        while start + 1 < end:
            mid = (start + end) // 2
            if self.search_k(pages, mid) > k:
                start = mid
            else:
                end = mid

        # double check
        if self.search_k(pages, start) <= k:
            return start
        if self.search_k(pages, end) <= k:
            return end


s = Solution()
ret = s.copyBooks([3, 2, 4], 2)
print(ret)
